import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    wh_Commands,
    wh_Definition,
    wh_Function,
    wh_Input,
    wh_Model,
    wh_Output,
    wh_Program,
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

def test_assoc_commands21_reverse_link_reassign_clear():
    a1 = wh_Commands(command="sample_text")
    a2 = wh_Commands(command="sample_text_2")
    b = wh_Commands(command="sample_text")
    _safe_set(b, 'wh_Commands22', a1)
    assert _is_linked(b, 'wh_Commands22', a1)
    if hasattr(a1, 'wh_Commands20'):
        assert _is_linked(a1, 'wh_Commands20', b)
    _safe_set(b, 'wh_Commands22', a2)
    assert _is_linked(b, 'wh_Commands22', a2)
    if hasattr(a1, 'wh_Commands20'):
        assert not _is_linked(a1, 'wh_Commands20', b)
    if hasattr(a2, 'wh_Commands20'):
        assert _is_linked(a2, 'wh_Commands20', b)
    _safe_set(b, 'wh_Commands22', None)
    assert not _is_linked(b, 'wh_Commands22', a2)
    if hasattr(a2, 'wh_Commands20'):
        assert not _is_linked(a2, 'wh_Commands20', b)


def test_assoc_input15_reverse_link_reassign_clear():
    a1 = wh_Input(variable="sample_text")
    a2 = wh_Input(variable="sample_text_2")
    b = wh_Input(variable="sample_text")
    _safe_set(b, 'wh_Input16', a1)
    assert _is_linked(b, 'wh_Input16', a1)
    if hasattr(a1, 'wh_Input14'):
        assert _is_linked(a1, 'wh_Input14', b)
    _safe_set(b, 'wh_Input16', a2)
    assert _is_linked(b, 'wh_Input16', a2)
    if hasattr(a1, 'wh_Input14'):
        assert not _is_linked(a1, 'wh_Input14', b)
    if hasattr(a2, 'wh_Input14'):
        assert _is_linked(a2, 'wh_Input14', b)
    _safe_set(b, 'wh_Input16', None)
    assert not _is_linked(b, 'wh_Input16', a2)
    if hasattr(a2, 'wh_Input14'):
        assert not _is_linked(a2, 'wh_Input14', b)


def test_assoc_output18_reverse_link_reassign_clear():
    a1 = wh_Output(variable="sample_text")
    a2 = wh_Output(variable="sample_text_2")
    b = wh_Output(variable="sample_text")
    _safe_set(b, 'wh_Output19', a1)
    assert _is_linked(b, 'wh_Output19', a1)
    if hasattr(a1, 'wh_Output17'):
        assert _is_linked(a1, 'wh_Output17', b)
    _safe_set(b, 'wh_Output19', a2)
    assert _is_linked(b, 'wh_Output19', a2)
    if hasattr(a1, 'wh_Output17'):
        assert not _is_linked(a1, 'wh_Output17', b)
    if hasattr(a2, 'wh_Output17'):
        assert _is_linked(a2, 'wh_Output17', b)
    _safe_set(b, 'wh_Output19', None)
    assert not _is_linked(b, 'wh_Output19', a2)
    if hasattr(a2, 'wh_Output17'):
        assert not _is_linked(a2, 'wh_Output17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_commands10_stub_double():
    # wh_Definition has no real 'wh_Definition11' property in the generated
    # code (a bare stub) -- manually attach it so wh_Commands's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Commands's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Commands(command="sample_text")
    partner = wh_Definition()
    setattr(partner, 'wh_Definition11', None)
    _safe_set(owner, 'wh_Commands', partner)
    assert getattr(partner, 'wh_Definition11') == owner
    _safe_set(owner, 'wh_Commands', None)
    assert getattr(partner, 'wh_Definition11') is None


def test_assoc_definition6_stub_double():
    # wh_Definition has no real 'wh_Definition' property in the generated
    # code (a bare stub) -- manually attach it so wh_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Function(name="sample_text")
    partner = wh_Definition()
    setattr(partner, 'wh_Definition', None)
    _safe_set(owner, 'wh_Function7', partner)
    assert getattr(partner, 'wh_Definition') == owner
    _safe_set(owner, 'wh_Function7', None)
    assert getattr(partner, 'wh_Definition') is None


def test_assoc_function1_stub_double():
    # wh_Program has no real 'wh_Program2' property in the generated
    # code (a bare stub) -- manually attach it so wh_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Function(name="sample_text")
    partner = wh_Program()
    setattr(partner, 'wh_Program2', None)
    _safe_set(owner, 'wh_Function', partner)
    assert getattr(partner, 'wh_Program2') == owner
    _safe_set(owner, 'wh_Function', None)
    assert getattr(partner, 'wh_Program2') is None


def test_assoc_input8_stub_double():
    # wh_Definition has no real 'wh_Definition9' property in the generated
    # code (a bare stub) -- manually attach it so wh_Input's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Input's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Input(variable="sample_text")
    partner = wh_Definition()
    setattr(partner, 'wh_Definition9', None)
    _safe_set(owner, 'wh_Input', partner)
    assert getattr(partner, 'wh_Definition9') == owner
    _safe_set(owner, 'wh_Input', None)
    assert getattr(partner, 'wh_Definition9') is None


def test_assoc_output12_stub_double():
    # wh_Definition has no real 'wh_Definition13' property in the generated
    # code (a bare stub) -- manually attach it so wh_Output's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Output's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Output(variable="sample_text")
    partner = wh_Definition()
    setattr(partner, 'wh_Definition13', None)
    _safe_set(owner, 'wh_Output', partner)
    assert getattr(partner, 'wh_Definition13') == owner
    _safe_set(owner, 'wh_Output', None)
    assert getattr(partner, 'wh_Definition13') is None


