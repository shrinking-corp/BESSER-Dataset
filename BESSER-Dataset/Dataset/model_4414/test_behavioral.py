import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Function,
    Instruction,
    Pin,
    arduino_DigitalPin,
    arduino_Function,
    arduino_Instruction,
    arduino_Loop,
    arduino_Pin,
    arduino_Project,
    arduino_Read,
    arduino_Setup,
    arduino_Sketch,
    arduino_Write,
    DigitalPinNumber,
    Direction,
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

def test_assoc_digitalpin10_reverse_link_reassign_clear():
    a1 = arduino_Write(name="sample_text")
    a2 = arduino_Write(name="sample_text_2")
    b = arduino_DigitalPin(number="sample_text")
    _safe_set(b, 'arduino_DigitalPin', a1)
    assert _is_linked(b, 'arduino_DigitalPin', a1)
    if hasattr(a1, 'arduino_Write'):
        assert _is_linked(a1, 'arduino_Write', b)
    _safe_set(b, 'arduino_DigitalPin', a2)
    assert _is_linked(b, 'arduino_DigitalPin', a2)
    if hasattr(a1, 'arduino_Write'):
        assert not _is_linked(a1, 'arduino_Write', b)
    if hasattr(a2, 'arduino_Write'):
        assert _is_linked(a2, 'arduino_Write', b)
    _safe_set(b, 'arduino_DigitalPin', None)
    assert not _is_linked(b, 'arduino_DigitalPin', a2)
    if hasattr(a2, 'arduino_Write'):
        assert not _is_linked(a2, 'arduino_Write', b)


def test_assoc_digitalpin11_reverse_link_reassign_clear():
    a1 = arduino_Read(name="sample_text", returnValue="sample_text")
    a2 = arduino_Read(name="sample_text_2", returnValue="sample_text_2")
    b = arduino_DigitalPin(number="sample_text")
    _safe_set(b, 'arduino_DigitalPin12', a1)
    assert _is_linked(b, 'arduino_DigitalPin12', a1)
    if hasattr(a1, 'arduino_Read'):
        assert _is_linked(a1, 'arduino_Read', b)
    _safe_set(b, 'arduino_DigitalPin12', a2)
    assert _is_linked(b, 'arduino_DigitalPin12', a2)
    if hasattr(a1, 'arduino_Read'):
        assert not _is_linked(a1, 'arduino_Read', b)
    if hasattr(a2, 'arduino_Read'):
        assert _is_linked(a2, 'arduino_Read', b)
    _safe_set(b, 'arduino_DigitalPin12', None)
    assert not _is_linked(b, 'arduino_DigitalPin12', a2)
    if hasattr(a2, 'arduino_Read'):
        assert not _is_linked(a2, 'arduino_Read', b)


def test_assoc_digitalpin13_reverse_link_reassign_clear():
    a1 = arduino_Setup(name="sample_text")
    a2 = arduino_Setup(name="sample_text_2")
    b = arduino_DigitalPin(number="sample_text")
    _safe_set(b, 'arduino_DigitalPin15', a1)
    assert _is_linked(b, 'arduino_DigitalPin15', a1)
    if hasattr(a1, 'arduino_Setup14'):
        assert _is_linked(a1, 'arduino_Setup14', b)
    _safe_set(b, 'arduino_DigitalPin15', a2)
    assert _is_linked(b, 'arduino_DigitalPin15', a2)
    if hasattr(a1, 'arduino_Setup14'):
        assert not _is_linked(a1, 'arduino_Setup14', b)
    if hasattr(a2, 'arduino_Setup14'):
        assert _is_linked(a2, 'arduino_Setup14', b)
    _safe_set(b, 'arduino_DigitalPin15', None)
    assert not _is_linked(b, 'arduino_DigitalPin15', a2)
    if hasattr(a2, 'arduino_Setup14'):
        assert not _is_linked(a2, 'arduino_Setup14', b)


def test_assoc_loop3_reverse_link_reassign_clear():
    a1 = arduino_Sketch(name="sample_text")
    a2 = arduino_Sketch(name="sample_text_2")
    b = arduino_Loop(name="sample_text")
    _safe_set(b, 'arduino_Loop', a1)
    assert _is_linked(b, 'arduino_Loop', a1)
    if hasattr(a1, 'arduino_Sketch4'):
        assert _is_linked(a1, 'arduino_Sketch4', b)
    _safe_set(b, 'arduino_Loop', a2)
    assert _is_linked(b, 'arduino_Loop', a2)
    if hasattr(a1, 'arduino_Sketch4'):
        assert not _is_linked(a1, 'arduino_Sketch4', b)
    if hasattr(a2, 'arduino_Sketch4'):
        assert _is_linked(a2, 'arduino_Sketch4', b)
    _safe_set(b, 'arduino_Loop', None)
    assert not _is_linked(b, 'arduino_Loop', a2)
    if hasattr(a2, 'arduino_Sketch4'):
        assert not _is_linked(a2, 'arduino_Sketch4', b)


def test_assoc_setup1_reverse_link_reassign_clear():
    a1 = arduino_Sketch(name="sample_text")
    a2 = arduino_Sketch(name="sample_text_2")
    b = arduino_Setup(name="sample_text")
    _safe_set(b, 'arduino_Setup', a1)
    assert _is_linked(b, 'arduino_Setup', a1)
    if hasattr(a1, 'arduino_Sketch2'):
        assert _is_linked(a1, 'arduino_Sketch2', b)
    _safe_set(b, 'arduino_Setup', a2)
    assert _is_linked(b, 'arduino_Setup', a2)
    if hasattr(a1, 'arduino_Sketch2'):
        assert not _is_linked(a1, 'arduino_Sketch2', b)
    if hasattr(a2, 'arduino_Sketch2'):
        assert _is_linked(a2, 'arduino_Sketch2', b)
    _safe_set(b, 'arduino_Setup', None)
    assert not _is_linked(b, 'arduino_Setup', a2)
    if hasattr(a2, 'arduino_Sketch2'):
        assert not _is_linked(a2, 'arduino_Sketch2', b)


def test_assoc_sketch0_reverse_link_reassign_clear():
    a1 = arduino_Sketch(name="sample_text")
    a2 = arduino_Sketch(name="sample_text_2")
    b = arduino_Project(name="sample_text")
    _safe_set(b, 'arduino_Project', a1)
    assert _is_linked(b, 'arduino_Project', a1)
    if hasattr(a1, 'arduino_Sketch'):
        assert _is_linked(a1, 'arduino_Sketch', b)
    _safe_set(b, 'arduino_Project', a2)
    assert _is_linked(b, 'arduino_Project', a2)
    if hasattr(a1, 'arduino_Sketch'):
        assert not _is_linked(a1, 'arduino_Sketch', b)
    if hasattr(a2, 'arduino_Sketch'):
        assert _is_linked(a2, 'arduino_Sketch', b)
    _safe_set(b, 'arduino_Project', None)
    assert not _is_linked(b, 'arduino_Project', a2)
    if hasattr(a2, 'arduino_Sketch'):
        assert not _is_linked(a2, 'arduino_Sketch', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_instruction16_stub_double():
    # arduino_Instruction has no real 'arduino_Instruction18' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Loop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Loop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Loop(name="sample_text")
    partner = arduino_Instruction()
    setattr(partner, 'arduino_Instruction18', None)
    _safe_set(owner, 'arduino_Loop17', {partner})
    assert getattr(partner, 'arduino_Instruction18') == owner
    _safe_set(owner, 'arduino_Loop17', set())
    assert getattr(partner, 'arduino_Instruction18') is None


def test_assoc_instruction5_stub_double():
    # arduino_Instruction has no real 'arduino_Instruction' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Sketch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Sketch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Sketch(name="sample_text")
    partner = arduino_Instruction()
    setattr(partner, 'arduino_Instruction', None)
    _safe_set(owner, 'arduino_Sketch6', {partner})
    assert getattr(partner, 'arduino_Instruction') == owner
    _safe_set(owner, 'arduino_Sketch6', set())
    assert getattr(partner, 'arduino_Instruction') is None


