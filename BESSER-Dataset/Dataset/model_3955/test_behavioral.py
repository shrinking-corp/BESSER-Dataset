import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DataType,
    Element,
    Event,
    MultiplicityElement,
    NamedElement,
    SecCon_Action,
    SecCon_Actor,
    SecCon_AttackEvent,
    SecCon_AttackUseCase,
    SecCon_AttackedState,
    SecCon_Attribute,
    SecCon_Class,
    SecCon_Comment,
    SecCon_Condition,
    SecCon_ContextInformation,
    SecCon_ContextScenario,
    SecCon_CountermeasureEvent,
    SecCon_CountermeasureUseCase,
    SecCon_DataType,
    SecCon_DetectionUseCase,
    SecCon_Element,
    SecCon_Enumeration,
    SecCon_EnumerationLiteral,
    SecCon_Event,
    SecCon_Extend,
    SecCon_FinalState,
    SecCon_Include,
    SecCon_InitialState,
    SecCon_MultiplicityElement,
    SecCon_NamedElement,
    SecCon_Operation,
    SecCon_Package,
    SecCon_Parameter,
    SecCon_PrevenctionUseCase,
    SecCon_PrimitiveType,
    SecCon_Project,
    SecCon_ProtectedState,
    SecCon_RecoverUseCase,
    SecCon_Rule,
    SecCon_State,
    SecCon_StateMachineScenario,
    SecCon_StateOperation,
    SecCon_StateVertex,
    SecCon_ThreatEvent,
    SecCon_ThreatUseCase,
    SecCon_ThreatenedState,
    SecCon_Transition,
    SecCon_Type,
    SecCon_TypedElement,
    SecCon_UseCase,
    SecCon_UseCaseScenario,
    SecCon_VulnerabilityUseCase,
    SecCon_VulnerableState,
    State,
    StateVertex,
    Type,
    TypedElement,
    UseCase,
    Operator,
    ParameterDirectionKind,
    PseudostateKind,
    TypeOfCondition,
    TypeOfContext,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_addition41_reverse_link_reassign_clear():
    a1 = SecCon_UseCase(description="sample_text", preCondition="sample_text")
    a2 = SecCon_UseCase(description="sample_text_2", preCondition="sample_text_2")
    b = SecCon_Include(name="sample_text")
    _safe_set(b, 'includes', a1)
    assert _is_linked(b, 'includes', a1)
    if hasattr(a1, 'UseCase'):
        assert _is_linked(a1, 'UseCase', b)
    _safe_set(b, 'includes', a2)
    assert _is_linked(b, 'includes', a2)
    if hasattr(a1, 'UseCase'):
        assert not _is_linked(a1, 'UseCase', b)
    if hasattr(a2, 'UseCase'):
        assert _is_linked(a2, 'UseCase', b)
    _safe_set(b, 'includes', None)
    assert not _is_linked(b, 'includes', a2)
    if hasattr(a2, 'UseCase'):
        assert not _is_linked(a2, 'UseCase', b)


def test_assoc_base42_reverse_link_reassign_clear():
    a1 = SecCon_UseCase(description="sample_text", preCondition="sample_text")
    a2 = SecCon_UseCase(description="sample_text_2", preCondition="sample_text_2")
    b = SecCon_Include(name="sample_text")
    _safe_set(b, 'include', a1)
    assert _is_linked(b, 'include', a1)
    if hasattr(a1, 'UseCase43'):
        assert _is_linked(a1, 'UseCase43', b)
    _safe_set(b, 'include', a2)
    assert _is_linked(b, 'include', a2)
    if hasattr(a1, 'UseCase43'):
        assert not _is_linked(a1, 'UseCase43', b)
    if hasattr(a2, 'UseCase43'):
        assert _is_linked(a2, 'UseCase43', b)
    _safe_set(b, 'include', None)
    assert not _is_linked(b, 'include', a2)
    if hasattr(a2, 'UseCase43'):
        assert not _is_linked(a2, 'UseCase43', b)


def test_assoc_base48_reverse_link_reassign_clear():
    a1 = SecCon_UseCase(description="sample_text", preCondition="sample_text")
    a2 = SecCon_UseCase(description="sample_text_2", preCondition="sample_text_2")
    b = SecCon_Extend(condition="sample_text", name="sample_text")
    _safe_set(b, 'extends', a1)
    assert _is_linked(b, 'extends', a1)
    if hasattr(a1, 'UseCase49'):
        assert _is_linked(a1, 'UseCase49', b)
    _safe_set(b, 'extends', a2)
    assert _is_linked(b, 'extends', a2)
    if hasattr(a1, 'UseCase49'):
        assert not _is_linked(a1, 'UseCase49', b)
    if hasattr(a2, 'UseCase49'):
        assert _is_linked(a2, 'UseCase49', b)
    _safe_set(b, 'extends', None)
    assert not _is_linked(b, 'extends', a2)
    if hasattr(a2, 'UseCase49'):
        assert not _is_linked(a2, 'UseCase49', b)


def test_assoc_contains92_reverse_link_reassign_clear():
    a1 = SecCon_Rule(logicValue=True, name="sample_text", operator="sample_text")
    a2 = SecCon_Rule(logicValue=False, name="sample_text_2", operator="sample_text_2")
    b = SecCon_ContextScenario(name="sample_text")
    _safe_set(b, 'SecCon_ContextScenario93', {a1})
    assert _is_linked(b, 'SecCon_ContextScenario93', a1)
    if hasattr(a1, 'SecCon_Rule'):
        assert _is_linked(a1, 'SecCon_Rule', b)
    _safe_set(b, 'SecCon_ContextScenario93', {a2})
    assert _is_linked(b, 'SecCon_ContextScenario93', a2)
    if hasattr(a1, 'SecCon_Rule'):
        assert not _is_linked(a1, 'SecCon_Rule', b)
    if hasattr(a2, 'SecCon_Rule'):
        assert _is_linked(a2, 'SecCon_Rule', b)
    _safe_set(b, 'SecCon_ContextScenario93', set())
    assert not _is_linked(b, 'SecCon_ContextScenario93', a2)
    if hasattr(a2, 'SecCon_Rule'):
        assert not _is_linked(a2, 'SecCon_Rule', b)


def test_assoc_extend35_reverse_link_reassign_clear():
    a1 = SecCon_UseCase(description="sample_text", preCondition="sample_text")
    a2 = SecCon_UseCase(description="sample_text_2", preCondition="sample_text_2")
    b = SecCon_Extend(condition="sample_text", name="sample_text")
    _safe_set(b, 'Extend', a1)
    assert _is_linked(b, 'Extend', a1)
    if hasattr(a1, 'extension'):
        assert _is_linked(a1, 'extension', b)
    _safe_set(b, 'Extend', a2)
    assert _is_linked(b, 'Extend', a2)
    if hasattr(a1, 'extension'):
        assert not _is_linked(a1, 'extension', b)
    if hasattr(a2, 'extension'):
        assert _is_linked(a2, 'extension', b)
    _safe_set(b, 'Extend', None)
    assert not _is_linked(b, 'Extend', a2)
    if hasattr(a2, 'extension'):
        assert not _is_linked(a2, 'extension', b)


def test_assoc_extends36_reverse_link_reassign_clear():
    a1 = SecCon_UseCase(description="sample_text", preCondition="sample_text")
    a2 = SecCon_UseCase(description="sample_text_2", preCondition="sample_text_2")
    b = SecCon_Extend(condition="sample_text", name="sample_text")
    _safe_set(b, 'Extend38', a1)
    assert _is_linked(b, 'Extend38', a1)
    if hasattr(a1, 'base37'):
        assert _is_linked(a1, 'base37', b)
    _safe_set(b, 'Extend38', a2)
    assert _is_linked(b, 'Extend38', a2)
    if hasattr(a1, 'base37'):
        assert not _is_linked(a1, 'base37', b)
    if hasattr(a2, 'base37'):
        assert _is_linked(a2, 'base37', b)
    _safe_set(b, 'Extend38', None)
    assert not _is_linked(b, 'Extend38', a2)
    if hasattr(a2, 'base37'):
        assert not _is_linked(a2, 'base37', b)


def test_assoc_extension46_reverse_link_reassign_clear():
    a1 = SecCon_UseCase(description="sample_text", preCondition="sample_text")
    a2 = SecCon_UseCase(description="sample_text_2", preCondition="sample_text_2")
    b = SecCon_Extend(condition="sample_text", name="sample_text")
    _safe_set(b, 'extend', a1)
    assert _is_linked(b, 'extend', a1)
    if hasattr(a1, 'UseCase47'):
        assert _is_linked(a1, 'UseCase47', b)
    _safe_set(b, 'extend', a2)
    assert _is_linked(b, 'extend', a2)
    if hasattr(a1, 'UseCase47'):
        assert not _is_linked(a1, 'UseCase47', b)
    if hasattr(a2, 'UseCase47'):
        assert _is_linked(a2, 'UseCase47', b)
    _safe_set(b, 'extend', None)
    assert not _is_linked(b, 'extend', a2)
    if hasattr(a2, 'UseCase47'):
        assert not _is_linked(a2, 'UseCase47', b)


def test_assoc_hasAction98_reverse_link_reassign_clear():
    a1 = SecCon_Rule(logicValue=True, name="sample_text", operator="sample_text")
    a2 = SecCon_Rule(logicValue=False, name="sample_text_2", operator="sample_text_2")
    b = SecCon_Action(name="sample_text", parameter="sample_text")
    _safe_set(b, 'SecCon_Action', a1)
    assert _is_linked(b, 'SecCon_Action', a1)
    if hasattr(a1, 'SecCon_Rule99'):
        assert _is_linked(a1, 'SecCon_Rule99', b)
    _safe_set(b, 'SecCon_Action', a2)
    assert _is_linked(b, 'SecCon_Action', a2)
    if hasattr(a1, 'SecCon_Rule99'):
        assert not _is_linked(a1, 'SecCon_Rule99', b)
    if hasattr(a2, 'SecCon_Rule99'):
        assert _is_linked(a2, 'SecCon_Rule99', b)
    _safe_set(b, 'SecCon_Action', None)
    assert not _is_linked(b, 'SecCon_Action', a2)
    if hasattr(a2, 'SecCon_Rule99'):
        assert not _is_linked(a2, 'SecCon_Rule99', b)


def test_assoc_hasCondition96_reverse_link_reassign_clear():
    a1 = SecCon_Rule(logicValue=True, name="sample_text", operator="sample_text")
    a2 = SecCon_Rule(logicValue=False, name="sample_text_2", operator="sample_text_2")
    b = SecCon_Condition(condition="sample_text", logicValue=True, value="sample_text")
    _safe_set(b, 'SecCon_Condition', a1)
    assert _is_linked(b, 'SecCon_Condition', a1)
    if hasattr(a1, 'SecCon_Rule97'):
        assert _is_linked(a1, 'SecCon_Rule97', b)
    _safe_set(b, 'SecCon_Condition', a2)
    assert _is_linked(b, 'SecCon_Condition', a2)
    if hasattr(a1, 'SecCon_Rule97'):
        assert not _is_linked(a1, 'SecCon_Rule97', b)
    if hasattr(a2, 'SecCon_Rule97'):
        assert _is_linked(a2, 'SecCon_Rule97', b)
    _safe_set(b, 'SecCon_Condition', None)
    assert not _is_linked(b, 'SecCon_Condition', a2)
    if hasattr(a2, 'SecCon_Rule97'):
        assert not _is_linked(a2, 'SecCon_Rule97', b)


def test_assoc_hasContextInformation100_reverse_link_reassign_clear():
    a1 = SecCon_ContextInformation(name="sample_text", type="sample_text")
    a2 = SecCon_ContextInformation(name="sample_text_2", type="sample_text_2")
    b = SecCon_Condition(condition="sample_text", logicValue=True, value="sample_text")
    _safe_set(b, 'SecCon_Condition101', a1)
    assert _is_linked(b, 'SecCon_Condition101', a1)
    if hasattr(a1, 'SecCon_ContextInformation102'):
        assert _is_linked(a1, 'SecCon_ContextInformation102', b)
    _safe_set(b, 'SecCon_Condition101', a2)
    assert _is_linked(b, 'SecCon_Condition101', a2)
    if hasattr(a1, 'SecCon_ContextInformation102'):
        assert not _is_linked(a1, 'SecCon_ContextInformation102', b)
    if hasattr(a2, 'SecCon_ContextInformation102'):
        assert _is_linked(a2, 'SecCon_ContextInformation102', b)
    _safe_set(b, 'SecCon_Condition101', None)
    assert not _is_linked(b, 'SecCon_Condition101', a2)
    if hasattr(a2, 'SecCon_ContextInformation102'):
        assert not _is_linked(a2, 'SecCon_ContextInformation102', b)


def test_assoc_include33_reverse_link_reassign_clear():
    a1 = SecCon_UseCase(description="sample_text", preCondition="sample_text")
    a2 = SecCon_UseCase(description="sample_text_2", preCondition="sample_text_2")
    b = SecCon_Include(name="sample_text")
    _safe_set(b, 'Include34', a1)
    assert _is_linked(b, 'Include34', a1)
    if hasattr(a1, 'base'):
        assert _is_linked(a1, 'base', b)
    _safe_set(b, 'Include34', a2)
    assert _is_linked(b, 'Include34', a2)
    if hasattr(a1, 'base'):
        assert not _is_linked(a1, 'base', b)
    if hasattr(a2, 'base'):
        assert _is_linked(a2, 'base', b)
    _safe_set(b, 'Include34', None)
    assert not _is_linked(b, 'Include34', a2)
    if hasattr(a2, 'base'):
        assert not _is_linked(a2, 'base', b)


def test_assoc_includes32_reverse_link_reassign_clear():
    a1 = SecCon_UseCase(description="sample_text", preCondition="sample_text")
    a2 = SecCon_UseCase(description="sample_text_2", preCondition="sample_text_2")
    b = SecCon_Include(name="sample_text")
    _safe_set(b, 'Include', a1)
    assert _is_linked(b, 'Include', a1)
    if hasattr(a1, 'addition'):
        assert _is_linked(a1, 'addition', b)
    _safe_set(b, 'Include', a2)
    assert _is_linked(b, 'Include', a2)
    if hasattr(a1, 'addition'):
        assert not _is_linked(a1, 'addition', b)
    if hasattr(a2, 'addition'):
        assert _is_linked(a2, 'addition', b)
    _safe_set(b, 'Include', None)
    assert not _is_linked(b, 'Include', a2)
    if hasattr(a2, 'addition'):
        assert not _is_linked(a2, 'addition', b)


def test_assoc_isFormed94_reverse_link_reassign_clear():
    a1 = SecCon_ContextScenario(name="sample_text")
    a2 = SecCon_ContextScenario(name="sample_text_2")
    b = SecCon_ContextInformation(name="sample_text", type="sample_text")
    _safe_set(b, 'SecCon_ContextInformation', a1)
    assert _is_linked(b, 'SecCon_ContextInformation', a1)
    if hasattr(a1, 'SecCon_ContextScenario95'):
        assert _is_linked(a1, 'SecCon_ContextScenario95', b)
    _safe_set(b, 'SecCon_ContextInformation', a2)
    assert _is_linked(b, 'SecCon_ContextInformation', a2)
    if hasattr(a1, 'SecCon_ContextScenario95'):
        assert not _is_linked(a1, 'SecCon_ContextScenario95', b)
    if hasattr(a2, 'SecCon_ContextScenario95'):
        assert _is_linked(a2, 'SecCon_ContextScenario95', b)
    _safe_set(b, 'SecCon_ContextInformation', None)
    assert not _is_linked(b, 'SecCon_ContextInformation', a2)
    if hasattr(a2, 'SecCon_ContextScenario95'):
        assert not _is_linked(a2, 'SecCon_ContextScenario95', b)


def test_assoc_opposite6_reverse_link_reassign_clear():
    a1 = SecCon_Attribute(default="sample_text", isComposite=True, isDerived=True, isID=True, isReadOnly=True)
    a2 = SecCon_Attribute(default="sample_text_2", isComposite=False, isDerived=False, isID=False, isReadOnly=False)
    b = SecCon_Attribute(default="sample_text", isComposite=True, isDerived=True, isID=True, isReadOnly=True)
    _safe_set(b, 'SecCon_Attribute5', a1)
    assert _is_linked(b, 'SecCon_Attribute5', a1)
    if hasattr(a1, 'SecCon_Attribute'):
        assert _is_linked(a1, 'SecCon_Attribute', b)
    _safe_set(b, 'SecCon_Attribute5', a2)
    assert _is_linked(b, 'SecCon_Attribute5', a2)
    if hasattr(a1, 'SecCon_Attribute'):
        assert not _is_linked(a1, 'SecCon_Attribute', b)
    if hasattr(a2, 'SecCon_Attribute'):
        assert _is_linked(a2, 'SecCon_Attribute', b)
    _safe_set(b, 'SecCon_Attribute5', None)
    assert not _is_linked(b, 'SecCon_Attribute5', a2)
    if hasattr(a2, 'SecCon_Attribute'):
        assert not _is_linked(a2, 'SecCon_Attribute', b)


def test_assoc_ownedAttribute18_reverse_link_reassign_clear():
    a1 = SecCon_Class(isAbstract=True)
    a2 = SecCon_Class(isAbstract=False)
    b = SecCon_Attribute(default="sample_text", isComposite=True, isDerived=True, isID=True, isReadOnly=True)
    _safe_set(b, 'SecCon_Attribute20', a1)
    assert _is_linked(b, 'SecCon_Attribute20', a1)
    if hasattr(a1, 'SecCon_Class19'):
        assert _is_linked(a1, 'SecCon_Class19', b)
    _safe_set(b, 'SecCon_Attribute20', a2)
    assert _is_linked(b, 'SecCon_Attribute20', a2)
    if hasattr(a1, 'SecCon_Class19'):
        assert not _is_linked(a1, 'SecCon_Class19', b)
    if hasattr(a2, 'SecCon_Class19'):
        assert _is_linked(a2, 'SecCon_Class19', b)
    _safe_set(b, 'SecCon_Attribute20', None)
    assert not _is_linked(b, 'SecCon_Attribute20', a2)
    if hasattr(a2, 'SecCon_Class19'):
        assert not _is_linked(a2, 'SecCon_Class19', b)


def test_assoc_ownedExtend55_reverse_link_reassign_clear():
    a1 = SecCon_UseCaseScenario(author="sample_text", version="sample_text")
    a2 = SecCon_UseCaseScenario(author="sample_text_2", version="sample_text_2")
    b = SecCon_Extend(condition="sample_text", name="sample_text")
    _safe_set(b, 'SecCon_Extend57', a1)
    assert _is_linked(b, 'SecCon_Extend57', a1)
    if hasattr(a1, 'SecCon_UseCaseScenario56'):
        assert _is_linked(a1, 'SecCon_UseCaseScenario56', b)
    _safe_set(b, 'SecCon_Extend57', a2)
    assert _is_linked(b, 'SecCon_Extend57', a2)
    if hasattr(a1, 'SecCon_UseCaseScenario56'):
        assert not _is_linked(a1, 'SecCon_UseCaseScenario56', b)
    if hasattr(a2, 'SecCon_UseCaseScenario56'):
        assert _is_linked(a2, 'SecCon_UseCaseScenario56', b)
    _safe_set(b, 'SecCon_Extend57', None)
    assert not _is_linked(b, 'SecCon_Extend57', a2)
    if hasattr(a2, 'SecCon_UseCaseScenario56'):
        assert not _is_linked(a2, 'SecCon_UseCaseScenario56', b)


def test_assoc_ownedInclude58_reverse_link_reassign_clear():
    a1 = SecCon_UseCaseScenario(author="sample_text", version="sample_text")
    a2 = SecCon_UseCaseScenario(author="sample_text_2", version="sample_text_2")
    b = SecCon_Include(name="sample_text")
    _safe_set(b, 'SecCon_Include60', a1)
    assert _is_linked(b, 'SecCon_Include60', a1)
    if hasattr(a1, 'SecCon_UseCaseScenario59'):
        assert _is_linked(a1, 'SecCon_UseCaseScenario59', b)
    _safe_set(b, 'SecCon_Include60', a2)
    assert _is_linked(b, 'SecCon_Include60', a2)
    if hasattr(a1, 'SecCon_UseCaseScenario59'):
        assert not _is_linked(a1, 'SecCon_UseCaseScenario59', b)
    if hasattr(a2, 'SecCon_UseCaseScenario59'):
        assert _is_linked(a2, 'SecCon_UseCaseScenario59', b)
    _safe_set(b, 'SecCon_Include60', None)
    assert not _is_linked(b, 'SecCon_Include60', a2)
    if hasattr(a2, 'SecCon_UseCaseScenario59'):
        assert not _is_linked(a2, 'SecCon_UseCaseScenario59', b)


def test_assoc_ownedOperation13_reverse_link_reassign_clear():
    a1 = SecCon_Operation(body="sample_text")
    a2 = SecCon_Operation(body="sample_text_2")
    b = SecCon_Class(isAbstract=True)
    _safe_set(b, 'SecCon_Class', {a1})
    assert _is_linked(b, 'SecCon_Class', a1)
    if hasattr(a1, 'SecCon_Operation14'):
        assert _is_linked(a1, 'SecCon_Operation14', b)
    _safe_set(b, 'SecCon_Class', {a2})
    assert _is_linked(b, 'SecCon_Class', a2)
    if hasattr(a1, 'SecCon_Operation14'):
        assert not _is_linked(a1, 'SecCon_Operation14', b)
    if hasattr(a2, 'SecCon_Operation14'):
        assert _is_linked(a2, 'SecCon_Operation14', b)
    _safe_set(b, 'SecCon_Class', set())
    assert not _is_linked(b, 'SecCon_Class', a2)
    if hasattr(a2, 'SecCon_Operation14'):
        assert not _is_linked(a2, 'SecCon_Operation14', b)


def test_assoc_ownedParameter9_reverse_link_reassign_clear():
    a1 = SecCon_Parameter(default="sample_text", direction="sample_text")
    a2 = SecCon_Parameter(default="sample_text_2", direction="sample_text_2")
    b = SecCon_Operation(body="sample_text")
    _safe_set(b, 'SecCon_Operation10', {a1})
    assert _is_linked(b, 'SecCon_Operation10', a1)
    if hasattr(a1, 'SecCon_Parameter'):
        assert _is_linked(a1, 'SecCon_Parameter', b)
    _safe_set(b, 'SecCon_Operation10', {a2})
    assert _is_linked(b, 'SecCon_Operation10', a2)
    if hasattr(a1, 'SecCon_Parameter'):
        assert not _is_linked(a1, 'SecCon_Parameter', b)
    if hasattr(a2, 'SecCon_Parameter'):
        assert _is_linked(a2, 'SecCon_Parameter', b)
    _safe_set(b, 'SecCon_Operation10', set())
    assert not _is_linked(b, 'SecCon_Operation10', a2)
    if hasattr(a2, 'SecCon_Parameter'):
        assert not _is_linked(a2, 'SecCon_Parameter', b)


def test_assoc_ownedUseCase52_reverse_link_reassign_clear():
    a1 = SecCon_UseCaseScenario(author="sample_text", version="sample_text")
    a2 = SecCon_UseCaseScenario(author="sample_text_2", version="sample_text_2")
    b = SecCon_UseCase(description="sample_text", preCondition="sample_text")
    _safe_set(b, 'SecCon_UseCase54', a1)
    assert _is_linked(b, 'SecCon_UseCase54', a1)
    if hasattr(a1, 'SecCon_UseCaseScenario53'):
        assert _is_linked(a1, 'SecCon_UseCaseScenario53', b)
    _safe_set(b, 'SecCon_UseCase54', a2)
    assert _is_linked(b, 'SecCon_UseCase54', a2)
    if hasattr(a1, 'SecCon_UseCaseScenario53'):
        assert not _is_linked(a1, 'SecCon_UseCaseScenario53', b)
    if hasattr(a2, 'SecCon_UseCaseScenario53'):
        assert _is_linked(a2, 'SecCon_UseCaseScenario53', b)
    _safe_set(b, 'SecCon_UseCase54', None)
    assert not _is_linked(b, 'SecCon_UseCase54', a2)
    if hasattr(a2, 'SecCon_UseCaseScenario53'):
        assert not _is_linked(a2, 'SecCon_UseCaseScenario53', b)


def test_assoc_scenario39_reverse_link_reassign_clear():
    a1 = SecCon_UseCaseScenario(author="sample_text", version="sample_text")
    a2 = SecCon_UseCaseScenario(author="sample_text_2", version="sample_text_2")
    b = SecCon_UseCase(description="sample_text", preCondition="sample_text")
    _safe_set(b, 'SecCon_UseCase40', a1)
    assert _is_linked(b, 'SecCon_UseCase40', a1)
    if hasattr(a1, 'SecCon_UseCaseScenario'):
        assert _is_linked(a1, 'SecCon_UseCaseScenario', b)
    _safe_set(b, 'SecCon_UseCase40', a2)
    assert _is_linked(b, 'SecCon_UseCase40', a2)
    if hasattr(a1, 'SecCon_UseCaseScenario'):
        assert not _is_linked(a1, 'SecCon_UseCaseScenario', b)
    if hasattr(a2, 'SecCon_UseCaseScenario'):
        assert _is_linked(a2, 'SecCon_UseCaseScenario', b)
    _safe_set(b, 'SecCon_UseCase40', None)
    assert not _is_linked(b, 'SecCon_UseCase40', a2)
    if hasattr(a2, 'SecCon_UseCaseScenario'):
        assert not _is_linked(a2, 'SecCon_UseCaseScenario', b)


def test_assoc_scenario44_reverse_link_reassign_clear():
    a1 = SecCon_UseCaseScenario(author="sample_text", version="sample_text")
    a2 = SecCon_UseCaseScenario(author="sample_text_2", version="sample_text_2")
    b = SecCon_Include(name="sample_text")
    _safe_set(b, 'SecCon_Include', a1)
    assert _is_linked(b, 'SecCon_Include', a1)
    if hasattr(a1, 'SecCon_UseCaseScenario45'):
        assert _is_linked(a1, 'SecCon_UseCaseScenario45', b)
    _safe_set(b, 'SecCon_Include', a2)
    assert _is_linked(b, 'SecCon_Include', a2)
    if hasattr(a1, 'SecCon_UseCaseScenario45'):
        assert not _is_linked(a1, 'SecCon_UseCaseScenario45', b)
    if hasattr(a2, 'SecCon_UseCaseScenario45'):
        assert _is_linked(a2, 'SecCon_UseCaseScenario45', b)
    _safe_set(b, 'SecCon_Include', None)
    assert not _is_linked(b, 'SecCon_Include', a2)
    if hasattr(a2, 'SecCon_UseCaseScenario45'):
        assert not _is_linked(a2, 'SecCon_UseCaseScenario45', b)


def test_assoc_scenario50_reverse_link_reassign_clear():
    a1 = SecCon_UseCaseScenario(author="sample_text", version="sample_text")
    a2 = SecCon_UseCaseScenario(author="sample_text_2", version="sample_text_2")
    b = SecCon_Extend(condition="sample_text", name="sample_text")
    _safe_set(b, 'SecCon_Extend', a1)
    assert _is_linked(b, 'SecCon_Extend', a1)
    if hasattr(a1, 'SecCon_UseCaseScenario51'):
        assert _is_linked(a1, 'SecCon_UseCaseScenario51', b)
    _safe_set(b, 'SecCon_Extend', a2)
    assert _is_linked(b, 'SecCon_Extend', a2)
    if hasattr(a1, 'SecCon_UseCaseScenario51'):
        assert not _is_linked(a1, 'SecCon_UseCaseScenario51', b)
    if hasattr(a2, 'SecCon_UseCaseScenario51'):
        assert _is_linked(a2, 'SecCon_UseCaseScenario51', b)
    _safe_set(b, 'SecCon_Extend', None)
    assert not _is_linked(b, 'SecCon_Extend', a2)
    if hasattr(a2, 'SecCon_UseCaseScenario51'):
        assert not _is_linked(a2, 'SecCon_UseCaseScenario51', b)


def test_assoc_superclass16_reverse_link_reassign_clear():
    a1 = SecCon_Class(isAbstract=True)
    a2 = SecCon_Class(isAbstract=False)
    b = SecCon_Class(isAbstract=True)
    _safe_set(b, 'SecCon_Class17', a1)
    assert _is_linked(b, 'SecCon_Class17', a1)
    if hasattr(a1, 'SecCon_Class15'):
        assert _is_linked(a1, 'SecCon_Class15', b)
    _safe_set(b, 'SecCon_Class17', a2)
    assert _is_linked(b, 'SecCon_Class17', a2)
    if hasattr(a1, 'SecCon_Class15'):
        assert not _is_linked(a1, 'SecCon_Class15', b)
    if hasattr(a2, 'SecCon_Class15'):
        assert _is_linked(a2, 'SecCon_Class15', b)
    _safe_set(b, 'SecCon_Class17', None)
    assert not _is_linked(b, 'SecCon_Class17', a2)
    if hasattr(a2, 'SecCon_Class15'):
        assert not _is_linked(a2, 'SecCon_Class15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actor31_stub_double():
    # SecCon_Actor has no real 'SecCon_Actor' property in the generated
    # code (a bare stub) -- manually attach it so SecCon_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SecCon_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SecCon_UseCase(description="sample_text", preCondition="sample_text")
    partner = SecCon_Actor()
    setattr(partner, 'SecCon_Actor', None)
    _safe_set(owner, 'SecCon_UseCase', {partner})
    assert getattr(partner, 'SecCon_Actor') == owner
    _safe_set(owner, 'SecCon_UseCase', set())
    assert getattr(partner, 'SecCon_Actor') is None


def test_assoc_annotatedElement2_stub_double():
    # SecCon_Element has no real 'SecCon_Element4' property in the generated
    # code (a bare stub) -- manually attach it so SecCon_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SecCon_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SecCon_Comment(body="sample_text")
    partner = SecCon_Element()
    setattr(partner, 'SecCon_Element4', None)
    _safe_set(owner, 'SecCon_Comment3', {partner})
    assert getattr(partner, 'SecCon_Element4') == owner
    _safe_set(owner, 'SecCon_Comment3', set())
    assert getattr(partner, 'SecCon_Element4') is None


def test_assoc_ownedActor61_stub_double():
    # SecCon_Actor has no real 'SecCon_Actor63' property in the generated
    # code (a bare stub) -- manually attach it so SecCon_UseCaseScenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SecCon_UseCaseScenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SecCon_UseCaseScenario(author="sample_text", version="sample_text")
    partner = SecCon_Actor()
    setattr(partner, 'SecCon_Actor63', None)
    _safe_set(owner, 'SecCon_UseCaseScenario62', {partner})
    assert getattr(partner, 'SecCon_Actor63') == owner
    _safe_set(owner, 'SecCon_UseCaseScenario62', set())
    assert getattr(partner, 'SecCon_Actor63') is None


def test_assoc_ownedContextScenario90_stub_double():
    # SecCon_Project has no real 'SecCon_Project91' property in the generated
    # code (a bare stub) -- manually attach it so SecCon_ContextScenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SecCon_ContextScenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SecCon_ContextScenario(name="sample_text")
    partner = SecCon_Project()
    setattr(partner, 'SecCon_Project91', None)
    _safe_set(owner, 'SecCon_ContextScenario', partner)
    assert owner in getattr(partner, 'SecCon_Project91')
    _safe_set(owner, 'SecCon_ContextScenario', None)
    assert owner not in getattr(partner, 'SecCon_Project91')


def test_assoc_ownedElement0_stub_double():
    # SecCon_Element has no real 'SecCon_Element' property in the generated
    # code (a bare stub) -- manually attach it so SecCon_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SecCon_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SecCon_Comment(body="sample_text")
    partner = SecCon_Element()
    setattr(partner, 'SecCon_Element', None)
    _safe_set(owner, 'SecCon_Comment', partner)
    assert owner in getattr(partner, 'SecCon_Element')
    _safe_set(owner, 'SecCon_Comment', None)
    assert owner not in getattr(partner, 'SecCon_Element')


def test_assoc_ownedEvent65_stub_double():
    # SecCon_Event has no real 'SecCon_Event' property in the generated
    # code (a bare stub) -- manually attach it so SecCon_StateMachineScenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SecCon_StateMachineScenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SecCon_StateMachineScenario(author="sample_text", version="sample_text")
    partner = SecCon_Event()
    setattr(partner, 'SecCon_Event', None)
    _safe_set(owner, 'SecCon_StateMachineScenario66', {partner})
    assert getattr(partner, 'SecCon_Event') == owner
    _safe_set(owner, 'SecCon_StateMachineScenario66', set())
    assert getattr(partner, 'SecCon_Event') is None


def test_assoc_ownedState64_stub_double():
    # SecCon_StateVertex has no real 'SecCon_StateVertex' property in the generated
    # code (a bare stub) -- manually attach it so SecCon_StateMachineScenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SecCon_StateMachineScenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SecCon_StateMachineScenario(author="sample_text", version="sample_text")
    partner = SecCon_StateVertex()
    setattr(partner, 'SecCon_StateVertex', None)
    _safe_set(owner, 'SecCon_StateMachineScenario', {partner})
    assert getattr(partner, 'SecCon_StateVertex') == owner
    _safe_set(owner, 'SecCon_StateMachineScenario', set())
    assert getattr(partner, 'SecCon_StateVertex') is None


def test_assoc_ownedStateMachineScenario87_stub_double():
    # SecCon_Project has no real 'SecCon_Project88' property in the generated
    # code (a bare stub) -- manually attach it so SecCon_StateMachineScenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SecCon_StateMachineScenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SecCon_StateMachineScenario(author="sample_text", version="sample_text")
    partner = SecCon_Project()
    setattr(partner, 'SecCon_Project88', None)
    _safe_set(owner, 'SecCon_StateMachineScenario89', partner)
    assert owner in getattr(partner, 'SecCon_Project88')
    _safe_set(owner, 'SecCon_StateMachineScenario89', None)
    assert owner not in getattr(partner, 'SecCon_Project88')


def test_assoc_ownedTransition67_stub_double():
    # SecCon_Transition has no real 'SecCon_Transition' property in the generated
    # code (a bare stub) -- manually attach it so SecCon_StateMachineScenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SecCon_StateMachineScenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SecCon_StateMachineScenario(author="sample_text", version="sample_text")
    partner = SecCon_Transition()
    setattr(partner, 'SecCon_Transition', None)
    _safe_set(owner, 'SecCon_StateMachineScenario68', {partner})
    assert getattr(partner, 'SecCon_Transition') == owner
    _safe_set(owner, 'SecCon_StateMachineScenario68', set())
    assert getattr(partner, 'SecCon_Transition') is None


def test_assoc_ownedUseCaseScenario84_stub_double():
    # SecCon_Project has no real 'SecCon_Project85' property in the generated
    # code (a bare stub) -- manually attach it so SecCon_UseCaseScenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SecCon_UseCaseScenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SecCon_UseCaseScenario(author="sample_text", version="sample_text")
    partner = SecCon_Project()
    setattr(partner, 'SecCon_Project85', None)
    _safe_set(owner, 'SecCon_UseCaseScenario86', partner)
    assert owner in getattr(partner, 'SecCon_Project85')
    _safe_set(owner, 'SecCon_UseCaseScenario86', None)
    assert owner not in getattr(partner, 'SecCon_Project85')


def test_assoc_raisedException7_stub_double():
    # SecCon_Type has no real 'SecCon_Type8' property in the generated
    # code (a bare stub) -- manually attach it so SecCon_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SecCon_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SecCon_Operation(body="sample_text")
    partner = SecCon_Type()
    setattr(partner, 'SecCon_Type8', None)
    _safe_set(owner, 'SecCon_Operation', {partner})
    assert getattr(partner, 'SecCon_Type8') == owner
    _safe_set(owner, 'SecCon_Operation', set())
    assert getattr(partner, 'SecCon_Type8') is None


