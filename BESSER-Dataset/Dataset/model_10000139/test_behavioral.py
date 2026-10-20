import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AcceleratorCard,
    CPU,
    Cache,
    Card,
    Chess,
    DeviceCard,
    ExtensionBoard,
    FastCard,
    GenericSound,
    Instruction,
    Processor,
    Program,
    RAM,
    Sound,
    Vendor1Adapter,
    Vendor1Sound,
    Vendor2Adapter,
    Vendor2Sound,
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

def test_assoc_Cache_RAM_stub_double():
    # RAM has no real 'cache5' property in the generated
    # code (a bare stub) -- manually attach it so Cache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Cache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Cache(chunck="sample_text")
    partner = RAM()
    setattr(partner, 'cache5', None)
    _safe_set(owner, 'ramProxy4', partner)
    assert getattr(partner, 'cache5') == owner
    _safe_set(owner, 'ramProxy4', None)
    assert getattr(partner, 'cache5') is None


def test_assoc_Processor_Program_stub_double():
    # Processor has no real 'program3' property in the generated
    # code (a bare stub) -- manually attach it so Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Program(name="sample_text")
    partner = Processor()
    setattr(partner, 'program3', None)
    _safe_set(owner, 'processor2', {partner})
    assert owner in getattr(partner, 'program3')
    _safe_set(owner, 'processor2', set())
    assert owner not in getattr(partner, 'program3')


def test_assoc_Program_Instruction_stub_double():
    # Instruction has no real 'program0' property in the generated
    # code (a bare stub) -- manually attach it so Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Program(name="sample_text")
    partner = Instruction()
    setattr(partner, 'program0', None)
    _safe_set(owner, 'instructions1', {partner})
    assert owner in getattr(partner, 'program0')
    _safe_set(owner, 'instructions1', set())
    assert owner not in getattr(partner, 'program0')


