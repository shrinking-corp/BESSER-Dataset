from enum import Enum
from python_code import ActivityUseKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ActivityUseKind.na, '\x00', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ActivityUseKind.na, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ActivityUseKind.na, '', '', '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ActivityUseKind.na, 0)

def test_Enum___new___2():
    assert Enum.__new__(ActivityUseKind.na, 'na') == ActivityUseKind.na

from enum import Enum
from python_code import ContractKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ContractKind.EXPRESS, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ContractKind.IMPLIED, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ContractKind.IMPLIED, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ContractKind.OTHER, 0)

def test_Enum___new___2():
    assert Enum.__new__(ContractKind.OTHER, 'OTHER') == ContractKind.OTHER

from enum import Enum
from python_code import EstimatingTechnique
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(EstimatingTechnique.COST, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(EstimatingTechnique.TIME, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(EstimatingTechnique.TIME, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(EstimatingTechnique.COST, 0)

def test_Enum___new___2():
    assert Enum.__new__(EstimatingTechnique.TIME, 'TIME') == EstimatingTechnique.TIME

from enum import Enum
from python_code import ExpertiseLevel
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ExpertiseLevel.LOW, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ExpertiseLevel.LOW, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ExpertiseLevel.LOW, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ExpertiseLevel.LOW, 0)

def test_Enum___new___2():
    assert Enum.__new__(ExpertiseLevel.LOW, 'LOW') == ExpertiseLevel.LOW

from enum import Enum
from python_code import OptionalityKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(OptionalityKind.optional, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(OptionalityKind.optional, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(OptionalityKind.mandatory, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(OptionalityKind.optional, 0)

def test_Enum___new___2():
    assert Enum.__new__(OptionalityKind.optional, 'optional') == OptionalityKind.optional

from enum import Enum
from python_code import ParameterDirectionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ParameterDirectionKind.in_, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ParameterDirectionKind.in_, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ParameterDirectionKind.in_, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ParameterDirectionKind.out, 0)

def test_Enum___new___2():
    assert Enum.__new__(ParameterDirectionKind.out, 'in_') == ParameterDirectionKind.in_

from enum import Enum
from python_code import RiskLevel
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(RiskLevel.LOW, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(RiskLevel.LOW, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(RiskLevel.LOW, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(RiskLevel.LOW, 0)

def test_Enum___new___2():
    assert Enum.__new__(RiskLevel.LOW, 'LOW') == RiskLevel.LOW

from enum import Enum
from python_code import VariabilityType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(VariabilityType.na, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(VariabilityType.na, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(VariabilityType.na, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(VariabilityType.na, 0)

def test_Enum___new___2():
    assert Enum.__new__(VariabilityType.na, 'na') == VariabilityType.na

from enum import Enum
from python_code import WorkSequenceKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(WorkSequenceKind.startToStart, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(WorkSequenceKind.startToStart, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(WorkSequenceKind.startToStart, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(WorkSequenceKind.startToStart, 0)

def test_Enum___new___2():
    assert Enum.__new__(WorkSequenceKind.startToStart, 'startToStart') == WorkSequenceKind.startToStart

from python_code import spem_MethodContentPackage
from python_code import spem_MethodContentPackageableElement

def test_spem_MethodContentPackageableElement___init__():
    assert spem_MethodContentPackageableElement.__init__(spem_MethodContentPackageableElement('', spem_MethodContentPackageableElement=spem_MethodContentPackage()), '', spem_MethodContentPackageableElement=spem_MethodContentPackage()) == None

from python_code import spem_MethodContentUse

def test_spem_MethodContentUse___init__():
    assert spem_MethodContentUse.__init__(spem_MethodContentUse(True), False) == None

from python_code import spem_MethodLibraryPackageableElement

def test_spem_MethodLibraryPackageableElement___init__():
    assert spem_MethodLibraryPackageableElement.__init__(spem_MethodLibraryPackageableElement(''), '') == None

from python_code import spem_ProcessPackage
from python_code import spem_ProcessPackageableElement

def test_spem_ProcessPackageableElement___init__():
    assert spem_ProcessPackageableElement.__init__(spem_ProcessPackageableElement('', spem_ProcessPackageableElement=spem_ProcessPackage()), '', spem_ProcessPackageableElement=spem_ProcessPackage()) == None

from python_code import spem_CompositeRole
from python_code import spem_Default_ResponsibilityAssignment
from python_code import spem_Default_TaskDefinitionPerformer
from python_code import spem_RoleDefinition
from python_code import spem_RoleUse

def test_spem_RoleDefinition___init__():
    assert spem_RoleDefinition.__init__(spem_RoleDefinition('', spem_RoleDefinition=spem_RoleUse(), spem_RoleDefinition104=set(), spem_RoleDefinition117=spem_Default_ResponsibilityAssignment(), spem_RoleDefinition115=spem_Default_TaskDefinitionPerformer(), spem_RoleDefinition136=spem_CompositeRole()), '', spem_RoleDefinition=spem_RoleUse(), spem_RoleDefinition104=set(), spem_RoleDefinition117=spem_Default_ResponsibilityAssignment(), spem_RoleDefinition115=spem_Default_TaskDefinitionPerformer(), spem_RoleDefinition136=spem_CompositeRole()) == None

from python_code import spem_WorkDefinition

def test_spem_WorkDefinition___init__():
    assert spem_WorkDefinition.__init__(spem_WorkDefinition('', '', spem_WorkDefinition=set()), '', '', spem_WorkDefinition=set()) == None

from python_code import spem_uma_Deliverable

def test_spem_uma_Deliverable___init__():
    assert spem_uma_Deliverable.__init__(spem_uma_Deliverable('\x00\x00', '', spem_uma_Deliverable=set()), '', '', spem_uma_Deliverable=set()) == None

from python_code import spem_uma_DeliveryProcess
from python_code import spem_uma_Discipline
from python_code import spem_uma_ProcessPlanningTemplate

def test_spem_uma_DeliveryProcess___init__():
    assert spem_uma_DeliveryProcess.__init__(spem_uma_DeliveryProcess('', '', '\x00', '', '', '', spem_uma_DeliveryProcess=set(), spem_uma_DeliveryProcess214=set(), Process231=spem_uma_ProcessPlanningTemplate(), Process=spem_uma_Discipline()), '', '', '', '', '', '', spem_uma_DeliveryProcess=set(), spem_uma_DeliveryProcess214=set(), Process231=spem_uma_ProcessPlanningTemplate(), Process=spem_uma_Discipline()) == None

from python_code import spem_uma_Practice

def test_spem_uma_Practice___init__():
    assert spem_uma_Practice.__init__(spem_uma_Practice('', '', '', '', '', '', spem_uma_Practice=set(), spem_uma_Practice227=set(), spem_uma_Practice229=set()), '', '', '', '', '\x00', '', spem_uma_Practice=set(), spem_uma_Practice227=set(), spem_uma_Practice229=set()) == None

from python_code import spem_uma_Process

def test_spem_uma_Process___init__():
    assert spem_uma_Process.__init__(spem_uma_Process('', '', spem_uma_Process=set(), spem_uma_Process211=set()), '', '', spem_uma_Process=set(), spem_uma_Process211=set()) == None
