from enum import Enum
from python_code import AccessPolicyKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AccessPolicyKind.Read, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AccessPolicyKind.Write, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AccessPolicyKind.Write, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AccessPolicyKind.Read, 0)

def test_Enum___new___2():
    assert Enum.__new__(AccessPolicyKind.Read, 'Read') == AccessPolicyKind.Read

from enum import Enum
from python_code import AllocationEndKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AllocationEndKind.undef, '\x00', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AllocationEndKind.both, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AllocationEndKind.both, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AllocationEndKind.both, 0)

def test_Enum___new___2():
    assert Enum.__new__(AllocationEndKind.both, 'both') == AllocationEndKind.both

from enum import Enum
from python_code import AllocationKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AllocationKind.hybrid, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AllocationKind.hybrid, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AllocationKind.hybrid, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AllocationKind.hybrid, 0)

def test_Enum___new___2():
    assert Enum.__new__(AllocationKind.hybrid, 'hybrid') == AllocationKind.hybrid

from enum import Enum
from python_code import AllocationNature
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AllocationNature.timeScheduling, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AllocationNature.timeScheduling, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AllocationNature.timeScheduling, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AllocationNature.timeScheduling, 0)

def test_Enum___new___2():
    assert Enum.__new__(AllocationNature.timeScheduling, 'timeScheduling') == AllocationNature.timeScheduling

from enum import Enum
from python_code import AssignmentKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AssignmentKind.hybrid, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AssignmentKind.hybrid, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AssignmentKind.hybrid, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AssignmentKind.hybrid, 0)

def test_Enum___new___2():
    assert Enum.__new__(AssignmentKind.hybrid, 'hybrid') == AssignmentKind.hybrid

from enum import Enum
from python_code import AssignmentNature
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AssignmentNature.timeScheduling, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AssignmentNature.timeScheduling, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AssignmentNature.timeScheduling, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AssignmentNature.timeScheduling, 0)

def test_Enum___new___2():
    assert Enum.__new__(AssignmentNature.timeScheduling, 'timeScheduling') == AssignmentNature.timeScheduling

from enum import Enum
from python_code import CacheType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CacheType.data, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CacheType.undef, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CacheType.data, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CacheType.data, 0)

def test_Enum___new___2():
    assert Enum.__new__(CacheType.data, 'data') == CacheType.data

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
from python_code import ClientServerKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ClientServerKind.proreq, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ClientServerKind.proreq, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ClientServerKind.proreq, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ClientServerKind.proreq, 0)

def test_Enum___new___2():
    assert Enum.__new__(ClientServerKind.proreq, 'proreq') == ClientServerKind.proreq

from enum import Enum
from python_code import ComponentKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ComponentKind.port, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ComponentKind.card, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ComponentKind.chip, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ComponentKind.port, 0)

def test_Enum___new___2():
    assert Enum.__new__(ComponentKind.chip, 'chip') == ComponentKind.chip

from enum import Enum
from python_code import ComponentState
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ComponentState.other, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ComponentState.undef, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ComponentState.undef, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ComponentState.other, 0)

def test_Enum___new___2():
    assert Enum.__new__(ComponentState.other, 'undef') == ComponentState.undef

from enum import Enum
from python_code import ConcurrencyKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ConcurrencyKind.reader, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ConcurrencyKind.reader, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ConcurrencyKind.reader, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ConcurrencyKind.reader, 0)

def test_Enum___new___2():
    assert Enum.__new__(ConcurrencyKind.reader, 'reader') == ConcurrencyKind.reader

from enum import Enum
from python_code import ConcurrentAccessProtocolKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ConcurrentAccessProtocolKind.PIP, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ConcurrentAccessProtocolKind.PCP, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ConcurrentAccessProtocolKind.PCP, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ConcurrentAccessProtocolKind.PIP, 0)

def test_Enum___new___2():
    assert Enum.__new__(ConcurrentAccessProtocolKind.PCP, 'PCP') == ConcurrentAccessProtocolKind.PCP

from enum import Enum
from python_code import ConditionType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ConditionType.undef, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ConditionType.undef, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ConditionType.undef, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ConditionType.undef, 0)

def test_Enum___new___2():
    assert Enum.__new__(ConditionType.undef, 'other') == ConditionType.other

from enum import Enum
from python_code import ConstraintKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ConstraintKind.offered, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ConstraintKind.offered, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ConstraintKind.offered, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ConstraintKind.offered, 0)

def test_Enum___new___2():
    assert Enum.__new__(ConstraintKind.offered, 'offered') == ConstraintKind.offered

from enum import Enum
from python_code import DataPoolOrderingKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(DataPoolOrderingKind.FIFO, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(DataPoolOrderingKind.FIFO, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(DataPoolOrderingKind.FIFO, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(DataPoolOrderingKind.FIFO, 0)

def test_Enum___new___2():
    assert Enum.__new__(DataPoolOrderingKind.FIFO, 'FIFO') == DataPoolOrderingKind.FIFO

from enum import Enum
from python_code import ExecutionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ExecutionKind.deferred, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ExecutionKind.deferred, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ExecutionKind.deferred, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ExecutionKind.deferred, 0)

def test_Enum___new___2():
    assert Enum.__new__(ExecutionKind.deferred, 'deferred') == ExecutionKind.deferred

from enum import Enum
from python_code import FlowDirectionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FlowDirectionKind.in_, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FlowDirectionKind.in_, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FlowDirectionKind.in_, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FlowDirectionKind.out, 0)

def test_Enum___new___2():
    assert Enum.__new__(FlowDirectionKind.out, 'in_') == FlowDirectionKind.in_

from enum import Enum
from python_code import ISA_Type
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ISA_Type.RISC, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ISA_Type.CISC, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ISA_Type.SIMD, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ISA_Type.VLIW, 0)

def test_Enum___new___2():
    assert Enum.__new__(ISA_Type.CISC, 'RISC') == ISA_Type.RISC

from enum import Enum
from python_code import InterruptKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(InterruptKind.Other, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(InterruptKind.Other, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(InterruptKind.Undef, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(InterruptKind.Other, 0)

def test_Enum___new___2():
    assert Enum.__new__(InterruptKind.Undef, 'Other') == InterruptKind.Other

from enum import Enum
from python_code import LaxityKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LaxityKind.hard, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LaxityKind.hard, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LaxityKind.hard, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LaxityKind.soft, 0)

def test_Enum___new___2():
    assert Enum.__new__(LaxityKind.soft, 'hard') == LaxityKind.hard

from python_code import Alloc_MARTE_Abstraction
from python_code import MARTE_Alloc_Allocate

def test_MARTE_Alloc_Allocate___init__():
    assert MARTE_Alloc_Allocate.__init__(MARTE_Alloc_Allocate('\x00\x00', '', MARTE_Alloc_Allocate=Alloc_MARTE_Abstraction(), MARTE_Alloc_Allocate48=set()), '', '', MARTE_Alloc_Allocate=Alloc_MARTE_Abstraction(), MARTE_Alloc_Allocate48=set()) == None

from python_code import Alloc_MARTE_ActivityPartition
from python_code import MARTE_Alloc_AllocateActivityGroup

def test_MARTE_Alloc_AllocateActivityGroup___init__():
    assert MARTE_Alloc_AllocateActivityGroup.__init__(MARTE_Alloc_AllocateActivityGroup('', MARTE_Alloc_AllocateActivityGroup=Alloc_MARTE_ActivityPartition()), '', MARTE_Alloc_AllocateActivityGroup=Alloc_MARTE_ActivityPartition()) == None

from python_code import Alloc_MARTE_NamedElement
from python_code import MARTE_Alloc_Allocated

def test_MARTE_Alloc_Allocated___init__():
    assert MARTE_Alloc_Allocated.__init__(MARTE_Alloc_Allocated('', MARTE_Alloc_Allocated=Alloc_MARTE_NamedElement(), MARTE_Alloc_Allocated31=set(), MARTE_Alloc_Allocated29=set()), '', MARTE_Alloc_Allocated=Alloc_MARTE_NamedElement(), MARTE_Alloc_Allocated31=set(), MARTE_Alloc_Allocated29=set()) == None
