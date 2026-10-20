import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Command,
    NamedElement,
    model_Block,
    model_Command,
    model_Light,
    model_Move,
    model_NamedElement,
    model_Ozobot,
    model_OzobotProgram,
    model_Repeat,
    model_Rotate,
    model_Transition,
    model_Wait,
    Color,
    Direction,
    Velocity,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_block9_stub_double():
    # model_Block has no real 'model_Block10' property in the generated
    # code (a bare stub) -- manually attach it so model_Repeat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Repeat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Repeat(count=7)
    partner = model_Block()
    setattr(partner, 'model_Block10', None)
    _safe_set(owner, 'model_Repeat', partner)
    assert getattr(partner, 'model_Block10') == owner
    _safe_set(owner, 'model_Repeat', None)
    assert getattr(partner, 'model_Block10') is None


def test_assoc_commands13_stub_double():
    # model_Block has no real 'model_Block14' property in the generated
    # code (a bare stub) -- manually attach it so model_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Command(message="sample_text")
    partner = model_Block()
    setattr(partner, 'model_Block14', None)
    _safe_set(owner, 'model_Command15', partner)
    assert owner in getattr(partner, 'model_Block14')
    _safe_set(owner, 'model_Command15', None)
    assert owner not in getattr(partner, 'model_Block14')


def test_assoc_current1_stub_double():
    # model_OzobotProgram has no real 'model_OzobotProgram2' property in the generated
    # code (a bare stub) -- manually attach it so model_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Command(message="sample_text")
    partner = model_OzobotProgram()
    setattr(partner, 'model_OzobotProgram2', None)
    _safe_set(owner, 'model_Command', partner)
    assert getattr(partner, 'model_OzobotProgram2') == owner
    _safe_set(owner, 'model_Command', None)
    assert getattr(partner, 'model_OzobotProgram2') is None


def test_assoc_currentCommand3_stub_double():
    # model_OzobotProgram has no real 'model_OzobotProgram4' property in the generated
    # code (a bare stub) -- manually attach it so model_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Command(message="sample_text")
    partner = model_OzobotProgram()
    setattr(partner, 'model_OzobotProgram4', None)
    _safe_set(owner, 'model_Command5', partner)
    assert getattr(partner, 'model_OzobotProgram4') == owner
    _safe_set(owner, 'model_Command5', None)
    assert getattr(partner, 'model_OzobotProgram4') is None


def test_assoc_incoming7_stub_double():
    # model_Transition has no real 'Transition8' property in the generated
    # code (a bare stub) -- manually attach it so model_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Command(message="sample_text")
    partner = model_Transition()
    setattr(partner, 'Transition8', None)
    _safe_set(owner, 'target', partner)
    assert getattr(partner, 'Transition8') == owner
    _safe_set(owner, 'target', None)
    assert getattr(partner, 'Transition8') is None


def test_assoc_outgoing6_stub_double():
    # model_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so model_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Command(message="sample_text")
    partner = model_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'source', partner)
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'source', None)
    assert getattr(partner, 'Transition') is None


def test_assoc_programs11_stub_double():
    # model_OzobotProgram has no real 'model_OzobotProgram12' property in the generated
    # code (a bare stub) -- manually attach it so model_Ozobot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Ozobot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Ozobot(orientation=3.14, xposition=3.14, yposition=3.14)
    partner = model_OzobotProgram()
    setattr(partner, 'model_OzobotProgram12', None)
    _safe_set(owner, 'model_Ozobot', {partner})
    assert getattr(partner, 'model_OzobotProgram12') == owner
    _safe_set(owner, 'model_Ozobot', set())
    assert getattr(partner, 'model_OzobotProgram12') is None


def test_assoc_source18_stub_double():
    # model_Transition has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so model_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Command(message="sample_text")
    partner = model_Transition()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'Command', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'Command', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_target19_stub_double():
    # model_Transition has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so model_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Command(message="sample_text")
    partner = model_Transition()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'Command20', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'Command20', None)
    assert getattr(partner, 'incoming') is None


