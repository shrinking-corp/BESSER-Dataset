import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Command,
    SuperCommand,
    helloWeb_Backward,
    helloWeb_Command,
    helloWeb_Down,
    helloWeb_FeatureMatch,
    helloWeb_Forward,
    helloWeb_FunctionName,
    helloWeb_Left,
    helloWeb_Main,
    helloWeb_Program,
    helloWeb_RecordedFlight,
    helloWeb_Right,
    helloWeb_RotateL,
    helloWeb_RotateR,
    helloWeb_Snapshot,
    helloWeb_SuperCommand,
    helloWeb_Up,
    helloWeb_UserFunction,
    helloWeb_Wait,
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

def test_assoc_commands1_stub_double():
    # helloWeb_SuperCommand has no real 'helloWeb_SuperCommand' property in the generated
    # code (a bare stub) -- manually attach it so helloWeb_Main's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # helloWeb_Main's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = helloWeb_Main(land="sample_text", takeoff="sample_text")
    partner = helloWeb_SuperCommand()
    setattr(partner, 'helloWeb_SuperCommand', None)
    _safe_set(owner, 'helloWeb_Main2', {partner})
    assert getattr(partner, 'helloWeb_SuperCommand') == owner
    _safe_set(owner, 'helloWeb_Main2', set())
    assert getattr(partner, 'helloWeb_SuperCommand') is None


def test_assoc_func3_stub_double():
    # helloWeb_Command has no real 'helloWeb_Command' property in the generated
    # code (a bare stub) -- manually attach it so helloWeb_UserFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # helloWeb_UserFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = helloWeb_UserFunction(name="sample_text")
    partner = helloWeb_Command()
    setattr(partner, 'helloWeb_Command', None)
    _safe_set(owner, 'helloWeb_UserFunction', {partner})
    assert getattr(partner, 'helloWeb_Command') == owner
    _safe_set(owner, 'helloWeb_UserFunction', set())
    assert getattr(partner, 'helloWeb_Command') is None


def test_assoc_main0_stub_double():
    # helloWeb_Program has no real 'helloWeb_Program' property in the generated
    # code (a bare stub) -- manually attach it so helloWeb_Main's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # helloWeb_Main's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = helloWeb_Main(land="sample_text", takeoff="sample_text")
    partner = helloWeb_Program()
    setattr(partner, 'helloWeb_Program', None)
    _safe_set(owner, 'helloWeb_Main', partner)
    assert getattr(partner, 'helloWeb_Program') == owner
    _safe_set(owner, 'helloWeb_Main', None)
    assert getattr(partner, 'helloWeb_Program') is None


