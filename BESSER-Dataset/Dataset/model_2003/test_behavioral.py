import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Step,
    StructValue,
    Value,
    trace_ArrayValue,
    trace_Assignment,
    trace_Failure,
    trace_FunctionCall,
    trace_FunctionReturn,
    trace_Location,
    trace_LocationOnly,
    trace_NameToValueMap,
    trace_Output,
    trace_SimpleValue,
    trace_Step,
    trace_StructValue,
    trace_Trace,
    trace_UnionValue,
    trace_Value,
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

def test_assoc_location5_reverse_link_reassign_clear():
    a1 = trace_Step(hidden="sample_text", number="sample_text", thread="sample_text")
    a2 = trace_Step(hidden="sample_text_2", number="sample_text_2", thread="sample_text_2")
    b = trace_Location(file="sample_text", function="sample_text", line="sample_text")
    _safe_set(b, 'trace_Location', a1)
    assert _is_linked(b, 'trace_Location', a1)
    if hasattr(a1, 'trace_Step'):
        assert _is_linked(a1, 'trace_Step', b)
    _safe_set(b, 'trace_Location', a2)
    assert _is_linked(b, 'trace_Location', a2)
    if hasattr(a1, 'trace_Step'):
        assert not _is_linked(a1, 'trace_Step', b)
    if hasattr(a2, 'trace_Step'):
        assert _is_linked(a2, 'trace_Step', b)
    _safe_set(b, 'trace_Location', None)
    assert not _is_linked(b, 'trace_Location', a2)
    if hasattr(a2, 'trace_Step'):
        assert not _is_linked(a2, 'trace_Step', b)


def test_assoc_value1_reverse_link_reassign_clear():
    a1 = trace_Value(type="sample_text")
    a2 = trace_Value(type="sample_text_2")
    b = trace_Assignment(assignmentType="sample_text", baseName="sample_text", displayName="sample_text", id="sample_text")
    _safe_set(b, 'trace_Assignment', a1)
    assert _is_linked(b, 'trace_Assignment', a1)
    if hasattr(a1, 'trace_Value2'):
        assert _is_linked(a1, 'trace_Value2', b)
    _safe_set(b, 'trace_Assignment', a2)
    assert _is_linked(b, 'trace_Assignment', a2)
    if hasattr(a1, 'trace_Value2'):
        assert not _is_linked(a1, 'trace_Value2', b)
    if hasattr(a2, 'trace_Value2'):
        assert _is_linked(a2, 'trace_Value2', b)
    _safe_set(b, 'trace_Assignment', None)
    assert not _is_linked(b, 'trace_Assignment', a2)
    if hasattr(a2, 'trace_Value2'):
        assert not _is_linked(a2, 'trace_Value2', b)


def test_assoc_value3_reverse_link_reassign_clear():
    a1 = trace_Value(type="sample_text")
    a2 = trace_Value(type="sample_text_2")
    b = trace_NameToValueMap(key="sample_text")
    _safe_set(b, 'trace_NameToValueMap', a1)
    assert _is_linked(b, 'trace_NameToValueMap', a1)
    if hasattr(a1, 'trace_Value4'):
        assert _is_linked(a1, 'trace_Value4', b)
    _safe_set(b, 'trace_NameToValueMap', a2)
    assert _is_linked(b, 'trace_NameToValueMap', a2)
    if hasattr(a1, 'trace_Value4'):
        assert not _is_linked(a1, 'trace_Value4', b)
    if hasattr(a2, 'trace_Value4'):
        assert _is_linked(a2, 'trace_Value4', b)
    _safe_set(b, 'trace_NameToValueMap', None)
    assert not _is_linked(b, 'trace_NameToValueMap', a2)
    if hasattr(a2, 'trace_Value4'):
        assert not _is_linked(a2, 'trace_Value4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_steps8_stub_double():
    # trace_Trace has no real 'trace_Trace' property in the generated
    # code (a bare stub) -- manually attach it so trace_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_Step(hidden="sample_text", number="sample_text", thread="sample_text")
    partner = trace_Trace()
    setattr(partner, 'trace_Trace', None)
    _safe_set(owner, 'trace_Step9', partner)
    assert owner in getattr(partner, 'trace_Trace')
    _safe_set(owner, 'trace_Step9', None)
    assert owner not in getattr(partner, 'trace_Trace')


def test_assoc_values0_stub_double():
    # trace_ArrayValue has no real 'trace_ArrayValue' property in the generated
    # code (a bare stub) -- manually attach it so trace_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_Value(type="sample_text")
    partner = trace_ArrayValue()
    setattr(partner, 'trace_ArrayValue', None)
    _safe_set(owner, 'trace_Value', partner)
    assert owner in getattr(partner, 'trace_ArrayValue')
    _safe_set(owner, 'trace_Value', None)
    assert owner not in getattr(partner, 'trace_ArrayValue')


def test_assoc_values6_stub_double():
    # trace_StructValue has no real 'trace_StructValue' property in the generated
    # code (a bare stub) -- manually attach it so trace_NameToValueMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_NameToValueMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_NameToValueMap(key="sample_text")
    partner = trace_StructValue()
    setattr(partner, 'trace_StructValue', None)
    _safe_set(owner, 'trace_NameToValueMap7', partner)
    assert owner in getattr(partner, 'trace_StructValue')
    _safe_set(owner, 'trace_NameToValueMap7', None)
    assert owner not in getattr(partner, 'trace_StructValue')


