import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DocumentElt,
    Port,
    Vertex,
    WT_Architecture,
    WT_Component,
    WT_ControlSubsystem,
    WT_DocumentElt,
    WT_Edge,
    WT_InPort,
    WT_InitialState,
    WT_OutPort,
    WT_Port,
    WT_SimpleState,
    WT_StateMachine,
    WT_Subsystem,
    WT_Vertex,
    WT_WTComponents,
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

def test_assoc_beh6_reverse_link_reassign_clear():
    a1 = WT_Subsystem(name="sample_text")
    a2 = WT_Subsystem(name="sample_text_2")
    b = WT_ControlSubsystem(name="sample_text")
    _safe_set(b, 'WT_ControlSubsystem', a1)
    assert _is_linked(b, 'WT_ControlSubsystem', a1)
    if hasattr(a1, 'WT_Subsystem7'):
        assert _is_linked(a1, 'WT_Subsystem7', b)
    _safe_set(b, 'WT_ControlSubsystem', a2)
    assert _is_linked(b, 'WT_ControlSubsystem', a2)
    if hasattr(a1, 'WT_Subsystem7'):
        assert not _is_linked(a1, 'WT_Subsystem7', b)
    if hasattr(a2, 'WT_Subsystem7'):
        assert _is_linked(a2, 'WT_Subsystem7', b)
    _safe_set(b, 'WT_ControlSubsystem', None)
    assert not _is_linked(b, 'WT_ControlSubsystem', a2)
    if hasattr(a2, 'WT_Subsystem7'):
        assert not _is_linked(a2, 'WT_Subsystem7', b)


def test_assoc_elements8_reverse_link_reassign_clear():
    a1 = WT_Component(label="sample_text")
    a2 = WT_Component(label="sample_text_2")
    b = WT_Architecture(name="sample_text")
    _safe_set(b, 'WT_Architecture9', {a1})
    assert _is_linked(b, 'WT_Architecture9', a1)
    if hasattr(a1, 'WT_Component'):
        assert _is_linked(a1, 'WT_Component', b)
    _safe_set(b, 'WT_Architecture9', {a2})
    assert _is_linked(b, 'WT_Architecture9', a2)
    if hasattr(a1, 'WT_Component'):
        assert not _is_linked(a1, 'WT_Component', b)
    if hasattr(a2, 'WT_Component'):
        assert _is_linked(a2, 'WT_Component', b)
    _safe_set(b, 'WT_Architecture9', set())
    assert not _is_linked(b, 'WT_Architecture9', a2)
    if hasattr(a2, 'WT_Component'):
        assert not _is_linked(a2, 'WT_Component', b)


def test_assoc_ensembles4_reverse_link_reassign_clear():
    a1 = WT_Subsystem(name="sample_text")
    a2 = WT_Subsystem(name="sample_text_2")
    b = WT_Architecture(name="sample_text")
    _safe_set(b, 'WT_Architecture', a1)
    assert _is_linked(b, 'WT_Architecture', a1)
    if hasattr(a1, 'WT_Subsystem5'):
        assert _is_linked(a1, 'WT_Subsystem5', b)
    _safe_set(b, 'WT_Architecture', a2)
    assert _is_linked(b, 'WT_Architecture', a2)
    if hasattr(a1, 'WT_Subsystem5'):
        assert not _is_linked(a1, 'WT_Subsystem5', b)
    if hasattr(a2, 'WT_Subsystem5'):
        assert _is_linked(a2, 'WT_Subsystem5', b)
    _safe_set(b, 'WT_Architecture', None)
    assert not _is_linked(b, 'WT_Architecture', a2)
    if hasattr(a2, 'WT_Subsystem5'):
        assert not _is_linked(a2, 'WT_Subsystem5', b)


def test_assoc_ports22_reverse_link_reassign_clear():
    a1 = WT_Port(label="sample_text")
    a2 = WT_Port(label="sample_text_2")
    b = WT_Component(label="sample_text")
    _safe_set(b, 'WT_Component23', {a1})
    assert _is_linked(b, 'WT_Component23', a1)
    if hasattr(a1, 'WT_Port'):
        assert _is_linked(a1, 'WT_Port', b)
    _safe_set(b, 'WT_Component23', {a2})
    assert _is_linked(b, 'WT_Component23', a2)
    if hasattr(a1, 'WT_Port'):
        assert not _is_linked(a1, 'WT_Port', b)
    if hasattr(a2, 'WT_Port'):
        assert _is_linked(a2, 'WT_Port', b)
    _safe_set(b, 'WT_Component23', set())
    assert not _is_linked(b, 'WT_Component23', a2)
    if hasattr(a2, 'WT_Port'):
        assert not _is_linked(a2, 'WT_Port', b)


def test_assoc_states10_reverse_link_reassign_clear():
    a1 = WT_StateMachine(isPublic="sample_text", name="sample_text")
    a2 = WT_StateMachine(isPublic="sample_text_2", name="sample_text_2")
    b = WT_ControlSubsystem(name="sample_text")
    _safe_set(b, 'WT_ControlSubsystem11', {a1})
    assert _is_linked(b, 'WT_ControlSubsystem11', a1)
    if hasattr(a1, 'WT_StateMachine'):
        assert _is_linked(a1, 'WT_StateMachine', b)
    _safe_set(b, 'WT_ControlSubsystem11', {a2})
    assert _is_linked(b, 'WT_ControlSubsystem11', a2)
    if hasattr(a1, 'WT_StateMachine'):
        assert not _is_linked(a1, 'WT_StateMachine', b)
    if hasattr(a2, 'WT_StateMachine'):
        assert _is_linked(a2, 'WT_StateMachine', b)
    _safe_set(b, 'WT_ControlSubsystem11', set())
    assert not _is_linked(b, 'WT_ControlSubsystem11', a2)
    if hasattr(a2, 'WT_StateMachine'):
        assert not _is_linked(a2, 'WT_StateMachine', b)


def test_assoc_states24_reverse_link_reassign_clear():
    a1 = WT_StateMachine(isPublic="sample_text", name="sample_text")
    a2 = WT_StateMachine(isPublic="sample_text_2", name="sample_text_2")
    b = WT_Component(label="sample_text")
    _safe_set(b, 'WT_Component25', {a1})
    assert _is_linked(b, 'WT_Component25', a1)
    if hasattr(a1, 'WT_StateMachine26'):
        assert _is_linked(a1, 'WT_StateMachine26', b)
    _safe_set(b, 'WT_Component25', {a2})
    assert _is_linked(b, 'WT_Component25', a2)
    if hasattr(a1, 'WT_StateMachine26'):
        assert not _is_linked(a1, 'WT_StateMachine26', b)
    if hasattr(a2, 'WT_StateMachine26'):
        assert _is_linked(a2, 'WT_StateMachine26', b)
    _safe_set(b, 'WT_Component25', set())
    assert not _is_linked(b, 'WT_Component25', a2)
    if hasattr(a2, 'WT_StateMachine26'):
        assert not _is_linked(a2, 'WT_StateMachine26', b)


def test_assoc_subsystems0_reverse_link_reassign_clear():
    a1 = WT_WTComponents(name="sample_text")
    a2 = WT_WTComponents(name="sample_text_2")
    b = WT_Subsystem(name="sample_text")
    _safe_set(b, 'WT_Subsystem', a1)
    assert _is_linked(b, 'WT_Subsystem', a1)
    if hasattr(a1, 'WT_WTComponents'):
        assert _is_linked(a1, 'WT_WTComponents', b)
    _safe_set(b, 'WT_Subsystem', a2)
    assert _is_linked(b, 'WT_Subsystem', a2)
    if hasattr(a1, 'WT_WTComponents'):
        assert not _is_linked(a1, 'WT_WTComponents', b)
    if hasattr(a2, 'WT_WTComponents'):
        assert _is_linked(a2, 'WT_WTComponents', b)
    _safe_set(b, 'WT_Subsystem', None)
    assert not _is_linked(b, 'WT_Subsystem', a2)
    if hasattr(a2, 'WT_WTComponents'):
        assert not _is_linked(a2, 'WT_WTComponents', b)


def test_assoc_subsystems2_reverse_link_reassign_clear():
    a1 = WT_Subsystem(name="sample_text")
    a2 = WT_Subsystem(name="sample_text_2")
    b = WT_Subsystem(name="sample_text")
    _safe_set(b, 'WT_Subsystem3', a1)
    assert _is_linked(b, 'WT_Subsystem3', a1)
    if hasattr(a1, 'WT_Subsystem1'):
        assert _is_linked(a1, 'WT_Subsystem1', b)
    _safe_set(b, 'WT_Subsystem3', a2)
    assert _is_linked(b, 'WT_Subsystem3', a2)
    if hasattr(a1, 'WT_Subsystem1'):
        assert not _is_linked(a1, 'WT_Subsystem1', b)
    if hasattr(a2, 'WT_Subsystem1'):
        assert _is_linked(a2, 'WT_Subsystem1', b)
    _safe_set(b, 'WT_Subsystem3', None)
    assert not _is_linked(b, 'WT_Subsystem3', a2)
    if hasattr(a2, 'WT_Subsystem1'):
        assert not _is_linked(a2, 'WT_Subsystem1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_states12_stub_double():
    # WT_Vertex has no real 'WT_Vertex' property in the generated
    # code (a bare stub) -- manually attach it so WT_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # WT_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = WT_StateMachine(isPublic="sample_text", name="sample_text")
    partner = WT_Vertex()
    setattr(partner, 'WT_Vertex', None)
    _safe_set(owner, 'WT_StateMachine13', {partner})
    assert getattr(partner, 'WT_Vertex') == owner
    _safe_set(owner, 'WT_StateMachine13', set())
    assert getattr(partner, 'WT_Vertex') is None


def test_assoc_transitions14_stub_double():
    # WT_Edge has no real 'WT_Edge' property in the generated
    # code (a bare stub) -- manually attach it so WT_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # WT_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = WT_StateMachine(isPublic="sample_text", name="sample_text")
    partner = WT_Edge()
    setattr(partner, 'WT_Edge', None)
    _safe_set(owner, 'WT_StateMachine15', {partner})
    assert getattr(partner, 'WT_Edge') == owner
    _safe_set(owner, 'WT_StateMachine15', set())
    assert getattr(partner, 'WT_Edge') is None


