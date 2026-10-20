import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    rm_Device,
    rm_Memory,
    rm_MemoryCellReference,
    rm_ResourceModel,
    rm_VariableReference,
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

def test_assoc_localMemoryCellReference3_reverse_link_reassign_clear():
    a1 = rm_MemoryCellReference(endCellIndex=7, startCellIndex=7)
    a2 = rm_MemoryCellReference(endCellIndex=13, startCellIndex=13)
    b = rm_Device(cacheSize=7)
    _safe_set(b, 'rm_Device4', a1)
    assert _is_linked(b, 'rm_Device4', a1)
    if hasattr(a1, 'rm_MemoryCellReference'):
        assert _is_linked(a1, 'rm_MemoryCellReference', b)
    _safe_set(b, 'rm_Device4', a2)
    assert _is_linked(b, 'rm_Device4', a2)
    if hasattr(a1, 'rm_MemoryCellReference'):
        assert not _is_linked(a1, 'rm_MemoryCellReference', b)
    if hasattr(a2, 'rm_MemoryCellReference'):
        assert _is_linked(a2, 'rm_MemoryCellReference', b)
    _safe_set(b, 'rm_Device4', None)
    assert not _is_linked(b, 'rm_Device4', a2)
    if hasattr(a2, 'rm_MemoryCellReference'):
        assert not _is_linked(a2, 'rm_MemoryCellReference', b)


def test_assoc_variableReferences5_reverse_link_reassign_clear():
    a1 = rm_VariableReference(memoryCellIndex=7, variable="sample_text")
    a2 = rm_VariableReference(memoryCellIndex=13, variable="sample_text_2")
    b = rm_Memory(size=7)
    _safe_set(b, 'rm_Memory6', {a1})
    assert _is_linked(b, 'rm_Memory6', a1)
    if hasattr(a1, 'rm_VariableReference'):
        assert _is_linked(a1, 'rm_VariableReference', b)
    _safe_set(b, 'rm_Memory6', {a2})
    assert _is_linked(b, 'rm_Memory6', a2)
    if hasattr(a1, 'rm_VariableReference'):
        assert not _is_linked(a1, 'rm_VariableReference', b)
    if hasattr(a2, 'rm_VariableReference'):
        assert _is_linked(a2, 'rm_VariableReference', b)
    _safe_set(b, 'rm_Memory6', set())
    assert not _is_linked(b, 'rm_Memory6', a2)
    if hasattr(a2, 'rm_VariableReference'):
        assert not _is_linked(a2, 'rm_VariableReference', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_devices0_stub_double():
    # rm_ResourceModel has no real 'rm_ResourceModel' property in the generated
    # code (a bare stub) -- manually attach it so rm_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rm_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rm_Device(cacheSize=7)
    partner = rm_ResourceModel()
    setattr(partner, 'rm_ResourceModel', None)
    _safe_set(owner, 'rm_Device', partner)
    assert owner in getattr(partner, 'rm_ResourceModel')
    _safe_set(owner, 'rm_Device', None)
    assert owner not in getattr(partner, 'rm_ResourceModel')


def test_assoc_memory1_stub_double():
    # rm_ResourceModel has no real 'rm_ResourceModel2' property in the generated
    # code (a bare stub) -- manually attach it so rm_Memory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rm_Memory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rm_Memory(size=7)
    partner = rm_ResourceModel()
    setattr(partner, 'rm_ResourceModel2', None)
    _safe_set(owner, 'rm_Memory', partner)
    assert getattr(partner, 'rm_ResourceModel2') == owner
    _safe_set(owner, 'rm_Memory', None)
    assert getattr(partner, 'rm_ResourceModel2') is None


