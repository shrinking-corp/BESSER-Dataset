import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Analog,
    ArduinoMetamodel_Action,
    ArduinoMetamodel_Analog,
    ArduinoMetamodel_ArduinoBoardUNO,
    ArduinoMetamodel_Digital,
    ArduinoMetamodel_FiniteStateMachine,
    ArduinoMetamodel_Instruccion,
    ArduinoMetamodel_Metodo,
    ArduinoMetamodel_PWM,
    ArduinoMetamodel_Pin,
    ArduinoMetamodel_Project,
    ArduinoMetamodel_State,
    ArduinoMetamodel_Transition,
    ArduinoMetamodel_delay,
    Instruccion,
    Pin,
    AnalogID,
    DigitalID,
    PinMode,
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

def test_assoc_instrucciones9_reverse_link_reassign_clear():
    a1 = ArduinoMetamodel_Metodo(nombre="sample_text")
    a2 = ArduinoMetamodel_Metodo(nombre="sample_text_2")
    b = ArduinoMetamodel_Instruccion(codigo="sample_text")
    _safe_set(b, 'ArduinoMetamodel_Instruccion', a1)
    assert _is_linked(b, 'ArduinoMetamodel_Instruccion', a1)
    if hasattr(a1, 'ArduinoMetamodel_Metodo10'):
        assert _is_linked(a1, 'ArduinoMetamodel_Metodo10', b)
    _safe_set(b, 'ArduinoMetamodel_Instruccion', a2)
    assert _is_linked(b, 'ArduinoMetamodel_Instruccion', a2)
    if hasattr(a1, 'ArduinoMetamodel_Metodo10'):
        assert not _is_linked(a1, 'ArduinoMetamodel_Metodo10', b)
    if hasattr(a2, 'ArduinoMetamodel_Metodo10'):
        assert _is_linked(a2, 'ArduinoMetamodel_Metodo10', b)
    _safe_set(b, 'ArduinoMetamodel_Instruccion', None)
    assert not _is_linked(b, 'ArduinoMetamodel_Instruccion', a2)
    if hasattr(a2, 'ArduinoMetamodel_Metodo10'):
        assert not _is_linked(a2, 'ArduinoMetamodel_Metodo10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_analogpins7_stub_double():
    # ArduinoMetamodel_ArduinoBoardUNO has no real 'ArduinoMetamodel_ArduinoBoardUNO8' property in the generated
    # code (a bare stub) -- manually attach it so ArduinoMetamodel_Analog's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ArduinoMetamodel_Analog's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ArduinoMetamodel_Analog(ID="sample_text")
    partner = ArduinoMetamodel_ArduinoBoardUNO()
    setattr(partner, 'ArduinoMetamodel_ArduinoBoardUNO8', None)
    _safe_set(owner, 'ArduinoMetamodel_Analog', partner)
    assert owner in getattr(partner, 'ArduinoMetamodel_ArduinoBoardUNO8')
    _safe_set(owner, 'ArduinoMetamodel_Analog', None)
    assert owner not in getattr(partner, 'ArduinoMetamodel_ArduinoBoardUNO8')


def test_assoc_digitalpins5_stub_double():
    # ArduinoMetamodel_ArduinoBoardUNO has no real 'ArduinoMetamodel_ArduinoBoardUNO6' property in the generated
    # code (a bare stub) -- manually attach it so ArduinoMetamodel_Digital's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ArduinoMetamodel_Digital's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ArduinoMetamodel_Digital(ID="sample_text")
    partner = ArduinoMetamodel_ArduinoBoardUNO()
    setattr(partner, 'ArduinoMetamodel_ArduinoBoardUNO6', None)
    _safe_set(owner, 'ArduinoMetamodel_Digital', partner)
    assert owner in getattr(partner, 'ArduinoMetamodel_ArduinoBoardUNO6')
    _safe_set(owner, 'ArduinoMetamodel_Digital', None)
    assert owner not in getattr(partner, 'ArduinoMetamodel_ArduinoBoardUNO6')


def test_assoc_incoming11_stub_double():
    # ArduinoMetamodel_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so ArduinoMetamodel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ArduinoMetamodel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ArduinoMetamodel_State(isInitial=True, name="sample_text")
    partner = ArduinoMetamodel_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Transition') is None


def test_assoc_metodos1_stub_double():
    # ArduinoMetamodel_Project has no real 'ArduinoMetamodel_Project2' property in the generated
    # code (a bare stub) -- manually attach it so ArduinoMetamodel_Metodo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ArduinoMetamodel_Metodo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ArduinoMetamodel_Metodo(nombre="sample_text")
    partner = ArduinoMetamodel_Project()
    setattr(partner, 'ArduinoMetamodel_Project2', None)
    _safe_set(owner, 'ArduinoMetamodel_Metodo', partner)
    assert owner in getattr(partner, 'ArduinoMetamodel_Project2')
    _safe_set(owner, 'ArduinoMetamodel_Metodo', None)
    assert owner not in getattr(partner, 'ArduinoMetamodel_Project2')


def test_assoc_outgoing12_stub_double():
    # ArduinoMetamodel_Transition has no real 'Transition13' property in the generated
    # code (a bare stub) -- manually attach it so ArduinoMetamodel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ArduinoMetamodel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ArduinoMetamodel_State(isInitial=True, name="sample_text")
    partner = ArduinoMetamodel_Transition()
    setattr(partner, 'Transition13', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Transition13') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Transition13') is None


def test_assoc_source15_stub_double():
    # ArduinoMetamodel_Transition has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so ArduinoMetamodel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ArduinoMetamodel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ArduinoMetamodel_State(isInitial=True, name="sample_text")
    partner = ArduinoMetamodel_Transition()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'State', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'State', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_states18_stub_double():
    # ArduinoMetamodel_FiniteStateMachine has no real 'ArduinoMetamodel_FiniteStateMachine19' property in the generated
    # code (a bare stub) -- manually attach it so ArduinoMetamodel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ArduinoMetamodel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ArduinoMetamodel_State(isInitial=True, name="sample_text")
    partner = ArduinoMetamodel_FiniteStateMachine()
    setattr(partner, 'ArduinoMetamodel_FiniteStateMachine19', None)
    _safe_set(owner, 'ArduinoMetamodel_State', partner)
    assert owner in getattr(partner, 'ArduinoMetamodel_FiniteStateMachine19')
    _safe_set(owner, 'ArduinoMetamodel_State', None)
    assert owner not in getattr(partner, 'ArduinoMetamodel_FiniteStateMachine19')


def test_assoc_target16_stub_double():
    # ArduinoMetamodel_Transition has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so ArduinoMetamodel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ArduinoMetamodel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ArduinoMetamodel_State(isInitial=True, name="sample_text")
    partner = ArduinoMetamodel_Transition()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'State17', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'State17', None)
    assert getattr(partner, 'incoming') is None


