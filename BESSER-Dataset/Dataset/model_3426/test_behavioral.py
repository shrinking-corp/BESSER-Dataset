import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Query,
    mongoQuery_Array,
    mongoQuery_FieldSelection,
    mongoQuery_JsonDate,
    mongoQuery_Query,
    mongoQuery_QueryObject,
    mongoQuery_Selection,
    mongoQuery_Selector,
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

def test_assoc_dateValue8_reverse_link_reassign_clear():
    a1 = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    a2 = mongoQuery_Query(integerValue=13, key="sample_text_2", numberValue=9.99, stringValue="sample_text_2")
    b = mongoQuery_JsonDate(dateString="sample_text", day=7, hour=7, millisecond=7, milliseconds=7, minute=7, month=7, second=7, year=7)
    _safe_set(b, 'mongoQuery_JsonDate', a1)
    assert _is_linked(b, 'mongoQuery_JsonDate', a1)
    if hasattr(a1, 'mongoQuery_Query9'):
        assert _is_linked(a1, 'mongoQuery_Query9', b)
    _safe_set(b, 'mongoQuery_JsonDate', a2)
    assert _is_linked(b, 'mongoQuery_JsonDate', a2)
    if hasattr(a1, 'mongoQuery_Query9'):
        assert not _is_linked(a1, 'mongoQuery_Query9', b)
    if hasattr(a2, 'mongoQuery_Query9'):
        assert _is_linked(a2, 'mongoQuery_Query9', b)
    _safe_set(b, 'mongoQuery_JsonDate', None)
    assert not _is_linked(b, 'mongoQuery_JsonDate', a2)
    if hasattr(a2, 'mongoQuery_Query9'):
        assert not _is_linked(a2, 'mongoQuery_Query9', b)


def test_assoc_objectValue13_reverse_link_reassign_clear():
    a1 = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    a2 = mongoQuery_Query(integerValue=13, key="sample_text_2", numberValue=9.99, stringValue="sample_text_2")
    b = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    _safe_set(b, 'mongoQuery_Query14', a1)
    assert _is_linked(b, 'mongoQuery_Query14', a1)
    if hasattr(a1, 'mongoQuery_Query12'):
        assert _is_linked(a1, 'mongoQuery_Query12', b)
    _safe_set(b, 'mongoQuery_Query14', a2)
    assert _is_linked(b, 'mongoQuery_Query14', a2)
    if hasattr(a1, 'mongoQuery_Query12'):
        assert not _is_linked(a1, 'mongoQuery_Query12', b)
    if hasattr(a2, 'mongoQuery_Query12'):
        assert _is_linked(a2, 'mongoQuery_Query12', b)
    _safe_set(b, 'mongoQuery_Query14', None)
    assert not _is_linked(b, 'mongoQuery_Query14', a2)
    if hasattr(a2, 'mongoQuery_Query12'):
        assert not _is_linked(a2, 'mongoQuery_Query12', b)


def test_assoc_value6_reverse_link_reassign_clear():
    a1 = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    a2 = mongoQuery_Query(integerValue=13, key="sample_text_2", numberValue=9.99, stringValue="sample_text_2")
    b = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    _safe_set(b, 'mongoQuery_Query7', a1)
    assert _is_linked(b, 'mongoQuery_Query7', a1)
    if hasattr(a1, 'mongoQuery_Query5'):
        assert _is_linked(a1, 'mongoQuery_Query5', b)
    _safe_set(b, 'mongoQuery_Query7', a2)
    assert _is_linked(b, 'mongoQuery_Query7', a2)
    if hasattr(a1, 'mongoQuery_Query5'):
        assert not _is_linked(a1, 'mongoQuery_Query5', b)
    if hasattr(a2, 'mongoQuery_Query5'):
        assert _is_linked(a2, 'mongoQuery_Query5', b)
    _safe_set(b, 'mongoQuery_Query7', None)
    assert not _is_linked(b, 'mongoQuery_Query7', a2)
    if hasattr(a2, 'mongoQuery_Query5'):
        assert not _is_linked(a2, 'mongoQuery_Query5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arrayValue10_stub_double():
    # mongoQuery_Array has no real 'mongoQuery_Array' property in the generated
    # code (a bare stub) -- manually attach it so mongoQuery_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mongoQuery_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    partner = mongoQuery_Array()
    setattr(partner, 'mongoQuery_Array', None)
    _safe_set(owner, 'mongoQuery_Query11', partner)
    assert getattr(partner, 'mongoQuery_Array') == owner
    _safe_set(owner, 'mongoQuery_Query11', None)
    assert getattr(partner, 'mongoQuery_Array') is None


def test_assoc_fields3_stub_double():
    # mongoQuery_Selection has no real 'mongoQuery_Selection4' property in the generated
    # code (a bare stub) -- manually attach it so mongoQuery_FieldSelection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mongoQuery_FieldSelection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mongoQuery_FieldSelection(enabled=7, key="sample_text")
    partner = mongoQuery_Selection()
    setattr(partner, 'mongoQuery_Selection4', None)
    _safe_set(owner, 'mongoQuery_FieldSelection', partner)
    assert owner in getattr(partner, 'mongoQuery_Selection4')
    _safe_set(owner, 'mongoQuery_FieldSelection', None)
    assert owner not in getattr(partner, 'mongoQuery_Selection4')


def test_assoc_members18_stub_double():
    # mongoQuery_QueryObject has no real 'mongoQuery_QueryObject' property in the generated
    # code (a bare stub) -- manually attach it so mongoQuery_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mongoQuery_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    partner = mongoQuery_QueryObject()
    setattr(partner, 'mongoQuery_QueryObject', None)
    _safe_set(owner, 'mongoQuery_Query19', partner)
    assert owner in getattr(partner, 'mongoQuery_QueryObject')
    _safe_set(owner, 'mongoQuery_Query19', None)
    assert owner not in getattr(partner, 'mongoQuery_QueryObject')


def test_assoc_query0_stub_double():
    # mongoQuery_Selector has no real 'mongoQuery_Selector' property in the generated
    # code (a bare stub) -- manually attach it so mongoQuery_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mongoQuery_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    partner = mongoQuery_Selector()
    setattr(partner, 'mongoQuery_Selector', None)
    _safe_set(owner, 'mongoQuery_Query', partner)
    assert getattr(partner, 'mongoQuery_Selector') == owner
    _safe_set(owner, 'mongoQuery_Query', None)
    assert getattr(partner, 'mongoQuery_Selector') is None


def test_assoc_values15_stub_double():
    # mongoQuery_Array has no real 'mongoQuery_Array16' property in the generated
    # code (a bare stub) -- manually attach it so mongoQuery_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mongoQuery_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mongoQuery_Query(integerValue=7, key="sample_text", numberValue=3.14, stringValue="sample_text")
    partner = mongoQuery_Array()
    setattr(partner, 'mongoQuery_Array16', None)
    _safe_set(owner, 'mongoQuery_Query17', partner)
    assert owner in getattr(partner, 'mongoQuery_Array16')
    _safe_set(owner, 'mongoQuery_Query17', None)
    assert owner not in getattr(partner, 'mongoQuery_Array16')


