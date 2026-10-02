from enum import Enum
from python_code import ActivityImplementationType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ActivityImplementationType.Manual, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ActivityImplementationType.Route, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ActivityImplementationType.Manual, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ActivityImplementationType.Route, 0)

def test_Enum___new___2():
    assert Enum.__new__(ActivityImplementationType.Route, 'Route') == ActivityImplementationType.Route

from enum import Enum
from python_code import DiagramModeType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DiagramModeType.MODE_4_5_0, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DiagramModeType.MODE_4_5_0, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DiagramModeType.MODE_4_0_0, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DiagramModeType.MODE_4_5_0, 0)

def test_Enum___new___2():
    assert Enum.__new__(DiagramModeType.MODE_4_5_0, 'MODE_4_5_0') == DiagramModeType.MODE_4_5_0

from enum import Enum
from python_code import DirectionType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DirectionType.IN, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DirectionType.IN, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DirectionType.IN, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DirectionType.IN, 0)

def test_Enum___new___2():
    assert Enum.__new__(DirectionType.IN, 'IN') == DirectionType.IN

from enum import Enum
from python_code import FlowControlType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FlowControlType.none, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FlowControlType.none, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FlowControlType.none, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FlowControlType.join, 0)

def test_Enum___new___2():
    assert Enum.__new__(FlowControlType.join, 'none') == FlowControlType.none

from enum import Enum
from python_code import ImplementationType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ImplementationType.push, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ImplementationType.push, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ImplementationType.push, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ImplementationType.push, 0)

def test_Enum___new___2():
    assert Enum.__new__(ImplementationType.push, 'push') == ImplementationType.push

from enum import Enum
from python_code import JoinSplitType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(JoinSplitType.AND, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(JoinSplitType.OR, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(JoinSplitType.OR, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(JoinSplitType.OR, 0)

def test_Enum___new___2():
    assert Enum.__new__(JoinSplitType.OR, 'OR') == JoinSplitType.OR

from enum import Enum
from python_code import LinkCardinality
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LinkCardinality.Many, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LinkCardinality.Many, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LinkCardinality.Many, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LinkCardinality.One, 0)

def test_Enum___new___2():
    assert Enum.__new__(LinkCardinality.One, 'One') == LinkCardinality.One

from enum import Enum
from python_code import LinkColor
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LinkColor.Black, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LinkColor.Red, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LinkColor.Red, 0, 0, '') == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LinkColor.Red, '')

def test_Enum___new___2():
    assert Enum.__new__(LinkColor.Red, 'Black') == LinkColor.Black

from enum import Enum
from python_code import LinkEndStyle
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LinkEndStyle.NoArrow, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LinkEndStyle.NoArrow, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LinkEndStyle.NoArrow, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LinkEndStyle.NoArrow, 0)

def test_Enum___new___2():
    assert Enum.__new__(LinkEndStyle.NoArrow, 'NoArrow') == LinkEndStyle.NoArrow

from enum import Enum
from python_code import LinkLineStyle
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LinkLineStyle.Normal, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LinkLineStyle.Normal, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LinkLineStyle.Normal, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LinkLineStyle.Normal, 0)

def test_Enum___new___2():
    assert Enum.__new__(LinkLineStyle.Normal, 'Normal') == LinkLineStyle.Normal

from enum import Enum
from python_code import LoopType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LoopType.While, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LoopType.None_, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LoopType.None_, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LoopType.While, 0)

def test_Enum___new___2():
    assert Enum.__new__(LoopType.None_, 'None_') == LoopType.None_

from enum import Enum
from python_code import OrientationType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(OrientationType.Vertical, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(OrientationType.Vertical, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(OrientationType.Vertical, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(OrientationType.Vertical, 0)

def test_Enum___new___2():
    assert Enum.__new__(OrientationType.Vertical, 'Vertical') == OrientationType.Vertical

from enum import Enum
from python_code import RoutingType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(RoutingType.Manhattan, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(RoutingType.Default, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(RoutingType.Explicit, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(RoutingType.Default, 0)

def test_Enum___new___2():
    assert Enum.__new__(RoutingType.Default, 'Default') == RoutingType.Default

from enum import Enum
from python_code import SubProcessModeType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(SubProcessModeType.sync_shared, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(SubProcessModeType.sync_shared, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(SubProcessModeType.sync_shared, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(SubProcessModeType.sync_shared, 0)

def test_Enum___new___2():
    assert Enum.__new__(SubProcessModeType.sync_shared, 'sync_shared') == SubProcessModeType.sync_shared

from python_code import carnot_AbstractEventSymbol

def test_carnot_AbstractEventSymbol___init__():
    assert carnot_AbstractEventSymbol.__init__(carnot_AbstractEventSymbol(''), '') == None

from python_code import carnot_DocumentRoot

def test_carnot_DocumentRoot___init__():
    assert carnot_DocumentRoot.__init__(carnot_DocumentRoot('', carnot_DocumentRoot174=set(), carnot_DocumentRoot=set(), carnot_DocumentRoot171=set()), '', carnot_DocumentRoot174=set(), carnot_DocumentRoot=set(), carnot_DocumentRoot171=set()) == None

from python_code import carnot_IGraphicalObject
from python_code import carnot_RefersToConnectionType

def test_carnot_IGraphicalObject___init__():
    assert carnot_IGraphicalObject.__init__(carnot_IGraphicalObject('', '', '', to=set(), from_=set(), IGraphicalObject=carnot_RefersToConnectionType(), IGraphicalObject311=carnot_RefersToConnectionType()), '', '', '', to=set(), from_=set(), IGraphicalObject=carnot_RefersToConnectionType(), IGraphicalObject311=carnot_RefersToConnectionType()) == None

from python_code import carnot_IIdentifiableElement

def test_carnot_IIdentifiableElement___init__():
    assert carnot_IIdentifiableElement.__init__(carnot_IIdentifiableElement('', '\x00'), '\x00\x00', '') == None

from python_code import carnot_IMetaType

def test_carnot_IMetaType___init__():
    assert carnot_IMetaType.__init__(carnot_IMetaType(''), '') == None

def test_carnot_IMetaType_getTypedElements():
    assert carnot_IMetaType.getTypedElements(carnot_IMetaType('')) == None

def test_carnot_IMetaType_getExtensionPointId():
    assert carnot_IMetaType.getExtensionPointId(carnot_IMetaType('')) == None

from python_code import carnot_IModelElement
from python_code import carnot_ViewableType

def test_carnot_IModelElement___init__():
    assert carnot_IModelElement.__init__(carnot_IModelElement('', carnot_IModelElement=carnot_ViewableType()), '', carnot_IModelElement=carnot_ViewableType()) == None

from python_code import carnot_IModelElementNodeSymbol

def test_carnot_IModelElementNodeSymbol___init__():
    assert carnot_IModelElementNodeSymbol.__init__(carnot_IModelElementNodeSymbol()) == None

def test_carnot_IModelElementNodeSymbol_getModelElement():
    assert carnot_IModelElementNodeSymbol.getModelElement(carnot_IModelElementNodeSymbol()) == None

def test_carnot_IModelElementNodeSymbol_setModelElement():
    assert carnot_IModelElementNodeSymbol.setModelElement(carnot_IModelElementNodeSymbol(), '') == None

from python_code import carnot_GenericLinkConnectionType
from python_code import carnot_INodeSymbol

def test_carnot_INodeSymbol___init__():
    assert carnot_INodeSymbol.__init__(carnot_INodeSymbol('', '', '', '', '\x00', targetSymbol=set(), sourceSymbol=set(), INodeSymbol=carnot_GenericLinkConnectionType(), INodeSymbol199=carnot_GenericLinkConnectionType()), '', '', '', '', '', targetSymbol=set(), sourceSymbol=set(), INodeSymbol=carnot_GenericLinkConnectionType(), INodeSymbol199=carnot_GenericLinkConnectionType()) == None

def test_carnot_INodeSymbol_getOutConnectionFeatures():
    assert carnot_INodeSymbol.getOutConnectionFeatures(carnot_INodeSymbol('\x00', '', '', '', '', targetSymbol=set(), sourceSymbol=set(), INodeSymbol=carnot_GenericLinkConnectionType(), INodeSymbol199=carnot_GenericLinkConnectionType())) == None

def test_carnot_INodeSymbol_getInConnectionFeatures():
    assert carnot_INodeSymbol.getInConnectionFeatures(carnot_INodeSymbol('\x00', '', '', '', '', targetSymbol=set(), sourceSymbol=set(), INodeSymbol=carnot_GenericLinkConnectionType(), INodeSymbol199=carnot_GenericLinkConnectionType())) == None

from python_code import carnot_IModelParticipant
from python_code import carnot_ISwimlaneSymbol
from python_code import carnot_LaneSymbol

def test_carnot_ISwimlaneSymbol___init__():
    assert carnot_ISwimlaneSymbol.__init__(carnot_ISwimlaneSymbol('\x00\x00', '', performedSwimlanes=carnot_IModelParticipant(), parentLane=set(), carnot_ISwimlaneSymbol=carnot_IModelParticipant(), ISwimlaneSymbol=carnot_IModelParticipant(), ISwimlaneSymbol203=carnot_LaneSymbol()), '', '', performedSwimlanes=carnot_IModelParticipant(), parentLane=set(), carnot_ISwimlaneSymbol=carnot_IModelParticipant(), ISwimlaneSymbol=carnot_IModelParticipant(), ISwimlaneSymbol203=carnot_LaneSymbol()) == None
