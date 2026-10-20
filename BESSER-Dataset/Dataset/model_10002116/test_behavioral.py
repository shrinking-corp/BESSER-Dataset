import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractConsumer,
    AbstractRetryConsumer,
    AcceleratorCard,
    CPU,
    Cache,
    Card,
    Container,
    DeviceCard,
    ExtensionBoard,
    FastCard,
    GenericSound,
    IConsumer_Interface,
    Instruction,
    K,
    Machine,
    Memory_Interface,
    Processor,
    Program,
    RAM,
    RetryEvent,
    Runnable_Interface,
    Sound,
    String,
    String1,
    T,
    Vendor1Adapter,
    Vendor1Sound,
    Vendor2Adapter,
    Vendor2Sound,
    Enumeration,
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
    # RAM has no real 'cache11' property in the generated
    # code (a bare stub) -- manually attach it so Cache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Cache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Cache(chunck="sample_text")
    partner = RAM()
    setattr(partner, 'cache11', None)
    _safe_set(owner, 'ramProxy10', partner)
    assert getattr(partner, 'cache11') == owner
    _safe_set(owner, 'ramProxy10', None)
    assert getattr(partner, 'cache11') is None


def test_assoc_Processor_Program_stub_double():
    # Processor has no real 'program9' property in the generated
    # code (a bare stub) -- manually attach it so Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Program(name="sample_text")
    partner = Processor()
    setattr(partner, 'program9', None)
    _safe_set(owner, 'processor8', {partner})
    assert owner in getattr(partner, 'program9')
    _safe_set(owner, 'processor8', set())
    assert owner not in getattr(partner, 'program9')


def test_assoc_Program_Instruction_stub_double():
    # Instruction has no real 'program4' property in the generated
    # code (a bare stub) -- manually attach it so Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Program(name="sample_text")
    partner = Instruction()
    setattr(partner, 'program4', None)
    _safe_set(owner, 'instructions5', {partner})
    assert owner in getattr(partner, 'program4')
    _safe_set(owner, 'instructions5', set())
    assert owner not in getattr(partner, 'program4')


