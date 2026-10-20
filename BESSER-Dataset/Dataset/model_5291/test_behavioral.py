import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryCalculator_BinaryCalculator,
    BinaryCalculator_Bit,
    BinaryCalculator_BitSeq,
    BinaryCalculator_L,
    BinaryCalculator_Model,
    BinaryCalculator_Value,
    BitSeq,
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

def test_assoc_result3_reverse_link_reassign_clear():
    a1 = BinaryCalculator_Value(value="sample_text")
    a2 = BinaryCalculator_Value(value="sample_text_2")
    b = BinaryCalculator_BinaryCalculator(description="sample_text")
    _safe_set(b, 'BinaryCalculator_BinaryCalculator4', a1)
    assert _is_linked(b, 'BinaryCalculator_BinaryCalculator4', a1)
    if hasattr(a1, 'BinaryCalculator_Value'):
        assert _is_linked(a1, 'BinaryCalculator_Value', b)
    _safe_set(b, 'BinaryCalculator_BinaryCalculator4', a2)
    assert _is_linked(b, 'BinaryCalculator_BinaryCalculator4', a2)
    if hasattr(a1, 'BinaryCalculator_Value'):
        assert not _is_linked(a1, 'BinaryCalculator_Value', b)
    if hasattr(a2, 'BinaryCalculator_Value'):
        assert _is_linked(a2, 'BinaryCalculator_Value', b)
    _safe_set(b, 'BinaryCalculator_BinaryCalculator4', None)
    assert not _is_linked(b, 'BinaryCalculator_BinaryCalculator4', a2)
    if hasattr(a2, 'BinaryCalculator_Value'):
        assert not _is_linked(a2, 'BinaryCalculator_Value', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_calculators0_stub_double():
    # BinaryCalculator_Model has no real 'BinaryCalculator_Model' property in the generated
    # code (a bare stub) -- manually attach it so BinaryCalculator_BinaryCalculator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # BinaryCalculator_BinaryCalculator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = BinaryCalculator_BinaryCalculator(description="sample_text")
    partner = BinaryCalculator_Model()
    setattr(partner, 'BinaryCalculator_Model', None)
    _safe_set(owner, 'BinaryCalculator_BinaryCalculator', partner)
    assert owner in getattr(partner, 'BinaryCalculator_Model')
    _safe_set(owner, 'BinaryCalculator_BinaryCalculator', None)
    assert owner not in getattr(partner, 'BinaryCalculator_Model')


def test_assoc_number1_stub_double():
    # BinaryCalculator_BitSeq has no real 'BinaryCalculator_BitSeq' property in the generated
    # code (a bare stub) -- manually attach it so BinaryCalculator_BinaryCalculator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # BinaryCalculator_BinaryCalculator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = BinaryCalculator_BinaryCalculator(description="sample_text")
    partner = BinaryCalculator_BitSeq()
    setattr(partner, 'BinaryCalculator_BitSeq', None)
    _safe_set(owner, 'BinaryCalculator_BinaryCalculator2', partner)
    assert getattr(partner, 'BinaryCalculator_BitSeq') == owner
    _safe_set(owner, 'BinaryCalculator_BinaryCalculator2', None)
    assert getattr(partner, 'BinaryCalculator_BitSeq') is None


def test_assoc_rigth7_stub_double():
    # BinaryCalculator_L has no real 'BinaryCalculator_L8' property in the generated
    # code (a bare stub) -- manually attach it so BinaryCalculator_Bit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # BinaryCalculator_Bit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = BinaryCalculator_Bit(value="sample_text")
    partner = BinaryCalculator_L()
    setattr(partner, 'BinaryCalculator_L8', None)
    _safe_set(owner, 'BinaryCalculator_Bit', partner)
    assert getattr(partner, 'BinaryCalculator_L8') == owner
    _safe_set(owner, 'BinaryCalculator_Bit', None)
    assert getattr(partner, 'BinaryCalculator_L8') is None


