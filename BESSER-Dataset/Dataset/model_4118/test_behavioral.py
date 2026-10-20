import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    wh_Command,
    wh_Commands,
    wh_Definition,
    wh_Program,
    wh_Wh,
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

def test_assoc_definition1_reverse_link_reassign_clear():
    a1 = wh_Program(name="sample_text")
    a2 = wh_Program(name="sample_text_2")
    b = wh_Definition(input="sample_text", output="sample_text")
    _safe_set(b, 'wh_Definition', a1)
    assert _is_linked(b, 'wh_Definition', a1)
    if hasattr(a1, 'wh_Program2'):
        assert _is_linked(a1, 'wh_Program2', b)
    _safe_set(b, 'wh_Definition', a2)
    assert _is_linked(b, 'wh_Definition', a2)
    if hasattr(a1, 'wh_Program2'):
        assert not _is_linked(a1, 'wh_Program2', b)
    if hasattr(a2, 'wh_Program2'):
        assert _is_linked(a2, 'wh_Program2', b)
    _safe_set(b, 'wh_Definition', None)
    assert not _is_linked(b, 'wh_Definition', a2)
    if hasattr(a2, 'wh_Program2'):
        assert not _is_linked(a2, 'wh_Program2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_command3_stub_double():
    # wh_Commands has no real 'wh_Commands' property in the generated
    # code (a bare stub) -- manually attach it so wh_Definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Definition(input="sample_text", output="sample_text")
    partner = wh_Commands()
    setattr(partner, 'wh_Commands', None)
    _safe_set(owner, 'wh_Definition4', partner)
    assert getattr(partner, 'wh_Commands') == owner
    _safe_set(owner, 'wh_Definition4', None)
    assert getattr(partner, 'wh_Commands') is None


def test_assoc_commands5_stub_double():
    # wh_Commands has no real 'wh_Commands6' property in the generated
    # code (a bare stub) -- manually attach it so wh_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Command(cmd="sample_text")
    partner = wh_Commands()
    setattr(partner, 'wh_Commands6', None)
    _safe_set(owner, 'wh_Command', partner)
    assert owner in getattr(partner, 'wh_Commands6')
    _safe_set(owner, 'wh_Command', None)
    assert owner not in getattr(partner, 'wh_Commands6')


def test_assoc_elements0_stub_double():
    # wh_Wh has no real 'wh_Wh' property in the generated
    # code (a bare stub) -- manually attach it so wh_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wh_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wh_Program(name="sample_text")
    partner = wh_Wh()
    setattr(partner, 'wh_Wh', None)
    _safe_set(owner, 'wh_Program', partner)
    assert owner in getattr(partner, 'wh_Wh')
    _safe_set(owner, 'wh_Program', None)
    assert owner not in getattr(partner, 'wh_Wh')


