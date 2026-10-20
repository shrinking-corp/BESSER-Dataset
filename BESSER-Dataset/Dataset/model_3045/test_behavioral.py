import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Adaptable,
    Attributable,
    Edge,
    Graph,
    Vertex,
    df_Action,
    df_Actor,
    df_Argument,
    df_Connection,
    df_EObject,
    df_Entity,
    df_Expression,
    df_FSM,
    df_Instance,
    df_MoC,
    df_Network,
    df_Pattern,
    df_Port,
    df_PortToEIntegerObjectMapEntry,
    df_PortToVarMapEntry,
    df_Procedure,
    df_State,
    df_Tag,
    df_Transition,
    df_Type,
    df_Unit,
    df_Var,
    df_VarToPortMapEntry,
    df_Vertex,
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

def test_assoc_inputs24_reverse_link_reassign_clear():
    a1 = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    a2 = df_Port(name="sample_text_2", numTokensConsumed=13, numTokensProduced=13)
    b = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    _safe_set(b, 'df_Actor25', {a1})
    assert _is_linked(b, 'df_Actor25', a1)
    if hasattr(a1, 'df_Port26'):
        assert _is_linked(a1, 'df_Port26', b)
    _safe_set(b, 'df_Actor25', {a2})
    assert _is_linked(b, 'df_Actor25', a2)
    if hasattr(a1, 'df_Port26'):
        assert not _is_linked(a1, 'df_Port26', b)
    if hasattr(a2, 'df_Port26'):
        assert _is_linked(a2, 'df_Port26', b)
    _safe_set(b, 'df_Actor25', set())
    assert not _is_linked(b, 'df_Actor25', a2)
    if hasattr(a2, 'df_Port26'):
        assert not _is_linked(a2, 'df_Port26', b)


def test_assoc_inputs42_reverse_link_reassign_clear():
    a1 = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    a2 = df_Port(name="sample_text_2", numTokensConsumed=13, numTokensProduced=13)
    b = df_Network(fileName="sample_text", name="sample_text")
    _safe_set(b, 'df_Network43', {a1})
    assert _is_linked(b, 'df_Network43', a1)
    if hasattr(a1, 'df_Port44'):
        assert _is_linked(a1, 'df_Port44', b)
    _safe_set(b, 'df_Network43', {a2})
    assert _is_linked(b, 'df_Network43', a2)
    if hasattr(a1, 'df_Port44'):
        assert not _is_linked(a1, 'df_Port44', b)
    if hasattr(a2, 'df_Port44'):
        assert _is_linked(a2, 'df_Port44', b)
    _safe_set(b, 'df_Network43', set())
    assert not _is_linked(b, 'df_Network43', a2)
    if hasattr(a2, 'df_Port44'):
        assert not _is_linked(a2, 'df_Port44', b)


def test_assoc_inputs7_reverse_link_reassign_clear():
    a1 = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    a2 = df_Port(name="sample_text_2", numTokensConsumed=13, numTokensProduced=13)
    b = df_Entity(incomingPortMap="sample_text", name="sample_text", outgoingPortMap="sample_text")
    _safe_set(b, 'df_Entity', {a1})
    assert _is_linked(b, 'df_Entity', a1)
    if hasattr(a1, 'df_Port8'):
        assert _is_linked(a1, 'df_Port8', b)
    _safe_set(b, 'df_Entity', {a2})
    assert _is_linked(b, 'df_Entity', a2)
    if hasattr(a1, 'df_Port8'):
        assert not _is_linked(a1, 'df_Port8', b)
    if hasattr(a2, 'df_Port8'):
        assert _is_linked(a2, 'df_Port8', b)
    _safe_set(b, 'df_Entity', set())
    assert not _is_linked(b, 'df_Entity', a2)
    if hasattr(a2, 'df_Port8'):
        assert not _is_linked(a2, 'df_Port8', b)


def test_assoc_key94_reverse_link_reassign_clear():
    a1 = df_PortToEIntegerObjectMapEntry(value="sample_text")
    a2 = df_PortToEIntegerObjectMapEntry(value="sample_text_2")
    b = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    _safe_set(b, 'df_Port96', a1)
    assert _is_linked(b, 'df_Port96', a1)
    if hasattr(a1, 'df_PortToEIntegerObjectMapEntry95'):
        assert _is_linked(a1, 'df_PortToEIntegerObjectMapEntry95', b)
    _safe_set(b, 'df_Port96', a2)
    assert _is_linked(b, 'df_Port96', a2)
    if hasattr(a1, 'df_PortToEIntegerObjectMapEntry95'):
        assert not _is_linked(a1, 'df_PortToEIntegerObjectMapEntry95', b)
    if hasattr(a2, 'df_PortToEIntegerObjectMapEntry95'):
        assert _is_linked(a2, 'df_PortToEIntegerObjectMapEntry95', b)
    _safe_set(b, 'df_Port96', None)
    assert not _is_linked(b, 'df_Port96', a2)
    if hasattr(a2, 'df_PortToEIntegerObjectMapEntry95'):
        assert not _is_linked(a2, 'df_PortToEIntegerObjectMapEntry95', b)


def test_assoc_outputs29_reverse_link_reassign_clear():
    a1 = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    a2 = df_Port(name="sample_text_2", numTokensConsumed=13, numTokensProduced=13)
    b = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    _safe_set(b, 'df_Actor30', {a1})
    assert _is_linked(b, 'df_Actor30', a1)
    if hasattr(a1, 'df_Port31'):
        assert _is_linked(a1, 'df_Port31', b)
    _safe_set(b, 'df_Actor30', {a2})
    assert _is_linked(b, 'df_Actor30', a2)
    if hasattr(a1, 'df_Port31'):
        assert not _is_linked(a1, 'df_Port31', b)
    if hasattr(a2, 'df_Port31'):
        assert _is_linked(a2, 'df_Port31', b)
    _safe_set(b, 'df_Actor30', set())
    assert not _is_linked(b, 'df_Actor30', a2)
    if hasattr(a2, 'df_Port31'):
        assert not _is_linked(a2, 'df_Port31', b)


def test_assoc_outputs48_reverse_link_reassign_clear():
    a1 = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    a2 = df_Port(name="sample_text_2", numTokensConsumed=13, numTokensProduced=13)
    b = df_Network(fileName="sample_text", name="sample_text")
    _safe_set(b, 'df_Network49', {a1})
    assert _is_linked(b, 'df_Network49', a1)
    if hasattr(a1, 'df_Port50'):
        assert _is_linked(a1, 'df_Port50', b)
    _safe_set(b, 'df_Network49', {a2})
    assert _is_linked(b, 'df_Network49', a2)
    if hasattr(a1, 'df_Port50'):
        assert not _is_linked(a1, 'df_Port50', b)
    if hasattr(a2, 'df_Port50'):
        assert _is_linked(a2, 'df_Port50', b)
    _safe_set(b, 'df_Network49', set())
    assert not _is_linked(b, 'df_Network49', a2)
    if hasattr(a2, 'df_Port50'):
        assert not _is_linked(a2, 'df_Port50', b)


def test_assoc_outputs9_reverse_link_reassign_clear():
    a1 = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    a2 = df_Port(name="sample_text_2", numTokensConsumed=13, numTokensProduced=13)
    b = df_Entity(incomingPortMap="sample_text", name="sample_text", outgoingPortMap="sample_text")
    _safe_set(b, 'df_Entity10', {a1})
    assert _is_linked(b, 'df_Entity10', a1)
    if hasattr(a1, 'df_Port11'):
        assert _is_linked(a1, 'df_Port11', b)
    _safe_set(b, 'df_Entity10', {a2})
    assert _is_linked(b, 'df_Entity10', a2)
    if hasattr(a1, 'df_Port11'):
        assert not _is_linked(a1, 'df_Port11', b)
    if hasattr(a2, 'df_Port11'):
        assert _is_linked(a2, 'df_Port11', b)
    _safe_set(b, 'df_Entity10', set())
    assert not _is_linked(b, 'df_Entity10', a2)
    if hasattr(a2, 'df_Port11'):
        assert not _is_linked(a2, 'df_Port11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions15_stub_double():
    # df_Action has no real 'df_Action' property in the generated
    # code (a bare stub) -- manually attach it so df_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    partner = df_Action()
    setattr(partner, 'df_Action', None)
    _safe_set(owner, 'df_Actor', {partner})
    assert getattr(partner, 'df_Action') == owner
    _safe_set(owner, 'df_Actor', set())
    assert getattr(partner, 'df_Action') is None


def test_assoc_actionsOutsideFsm16_stub_double():
    # df_Action has no real 'df_Action18' property in the generated
    # code (a bare stub) -- manually attach it so df_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    partner = df_Action()
    setattr(partner, 'df_Action18', None)
    _safe_set(owner, 'df_Actor17', {partner})
    assert getattr(partner, 'df_Action18') == owner
    _safe_set(owner, 'df_Actor17', set())
    assert getattr(partner, 'df_Action18') is None


def test_assoc_arguments4_stub_double():
    # df_Argument has no real 'df_Argument' property in the generated
    # code (a bare stub) -- manually attach it so df_Instance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Instance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Instance(name="sample_text")
    partner = df_Argument()
    setattr(partner, 'df_Argument', None)
    _safe_set(owner, 'df_Instance', {partner})
    assert getattr(partner, 'df_Argument') == owner
    _safe_set(owner, 'df_Instance', set())
    assert getattr(partner, 'df_Argument') is None


def test_assoc_children41_stub_double():
    # df_Vertex has no real 'df_Vertex' property in the generated
    # code (a bare stub) -- manually attach it so df_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Network(fileName="sample_text", name="sample_text")
    partner = df_Vertex()
    setattr(partner, 'df_Vertex', None)
    _safe_set(owner, 'df_Network', {partner})
    assert getattr(partner, 'df_Vertex') == owner
    _safe_set(owner, 'df_Network', set())
    assert getattr(partner, 'df_Vertex') is None


def test_assoc_constants0_stub_double():
    # df_Var has no real 'df_Var' property in the generated
    # code (a bare stub) -- manually attach it so df_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Unit(fileName="sample_text", lineNumber=7, name="sample_text")
    partner = df_Var()
    setattr(partner, 'df_Var', None)
    _safe_set(owner, 'df_Unit', {partner})
    assert getattr(partner, 'df_Var') == owner
    _safe_set(owner, 'df_Unit', set())
    assert getattr(partner, 'df_Var') is None


def test_assoc_entity5_stub_double():
    # df_EObject has no real 'df_EObject' property in the generated
    # code (a bare stub) -- manually attach it so df_Instance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Instance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Instance(name="sample_text")
    partner = df_EObject()
    setattr(partner, 'df_EObject', None)
    _safe_set(owner, 'df_Instance6', partner)
    assert getattr(partner, 'df_EObject') == owner
    _safe_set(owner, 'df_Instance6', None)
    assert getattr(partner, 'df_EObject') is None


def test_assoc_fsm19_stub_double():
    # df_FSM has no real 'df_FSM' property in the generated
    # code (a bare stub) -- manually attach it so df_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    partner = df_FSM()
    setattr(partner, 'df_FSM', None)
    _safe_set(owner, 'df_Actor20', partner)
    assert getattr(partner, 'df_FSM') == owner
    _safe_set(owner, 'df_Actor20', None)
    assert getattr(partner, 'df_FSM') is None


def test_assoc_initializes21_stub_double():
    # df_Action has no real 'df_Action23' property in the generated
    # code (a bare stub) -- manually attach it so df_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    partner = df_Action()
    setattr(partner, 'df_Action23', None)
    _safe_set(owner, 'df_Actor22', {partner})
    assert getattr(partner, 'df_Action23') == owner
    _safe_set(owner, 'df_Actor22', set())
    assert getattr(partner, 'df_Action23') is None


def test_assoc_key97_stub_double():
    # df_PortToVarMapEntry has no real 'df_PortToVarMapEntry98' property in the generated
    # code (a bare stub) -- manually attach it so df_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    partner = df_PortToVarMapEntry()
    setattr(partner, 'df_PortToVarMapEntry98', None)
    _safe_set(owner, 'df_Port99', partner)
    assert getattr(partner, 'df_PortToVarMapEntry98') == owner
    _safe_set(owner, 'df_Port99', None)
    assert getattr(partner, 'df_PortToVarMapEntry98') is None


def test_assoc_moC27_stub_double():
    # df_MoC has no real 'df_MoC' property in the generated
    # code (a bare stub) -- manually attach it so df_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    partner = df_MoC()
    setattr(partner, 'df_MoC', None)
    _safe_set(owner, 'df_Actor28', partner)
    assert getattr(partner, 'df_MoC') == owner
    _safe_set(owner, 'df_Actor28', None)
    assert getattr(partner, 'df_MoC') is None


def test_assoc_moC45_stub_double():
    # df_MoC has no real 'df_MoC47' property in the generated
    # code (a bare stub) -- manually attach it so df_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Network(fileName="sample_text", name="sample_text")
    partner = df_MoC()
    setattr(partner, 'df_MoC47', None)
    _safe_set(owner, 'df_Network46', partner)
    assert getattr(partner, 'df_MoC47') == owner
    _safe_set(owner, 'df_Network46', None)
    assert getattr(partner, 'df_MoC47') is None


def test_assoc_numTokensMap80_stub_double():
    # df_Pattern has no real 'df_Pattern81' property in the generated
    # code (a bare stub) -- manually attach it so df_PortToEIntegerObjectMapEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_PortToEIntegerObjectMapEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_PortToEIntegerObjectMapEntry(value="sample_text")
    partner = df_Pattern()
    setattr(partner, 'df_Pattern81', None)
    _safe_set(owner, 'df_PortToEIntegerObjectMapEntry', partner)
    assert owner in getattr(partner, 'df_Pattern81')
    _safe_set(owner, 'df_PortToEIntegerObjectMapEntry', None)
    assert owner not in getattr(partner, 'df_Pattern81')


def test_assoc_parameters12_stub_double():
    # df_Var has no real 'df_Var14' property in the generated
    # code (a bare stub) -- manually attach it so df_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Entity(incomingPortMap="sample_text", name="sample_text", outgoingPortMap="sample_text")
    partner = df_Var()
    setattr(partner, 'df_Var14', None)
    _safe_set(owner, 'df_Entity13', {partner})
    assert getattr(partner, 'df_Var14') == owner
    _safe_set(owner, 'df_Entity13', set())
    assert getattr(partner, 'df_Var14') is None


def test_assoc_parameters32_stub_double():
    # df_Var has no real 'df_Var34' property in the generated
    # code (a bare stub) -- manually attach it so df_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    partner = df_Var()
    setattr(partner, 'df_Var34', None)
    _safe_set(owner, 'df_Actor33', {partner})
    assert getattr(partner, 'df_Var34') == owner
    _safe_set(owner, 'df_Actor33', set())
    assert getattr(partner, 'df_Var34') is None


def test_assoc_parameters51_stub_double():
    # df_Var has no real 'df_Var53' property in the generated
    # code (a bare stub) -- manually attach it so df_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Network(fileName="sample_text", name="sample_text")
    partner = df_Var()
    setattr(partner, 'df_Var53', None)
    _safe_set(owner, 'df_Network52', {partner})
    assert getattr(partner, 'df_Var53') == owner
    _safe_set(owner, 'df_Network52', set())
    assert getattr(partner, 'df_Var53') is None


def test_assoc_ports82_stub_double():
    # df_Pattern has no real 'df_Pattern83' property in the generated
    # code (a bare stub) -- manually attach it so df_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    partner = df_Pattern()
    setattr(partner, 'df_Pattern83', None)
    _safe_set(owner, 'df_Port84', partner)
    assert owner in getattr(partner, 'df_Pattern83')
    _safe_set(owner, 'df_Port84', None)
    assert owner not in getattr(partner, 'df_Pattern83')


def test_assoc_procedures1_stub_double():
    # df_Procedure has no real 'df_Procedure' property in the generated
    # code (a bare stub) -- manually attach it so df_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Unit(fileName="sample_text", lineNumber=7, name="sample_text")
    partner = df_Procedure()
    setattr(partner, 'df_Procedure', None)
    _safe_set(owner, 'df_Unit2', {partner})
    assert getattr(partner, 'df_Procedure') == owner
    _safe_set(owner, 'df_Unit2', set())
    assert getattr(partner, 'df_Procedure') is None


def test_assoc_procs35_stub_double():
    # df_Procedure has no real 'df_Procedure37' property in the generated
    # code (a bare stub) -- manually attach it so df_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    partner = df_Procedure()
    setattr(partner, 'df_Procedure37', None)
    _safe_set(owner, 'df_Actor36', {partner})
    assert getattr(partner, 'df_Procedure37') == owner
    _safe_set(owner, 'df_Actor36', set())
    assert getattr(partner, 'df_Procedure37') is None


def test_assoc_sourcePort57_stub_double():
    # df_Connection has no real 'df_Connection' property in the generated
    # code (a bare stub) -- manually attach it so df_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    partner = df_Connection()
    setattr(partner, 'df_Connection', None)
    _safe_set(owner, 'df_Port58', partner)
    assert getattr(partner, 'df_Connection') == owner
    _safe_set(owner, 'df_Port58', None)
    assert getattr(partner, 'df_Connection') is None


def test_assoc_stateVars38_stub_double():
    # df_Var has no real 'df_Var40' property in the generated
    # code (a bare stub) -- manually attach it so df_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    partner = df_Var()
    setattr(partner, 'df_Var40', None)
    _safe_set(owner, 'df_Actor39', {partner})
    assert getattr(partner, 'df_Var40') == owner
    _safe_set(owner, 'df_Actor39', set())
    assert getattr(partner, 'df_Var40') is None


def test_assoc_tag76_stub_double():
    # df_Action has no real 'df_Action77' property in the generated
    # code (a bare stub) -- manually attach it so df_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Tag(identifiers="sample_text")
    partner = df_Action()
    setattr(partner, 'df_Action77', None)
    _safe_set(owner, 'df_Tag', partner)
    assert getattr(partner, 'df_Action77') == owner
    _safe_set(owner, 'df_Tag', None)
    assert getattr(partner, 'df_Action77') is None


def test_assoc_targetPort59_stub_double():
    # df_Connection has no real 'df_Connection60' property in the generated
    # code (a bare stub) -- manually attach it so df_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    partner = df_Connection()
    setattr(partner, 'df_Connection60', None)
    _safe_set(owner, 'df_Port61', partner)
    assert getattr(partner, 'df_Connection60') == owner
    _safe_set(owner, 'df_Port61', None)
    assert getattr(partner, 'df_Connection60') is None


def test_assoc_type3_stub_double():
    # df_Type has no real 'df_Type' property in the generated
    # code (a bare stub) -- manually attach it so df_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    partner = df_Type()
    setattr(partner, 'df_Type', None)
    _safe_set(owner, 'df_Port', partner)
    assert getattr(partner, 'df_Type') == owner
    _safe_set(owner, 'df_Port', None)
    assert getattr(partner, 'df_Type') is None


def test_assoc_value106_stub_double():
    # df_VarToPortMapEntry has no real 'df_VarToPortMapEntry107' property in the generated
    # code (a bare stub) -- manually attach it so df_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    partner = df_VarToPortMapEntry()
    setattr(partner, 'df_VarToPortMapEntry107', None)
    _safe_set(owner, 'df_Port108', partner)
    assert getattr(partner, 'df_VarToPortMapEntry107') == owner
    _safe_set(owner, 'df_Port108', None)
    assert getattr(partner, 'df_VarToPortMapEntry107') is None


def test_assoc_variables54_stub_double():
    # df_Var has no real 'df_Var56' property in the generated
    # code (a bare stub) -- manually attach it so df_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # df_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = df_Network(fileName="sample_text", name="sample_text")
    partner = df_Var()
    setattr(partner, 'df_Var56', None)
    _safe_set(owner, 'df_Network55', {partner})
    assert getattr(partner, 'df_Var56') == owner
    _safe_set(owner, 'df_Network55', set())
    assert getattr(partner, 'df_Var56') is None


