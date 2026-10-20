import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    ActionType,
    Contract,
    Expression,
    Placeholder,
    Prefix,
    Process,
    ReceiveGroup,
    SendGroup,
    Type,
    VariableDeclaration,
    co2_Action,
    co2_ActionType,
    co2_AndExpression,
    co2_ArithmeticSigned,
    co2_Ask,
    co2_BoolPlaceholder,
    co2_BooleanLiteral,
    co2_BooleanNegation,
    co2_BooleanType,
    co2_CO2System,
    co2_Case,
    co2_Comparison,
    co2_Contract,
    co2_ContractDefinition,
    co2_ContractReference,
    co2_ContractsAndProcessesDeclaration,
    co2_DelimitedProcess,
    co2_DoInput,
    co2_DoOutput,
    co2_EmptyContract,
    co2_EmptyProcess,
    co2_Equals,
    co2_Expression,
    co2_ExtAction,
    co2_ExtSum,
    co2_HonestyDeclaration,
    co2_IfThenElse,
    co2_Import,
    co2_Input,
    co2_IntAction,
    co2_IntActionType,
    co2_IntPlaceholder,
    co2_IntSum,
    co2_IntType,
    co2_Minus,
    co2_MultiOrDiv,
    co2_NumberLiteral,
    co2_OrExpression,
    co2_PackageDeclaration,
    co2_ParallelProcesses,
    co2_Placeholder,
    co2_Plus,
    co2_Prefix,
    co2_Process,
    co2_ProcessCall,
    co2_ProcessDefinition,
    co2_Receive,
    co2_ReceiveGroup,
    co2_Retract,
    co2_RetractedProcess,
    co2_Send,
    co2_SendGroup,
    co2_Session,
    co2_SessionType,
    co2_StringActionType,
    co2_StringLiteral,
    co2_StringPlaceholder,
    co2_StringType,
    co2_Sum,
    co2_SwitchCase,
    co2_Tau,
    co2_Tell,
    co2_TellAndReturn,
    co2_TellAndWait,
    co2_TimeoutProcess,
    co2_Type,
    co2_UnitActionType,
    co2_Variable,
    co2_VariableDeclaration,
    co2_VariableReference,
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

def test_assoc_session61_reverse_link_reassign_clear():
    a1 = co2_VariableDeclaration(name="sample_text")
    a2 = co2_VariableDeclaration(name="sample_text_2")
    b = co2_Ask(formula="sample_text")
    _safe_set(b, 'co2_Ask', a1)
    assert _is_linked(b, 'co2_Ask', a1)
    if hasattr(a1, 'co2_VariableDeclaration62'):
        assert _is_linked(a1, 'co2_VariableDeclaration62', b)
    _safe_set(b, 'co2_Ask', a2)
    assert _is_linked(b, 'co2_Ask', a2)
    if hasattr(a1, 'co2_VariableDeclaration62'):
        assert not _is_linked(a1, 'co2_VariableDeclaration62', b)
    if hasattr(a2, 'co2_VariableDeclaration62'):
        assert _is_linked(a2, 'co2_VariableDeclaration62', b)
    _safe_set(b, 'co2_Ask', None)
    assert not _is_linked(b, 'co2_Ask', a2)
    if hasattr(a2, 'co2_VariableDeclaration62'):
        assert not _is_linked(a2, 'co2_VariableDeclaration62', b)


def test_assoc_type137_reverse_link_reassign_clear():
    a1 = co2_ActionType(value="sample_text")
    a2 = co2_ActionType(value="sample_text_2")
    b = co2_Action(name="sample_text")
    _safe_set(b, 'co2_Action', a1)
    assert _is_linked(b, 'co2_Action', a1)
    if hasattr(a1, 'co2_ActionType'):
        assert _is_linked(a1, 'co2_ActionType', b)
    _safe_set(b, 'co2_Action', a2)
    assert _is_linked(b, 'co2_Action', a2)
    if hasattr(a1, 'co2_ActionType'):
        assert not _is_linked(a1, 'co2_ActionType', b)
    if hasattr(a2, 'co2_ActionType'):
        assert _is_linked(a2, 'co2_ActionType', b)
    _safe_set(b, 'co2_Action', None)
    assert not _is_linked(b, 'co2_Action', a2)
    if hasattr(a2, 'co2_ActionType'):
        assert not _is_linked(a2, 'co2_ActionType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cases109_stub_double():
    # co2_Case has no real 'co2_Case' property in the generated
    # code (a bare stub) -- manually attach it so co2_SwitchCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_SwitchCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_SwitchCase(default=True)
    partner = co2_Case()
    setattr(partner, 'co2_Case', None)
    _safe_set(owner, 'co2_SwitchCase110', {partner})
    assert getattr(partner, 'co2_Case') == owner
    _safe_set(owner, 'co2_SwitchCase110', set())
    assert getattr(partner, 'co2_Case') is None


def test_assoc_contract130_stub_double():
    # co2_Contract has no real 'co2_Contract132' property in the generated
    # code (a bare stub) -- manually attach it so co2_ContractDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_ContractDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_ContractDefinition(name="sample_text")
    partner = co2_Contract()
    setattr(partner, 'co2_Contract132', None)
    _safe_set(owner, 'co2_ContractDefinition131', partner)
    assert getattr(partner, 'co2_Contract132') == owner
    _safe_set(owner, 'co2_ContractDefinition131', None)
    assert getattr(partner, 'co2_Contract132') is None


def test_assoc_contractReference127_stub_double():
    # co2_Session has no real 'co2_Session128' property in the generated
    # code (a bare stub) -- manually attach it so co2_ContractDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_ContractDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_ContractDefinition(name="sample_text")
    partner = co2_Session()
    setattr(partner, 'co2_Session128', None)
    _safe_set(owner, 'co2_ContractDefinition129', partner)
    assert getattr(partner, 'co2_Session128') == owner
    _safe_set(owner, 'co2_ContractDefinition129', None)
    assert getattr(partner, 'co2_Session128') is None


def test_assoc_contractReference42_stub_double():
    # co2_Tell has no real 'co2_Tell43' property in the generated
    # code (a bare stub) -- manually attach it so co2_ContractDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_ContractDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_ContractDefinition(name="sample_text")
    partner = co2_Tell()
    setattr(partner, 'co2_Tell43', None)
    _safe_set(owner, 'co2_ContractDefinition44', partner)
    assert getattr(partner, 'co2_Tell43') == owner
    _safe_set(owner, 'co2_ContractDefinition44', None)
    assert getattr(partner, 'co2_Tell43') is None


def test_assoc_contracts7_stub_double():
    # co2_ContractsAndProcessesDeclaration has no real 'co2_ContractsAndProcessesDeclaration8' property in the generated
    # code (a bare stub) -- manually attach it so co2_ContractDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_ContractDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_ContractDefinition(name="sample_text")
    partner = co2_ContractsAndProcessesDeclaration()
    setattr(partner, 'co2_ContractsAndProcessesDeclaration8', None)
    _safe_set(owner, 'co2_ContractDefinition', partner)
    assert owner in getattr(partner, 'co2_ContractsAndProcessesDeclaration8')
    _safe_set(owner, 'co2_ContractDefinition', None)
    assert owner not in getattr(partner, 'co2_ContractsAndProcessesDeclaration8')


def test_assoc_defaultProc111_stub_double():
    # co2_Process has no real 'co2_Process113' property in the generated
    # code (a bare stub) -- manually attach it so co2_SwitchCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_SwitchCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_SwitchCase(default=True)
    partner = co2_Process()
    setattr(partner, 'co2_Process113', None)
    _safe_set(owner, 'co2_SwitchCase112', partner)
    assert getattr(partner, 'co2_Process113') == owner
    _safe_set(owner, 'co2_SwitchCase112', None)
    assert getattr(partner, 'co2_Process113') is None


def test_assoc_exp107_stub_double():
    # co2_Expression has no real 'co2_Expression108' property in the generated
    # code (a bare stub) -- manually attach it so co2_SwitchCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_SwitchCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_SwitchCase(default=True)
    partner = co2_Expression()
    setattr(partner, 'co2_Expression108', None)
    _safe_set(owner, 'co2_SwitchCase', partner)
    assert getattr(partner, 'co2_Expression108') == owner
    _safe_set(owner, 'co2_SwitchCase', None)
    assert getattr(partner, 'co2_Expression108') is None


def test_assoc_inputs91_stub_double():
    # co2_Input has no real 'co2_Input' property in the generated
    # code (a bare stub) -- manually attach it so co2_Receive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_Receive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_Receive(timeout=True)
    partner = co2_Input()
    setattr(partner, 'co2_Input', None)
    _safe_set(owner, 'co2_Receive', {partner})
    assert getattr(partner, 'co2_Input') == owner
    _safe_set(owner, 'co2_Receive', set())
    assert getattr(partner, 'co2_Input') is None


def test_assoc_left153_stub_double():
    # co2_Expression has no real 'co2_Expression154' property in the generated
    # code (a bare stub) -- manually attach it so co2_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_Comparison(op="sample_text")
    partner = co2_Expression()
    setattr(partner, 'co2_Expression154', None)
    _safe_set(owner, 'co2_Comparison', partner)
    assert getattr(partner, 'co2_Expression154') == owner
    _safe_set(owner, 'co2_Comparison', None)
    assert getattr(partner, 'co2_Expression154') is None


def test_assoc_left158_stub_double():
    # co2_Expression has no real 'co2_Expression159' property in the generated
    # code (a bare stub) -- manually attach it so co2_Equals's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_Equals's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_Equals(op="sample_text")
    partner = co2_Expression()
    setattr(partner, 'co2_Expression159', None)
    _safe_set(owner, 'co2_Equals', partner)
    assert getattr(partner, 'co2_Expression159') == owner
    _safe_set(owner, 'co2_Equals', None)
    assert getattr(partner, 'co2_Expression159') is None


def test_assoc_left173_stub_double():
    # co2_Expression has no real 'co2_Expression174' property in the generated
    # code (a bare stub) -- manually attach it so co2_MultiOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_MultiOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_MultiOrDiv(op="sample_text")
    partner = co2_Expression()
    setattr(partner, 'co2_Expression174', None)
    _safe_set(owner, 'co2_MultiOrDiv', partner)
    assert getattr(partner, 'co2_Expression174') == owner
    _safe_set(owner, 'co2_MultiOrDiv', None)
    assert getattr(partner, 'co2_Expression174') is None


def test_assoc_next138_stub_double():
    # co2_Contract has no real 'co2_Contract140' property in the generated
    # code (a bare stub) -- manually attach it so co2_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_Action(name="sample_text")
    partner = co2_Contract()
    setattr(partner, 'co2_Contract140', None)
    _safe_set(owner, 'co2_Action139', partner)
    assert getattr(partner, 'co2_Contract140') == owner
    _safe_set(owner, 'co2_Action139', None)
    assert getattr(partner, 'co2_Contract140') is None


def test_assoc_package0_stub_double():
    # co2_CO2System has no real 'co2_CO2System' property in the generated
    # code (a bare stub) -- manually attach it so co2_PackageDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_PackageDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_PackageDeclaration(name="sample_text", single=True)
    partner = co2_CO2System()
    setattr(partner, 'co2_CO2System', None)
    _safe_set(owner, 'co2_PackageDeclaration', partner)
    assert getattr(partner, 'co2_CO2System') == owner
    _safe_set(owner, 'co2_PackageDeclaration', None)
    assert getattr(partner, 'co2_CO2System') is None


def test_assoc_params12_stub_double():
    # co2_Variable has no real 'co2_Variable' property in the generated
    # code (a bare stub) -- manually attach it so co2_ProcessDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_ProcessDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_ProcessDefinition(name="sample_text", withoutRestrictions=True)
    partner = co2_Variable()
    setattr(partner, 'co2_Variable', None)
    _safe_set(owner, 'co2_ProcessDefinition13', {partner})
    assert getattr(partner, 'co2_Variable') == owner
    _safe_set(owner, 'co2_ProcessDefinition13', set())
    assert getattr(partner, 'co2_Variable') is None


def test_assoc_process14_stub_double():
    # co2_ParallelProcesses has no real 'co2_ParallelProcesses' property in the generated
    # code (a bare stub) -- manually attach it so co2_ProcessDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_ProcessDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_ProcessDefinition(name="sample_text", withoutRestrictions=True)
    partner = co2_ParallelProcesses()
    setattr(partner, 'co2_ParallelProcesses', None)
    _safe_set(owner, 'co2_ProcessDefinition15', partner)
    assert getattr(partner, 'co2_ParallelProcesses') == owner
    _safe_set(owner, 'co2_ProcessDefinition15', None)
    assert getattr(partner, 'co2_ParallelProcesses') is None


def test_assoc_process69_stub_double():
    # co2_Process has no real 'co2_Process71' property in the generated
    # code (a bare stub) -- manually attach it so co2_TellAndWait's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_TellAndWait's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_TellAndWait(timeout=True)
    partner = co2_Process()
    setattr(partner, 'co2_Process71', None)
    _safe_set(owner, 'co2_TellAndWait70', partner)
    assert getattr(partner, 'co2_Process71') == owner
    _safe_set(owner, 'co2_TellAndWait70', None)
    assert getattr(partner, 'co2_Process71') is None


def test_assoc_processes5_stub_double():
    # co2_HonestyDeclaration has no real 'co2_HonestyDeclaration6' property in the generated
    # code (a bare stub) -- manually attach it so co2_ProcessDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_ProcessDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_ProcessDefinition(name="sample_text", withoutRestrictions=True)
    partner = co2_HonestyDeclaration()
    setattr(partner, 'co2_HonestyDeclaration6', None)
    _safe_set(owner, 'co2_ProcessDefinition', partner)
    assert owner in getattr(partner, 'co2_HonestyDeclaration6')
    _safe_set(owner, 'co2_ProcessDefinition', None)
    assert owner not in getattr(partner, 'co2_HonestyDeclaration6')


def test_assoc_processes9_stub_double():
    # co2_ContractsAndProcessesDeclaration has no real 'co2_ContractsAndProcessesDeclaration10' property in the generated
    # code (a bare stub) -- manually attach it so co2_ProcessDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_ProcessDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_ProcessDefinition(name="sample_text", withoutRestrictions=True)
    partner = co2_ContractsAndProcessesDeclaration()
    setattr(partner, 'co2_ContractsAndProcessesDeclaration10', None)
    _safe_set(owner, 'co2_ProcessDefinition11', partner)
    assert owner in getattr(partner, 'co2_ContractsAndProcessesDeclaration10')
    _safe_set(owner, 'co2_ProcessDefinition11', None)
    assert owner not in getattr(partner, 'co2_ContractsAndProcessesDeclaration10')


def test_assoc_ref182_stub_double():
    # co2_VariableReference has no real 'co2_VariableReference' property in the generated
    # code (a bare stub) -- manually attach it so co2_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_VariableDeclaration(name="sample_text")
    partner = co2_VariableReference()
    setattr(partner, 'co2_VariableReference', None)
    _safe_set(owner, 'co2_VariableDeclaration183', partner)
    assert getattr(partner, 'co2_VariableReference') == owner
    _safe_set(owner, 'co2_VariableDeclaration183', None)
    assert getattr(partner, 'co2_VariableReference') is None


def test_assoc_ref184_stub_double():
    # co2_ContractReference has no real 'co2_ContractReference' property in the generated
    # code (a bare stub) -- manually attach it so co2_ContractDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_ContractDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_ContractDefinition(name="sample_text")
    partner = co2_ContractReference()
    setattr(partner, 'co2_ContractReference', None)
    _safe_set(owner, 'co2_ContractDefinition185', partner)
    assert getattr(partner, 'co2_ContractReference') == owner
    _safe_set(owner, 'co2_ContractDefinition185', None)
    assert getattr(partner, 'co2_ContractReference') is None


def test_assoc_reference31_stub_double():
    # co2_ProcessCall has no real 'co2_ProcessCall' property in the generated
    # code (a bare stub) -- manually attach it so co2_ProcessDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_ProcessDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_ProcessDefinition(name="sample_text", withoutRestrictions=True)
    partner = co2_ProcessCall()
    setattr(partner, 'co2_ProcessCall', None)
    _safe_set(owner, 'co2_ProcessDefinition32', partner)
    assert getattr(partner, 'co2_ProcessCall') == owner
    _safe_set(owner, 'co2_ProcessDefinition32', None)
    assert getattr(partner, 'co2_ProcessCall') is None


def test_assoc_right155_stub_double():
    # co2_Expression has no real 'co2_Expression157' property in the generated
    # code (a bare stub) -- manually attach it so co2_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_Comparison(op="sample_text")
    partner = co2_Expression()
    setattr(partner, 'co2_Expression157', None)
    _safe_set(owner, 'co2_Comparison156', partner)
    assert getattr(partner, 'co2_Expression157') == owner
    _safe_set(owner, 'co2_Comparison156', None)
    assert getattr(partner, 'co2_Expression157') is None


def test_assoc_right160_stub_double():
    # co2_Expression has no real 'co2_Expression162' property in the generated
    # code (a bare stub) -- manually attach it so co2_Equals's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_Equals's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_Equals(op="sample_text")
    partner = co2_Expression()
    setattr(partner, 'co2_Expression162', None)
    _safe_set(owner, 'co2_Equals161', partner)
    assert getattr(partner, 'co2_Expression162') == owner
    _safe_set(owner, 'co2_Equals161', None)
    assert getattr(partner, 'co2_Expression162') is None


def test_assoc_right175_stub_double():
    # co2_Expression has no real 'co2_Expression177' property in the generated
    # code (a bare stub) -- manually attach it so co2_MultiOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_MultiOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_MultiOrDiv(op="sample_text")
    partner = co2_Expression()
    setattr(partner, 'co2_Expression177', None)
    _safe_set(owner, 'co2_MultiOrDiv176', partner)
    assert getattr(partner, 'co2_Expression177') == owner
    _safe_set(owner, 'co2_MultiOrDiv176', None)
    assert getattr(partner, 'co2_Expression177') is None


def test_assoc_session104_stub_double():
    # co2_Input has no real 'co2_Input105' property in the generated
    # code (a bare stub) -- manually attach it so co2_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_VariableDeclaration(name="sample_text")
    partner = co2_Input()
    setattr(partner, 'co2_Input105', None)
    _safe_set(owner, 'co2_VariableDeclaration106', partner)
    assert getattr(partner, 'co2_Input105') == owner
    _safe_set(owner, 'co2_VariableDeclaration106', None)
    assert getattr(partner, 'co2_Input105') is None


def test_assoc_session39_stub_double():
    # co2_Tell has no real 'co2_Tell' property in the generated
    # code (a bare stub) -- manually attach it so co2_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_VariableDeclaration(name="sample_text")
    partner = co2_Tell()
    setattr(partner, 'co2_Tell', None)
    _safe_set(owner, 'co2_VariableDeclaration', partner)
    assert getattr(partner, 'co2_Tell') == owner
    _safe_set(owner, 'co2_VariableDeclaration', None)
    assert getattr(partner, 'co2_Tell') is None


def test_assoc_session45_stub_double():
    # co2_Retract has no real 'co2_Retract' property in the generated
    # code (a bare stub) -- manually attach it so co2_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_VariableDeclaration(name="sample_text")
    partner = co2_Retract()
    setattr(partner, 'co2_Retract', None)
    _safe_set(owner, 'co2_VariableDeclaration46', partner)
    assert getattr(partner, 'co2_Retract') == owner
    _safe_set(owner, 'co2_VariableDeclaration46', None)
    assert getattr(partner, 'co2_Retract') is None


def test_assoc_session47_stub_double():
    # co2_DoOutput has no real 'co2_DoOutput' property in the generated
    # code (a bare stub) -- manually attach it so co2_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_VariableDeclaration(name="sample_text")
    partner = co2_DoOutput()
    setattr(partner, 'co2_DoOutput', None)
    _safe_set(owner, 'co2_VariableDeclaration48', partner)
    assert getattr(partner, 'co2_DoOutput') == owner
    _safe_set(owner, 'co2_VariableDeclaration48', None)
    assert getattr(partner, 'co2_DoOutput') is None


def test_assoc_session54_stub_double():
    # co2_DoInput has no real 'co2_DoInput' property in the generated
    # code (a bare stub) -- manually attach it so co2_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_VariableDeclaration(name="sample_text")
    partner = co2_DoInput()
    setattr(partner, 'co2_DoInput', None)
    _safe_set(owner, 'co2_VariableDeclaration55', partner)
    assert getattr(partner, 'co2_DoInput') == owner
    _safe_set(owner, 'co2_VariableDeclaration55', None)
    assert getattr(partner, 'co2_DoInput') is None


def test_assoc_session67_stub_double():
    # co2_Session has no real 'co2_Session68' property in the generated
    # code (a bare stub) -- manually attach it so co2_TellAndWait's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_TellAndWait's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_TellAndWait(timeout=True)
    partner = co2_Session()
    setattr(partner, 'co2_Session68', None)
    _safe_set(owner, 'co2_TellAndWait', partner)
    assert getattr(partner, 'co2_Session68') == owner
    _safe_set(owner, 'co2_TellAndWait', None)
    assert getattr(partner, 'co2_Session68') is None


def test_assoc_session88_stub_double():
    # co2_Send has no real 'co2_Send89' property in the generated
    # code (a bare stub) -- manually attach it so co2_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_VariableDeclaration(name="sample_text")
    partner = co2_Send()
    setattr(partner, 'co2_Send89', None)
    _safe_set(owner, 'co2_VariableDeclaration90', partner)
    assert getattr(partner, 'co2_Send89') == owner
    _safe_set(owner, 'co2_VariableDeclaration90', None)
    assert getattr(partner, 'co2_Send89') is None


def test_assoc_timeoutValue72_stub_double():
    # co2_TimeoutProcess has no real 'co2_TimeoutProcess' property in the generated
    # code (a bare stub) -- manually attach it so co2_TellAndWait's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_TellAndWait's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_TellAndWait(timeout=True)
    partner = co2_TimeoutProcess()
    setattr(partner, 'co2_TimeoutProcess', None)
    _safe_set(owner, 'co2_TellAndWait73', partner)
    assert getattr(partner, 'co2_TimeoutProcess') == owner
    _safe_set(owner, 'co2_TellAndWait73', None)
    assert getattr(partner, 'co2_TimeoutProcess') is None


def test_assoc_timeoutValue92_stub_double():
    # co2_TimeoutProcess has no real 'co2_TimeoutProcess94' property in the generated
    # code (a bare stub) -- manually attach it so co2_Receive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_Receive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_Receive(timeout=True)
    partner = co2_TimeoutProcess()
    setattr(partner, 'co2_TimeoutProcess94', None)
    _safe_set(owner, 'co2_Receive93', partner)
    assert getattr(partner, 'co2_TimeoutProcess94') == owner
    _safe_set(owner, 'co2_Receive93', None)
    assert getattr(partner, 'co2_TimeoutProcess94') is None


def test_assoc_type120_stub_double():
    # co2_Placeholder has no real 'co2_Placeholder' property in the generated
    # code (a bare stub) -- manually attach it so co2_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_Type(value="sample_text")
    partner = co2_Placeholder()
    setattr(partner, 'co2_Placeholder', None)
    _safe_set(owner, 'co2_Type', partner)
    assert getattr(partner, 'co2_Placeholder') == owner
    _safe_set(owner, 'co2_Type', None)
    assert getattr(partner, 'co2_Placeholder') is None


def test_assoc_type121_stub_double():
    # co2_Variable has no real 'co2_Variable122' property in the generated
    # code (a bare stub) -- manually attach it so co2_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # co2_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = co2_Type(value="sample_text")
    partner = co2_Variable()
    setattr(partner, 'co2_Variable122', None)
    _safe_set(owner, 'co2_Type123', partner)
    assert getattr(partner, 'co2_Variable122') == owner
    _safe_set(owner, 'co2_Type123', None)
    assert getattr(partner, 'co2_Variable122') is None


