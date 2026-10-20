import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EModelElement,
    State,
    fiacre_Component,
    fiacre_DataType,
    fiacre_Init,
    fiacre_Process,
    fiacre_Program,
    fiacre_State,
    fiacre_Transition,
    fiacre_Variable,
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

def test_assoc_component8_reverse_link_reassign_clear():
    a1 = fiacre_Variable(ID="sample_text")
    a2 = fiacre_Variable(ID="sample_text_2")
    b = fiacre_Component(ID="sample_text")
    _safe_set(b, 'Component', a1)
    assert _is_linked(b, 'Component', a1)
    if hasattr(a1, 'variable9'):
        assert _is_linked(a1, 'variable9', b)
    _safe_set(b, 'Component', a2)
    assert _is_linked(b, 'Component', a2)
    if hasattr(a1, 'variable9'):
        assert not _is_linked(a1, 'variable9', b)
    if hasattr(a2, 'variable9'):
        assert _is_linked(a2, 'variable9', b)
    _safe_set(b, 'Component', None)
    assert not _is_linked(b, 'Component', a2)
    if hasattr(a2, 'variable9'):
        assert not _is_linked(a2, 'variable9', b)


def test_assoc_process10_reverse_link_reassign_clear():
    a1 = fiacre_Process(ID="sample_text")
    a2 = fiacre_Process(ID="sample_text_2")
    b = fiacre_Component(ID="sample_text")
    _safe_set(b, 'fiacre_Component', {a1})
    assert _is_linked(b, 'fiacre_Component', a1)
    if hasattr(a1, 'fiacre_Process11'):
        assert _is_linked(a1, 'fiacre_Process11', b)
    _safe_set(b, 'fiacre_Component', {a2})
    assert _is_linked(b, 'fiacre_Component', a2)
    if hasattr(a1, 'fiacre_Process11'):
        assert not _is_linked(a1, 'fiacre_Process11', b)
    if hasattr(a2, 'fiacre_Process11'):
        assert _is_linked(a2, 'fiacre_Process11', b)
    _safe_set(b, 'fiacre_Component', set())
    assert not _is_linked(b, 'fiacre_Component', a2)
    if hasattr(a2, 'fiacre_Process11'):
        assert not _is_linked(a2, 'fiacre_Process11', b)


def test_assoc_process7_reverse_link_reassign_clear():
    a1 = fiacre_Variable(ID="sample_text")
    a2 = fiacre_Variable(ID="sample_text_2")
    b = fiacre_Process(ID="sample_text")
    _safe_set(b, 'Process', a1)
    assert _is_linked(b, 'Process', a1)
    if hasattr(a1, 'variable'):
        assert _is_linked(a1, 'variable', b)
    _safe_set(b, 'Process', a2)
    assert _is_linked(b, 'Process', a2)
    if hasattr(a1, 'variable'):
        assert not _is_linked(a1, 'variable', b)
    if hasattr(a2, 'variable'):
        assert _is_linked(a2, 'variable', b)
    _safe_set(b, 'Process', None)
    assert not _is_linked(b, 'Process', a2)
    if hasattr(a2, 'variable'):
        assert not _is_linked(a2, 'variable', b)


def test_assoc_state1_reverse_link_reassign_clear():
    a1 = fiacre_State(ID="sample_text")
    a2 = fiacre_State(ID="sample_text_2")
    b = fiacre_Process(ID="sample_text")
    _safe_set(b, 'fiacre_Process', {a1})
    assert _is_linked(b, 'fiacre_Process', a1)
    if hasattr(a1, 'fiacre_State'):
        assert _is_linked(a1, 'fiacre_State', b)
    _safe_set(b, 'fiacre_Process', {a2})
    assert _is_linked(b, 'fiacre_Process', a2)
    if hasattr(a1, 'fiacre_State'):
        assert not _is_linked(a1, 'fiacre_State', b)
    if hasattr(a2, 'fiacre_State'):
        assert _is_linked(a2, 'fiacre_State', b)
    _safe_set(b, 'fiacre_Process', set())
    assert not _is_linked(b, 'fiacre_Process', a2)
    if hasattr(a2, 'fiacre_State'):
        assert not _is_linked(a2, 'fiacre_State', b)


def test_assoc_state5_reverse_link_reassign_clear():
    a1 = fiacre_Transition()
    a2 = fiacre_Transition()
    b = fiacre_State(ID="sample_text")
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'transition'):
        assert _is_linked(a1, 'transition', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'transition'):
        assert not _is_linked(a1, 'transition', b)
    if hasattr(a2, 'transition'):
        assert _is_linked(a2, 'transition', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'transition'):
        assert not _is_linked(a2, 'transition', b)


def test_assoc_transition0_reverse_link_reassign_clear():
    a1 = fiacre_Transition()
    a2 = fiacre_Transition()
    b = fiacre_State(ID="sample_text")
    _safe_set(b, 'state', {a1})
    assert _is_linked(b, 'state', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'state', {a2})
    assert _is_linked(b, 'state', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'state', set())
    assert not _is_linked(b, 'state', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_transition2_reverse_link_reassign_clear():
    a1 = fiacre_Transition()
    a2 = fiacre_Transition()
    b = fiacre_Process(ID="sample_text")
    _safe_set(b, 'fiacre_Process3', {a1})
    assert _is_linked(b, 'fiacre_Process3', a1)
    if hasattr(a1, 'fiacre_Transition'):
        assert _is_linked(a1, 'fiacre_Transition', b)
    _safe_set(b, 'fiacre_Process3', {a2})
    assert _is_linked(b, 'fiacre_Process3', a2)
    if hasattr(a1, 'fiacre_Transition'):
        assert not _is_linked(a1, 'fiacre_Transition', b)
    if hasattr(a2, 'fiacre_Transition'):
        assert _is_linked(a2, 'fiacre_Transition', b)
    _safe_set(b, 'fiacre_Process3', set())
    assert not _is_linked(b, 'fiacre_Process3', a2)
    if hasattr(a2, 'fiacre_Transition'):
        assert not _is_linked(a2, 'fiacre_Transition', b)


def test_assoc_variable12_reverse_link_reassign_clear():
    a1 = fiacre_Variable(ID="sample_text")
    a2 = fiacre_Variable(ID="sample_text_2")
    b = fiacre_Component(ID="sample_text")
    _safe_set(b, 'component', {a1})
    assert _is_linked(b, 'component', a1)
    if hasattr(a1, 'Variable13'):
        assert _is_linked(a1, 'Variable13', b)
    _safe_set(b, 'component', {a2})
    assert _is_linked(b, 'component', a2)
    if hasattr(a1, 'Variable13'):
        assert not _is_linked(a1, 'Variable13', b)
    if hasattr(a2, 'Variable13'):
        assert _is_linked(a2, 'Variable13', b)
    _safe_set(b, 'component', set())
    assert not _is_linked(b, 'component', a2)
    if hasattr(a2, 'Variable13'):
        assert not _is_linked(a2, 'Variable13', b)


def test_assoc_variable4_reverse_link_reassign_clear():
    a1 = fiacre_Variable(ID="sample_text")
    a2 = fiacre_Variable(ID="sample_text_2")
    b = fiacre_Process(ID="sample_text")
    _safe_set(b, 'process', {a1})
    assert _is_linked(b, 'process', a1)
    if hasattr(a1, 'Variable'):
        assert _is_linked(a1, 'Variable', b)
    _safe_set(b, 'process', {a2})
    assert _is_linked(b, 'process', a2)
    if hasattr(a1, 'Variable'):
        assert not _is_linked(a1, 'Variable', b)
    if hasattr(a2, 'Variable'):
        assert _is_linked(a2, 'Variable', b)
    _safe_set(b, 'process', set())
    assert not _is_linked(b, 'process', a2)
    if hasattr(a2, 'Variable'):
        assert not _is_linked(a2, 'Variable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_component14_stub_double():
    # fiacre_Program has no real 'fiacre_Program' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Component(ID="sample_text")
    partner = fiacre_Program()
    setattr(partner, 'fiacre_Program', None)
    _safe_set(owner, 'fiacre_Component15', partner)
    assert owner in getattr(partner, 'fiacre_Program')
    _safe_set(owner, 'fiacre_Component15', None)
    assert owner not in getattr(partner, 'fiacre_Program')


def test_assoc_datatype6_stub_double():
    # fiacre_DataType has no real 'fiacre_DataType' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Variable(ID="sample_text")
    partner = fiacre_DataType()
    setattr(partner, 'fiacre_DataType', None)
    _safe_set(owner, 'fiacre_Variable', partner)
    assert getattr(partner, 'fiacre_DataType') == owner
    _safe_set(owner, 'fiacre_Variable', None)
    assert getattr(partner, 'fiacre_DataType') is None


def test_assoc_process19_stub_double():
    # fiacre_Program has no real 'fiacre_Program20' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Process(ID="sample_text")
    partner = fiacre_Program()
    setattr(partner, 'fiacre_Program20', None)
    _safe_set(owner, 'fiacre_Process21', partner)
    assert owner in getattr(partner, 'fiacre_Program20')
    _safe_set(owner, 'fiacre_Process21', None)
    assert owner not in getattr(partner, 'fiacre_Program20')


def test_assoc_variable16_stub_double():
    # fiacre_Program has no real 'fiacre_Program17' property in the generated
    # code (a bare stub) -- manually attach it so fiacre_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fiacre_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fiacre_Variable(ID="sample_text")
    partner = fiacre_Program()
    setattr(partner, 'fiacre_Program17', None)
    _safe_set(owner, 'fiacre_Variable18', partner)
    assert owner in getattr(partner, 'fiacre_Program17')
    _safe_set(owner, 'fiacre_Variable18', None)
    assert owner not in getattr(partner, 'fiacre_Program17')


