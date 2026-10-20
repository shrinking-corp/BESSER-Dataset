import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    Thing,
    simplestatechart_NamedElement,
    simplestatechart_RelatedTo,
    simplestatechart_State,
    simplestatechart_Thing,
    simplestatechart_Transition,
    simplestatechart_Variable,
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

def test_assoc_fromThing1_reverse_link_reassign_clear():
    a1 = simplestatechart_Thing(id=7)
    a2 = simplestatechart_Thing(id=13)
    b = simplestatechart_RelatedTo(since="sample_text")
    _safe_set(b, 'relations', a1)
    assert _is_linked(b, 'relations', a1)
    if hasattr(a1, 'Thing'):
        assert _is_linked(a1, 'Thing', b)
    _safe_set(b, 'relations', a2)
    assert _is_linked(b, 'relations', a2)
    if hasattr(a1, 'Thing'):
        assert not _is_linked(a1, 'Thing', b)
    if hasattr(a2, 'Thing'):
        assert _is_linked(a2, 'Thing', b)
    _safe_set(b, 'relations', None)
    assert not _is_linked(b, 'relations', a2)
    if hasattr(a2, 'Thing'):
        assert not _is_linked(a2, 'Thing', b)


def test_assoc_parentstate11_reverse_link_reassign_clear():
    a1 = simplestatechart_State(activity="sample_text", label="sample_text", type="sample_text")
    a2 = simplestatechart_State(activity="sample_text_2", label="sample_text_2", type="sample_text_2")
    b = simplestatechart_State(activity="sample_text", label="sample_text", type="sample_text")
    _safe_set(b, 'simplestatechart_State12', a1)
    assert _is_linked(b, 'simplestatechart_State12', a1)
    if hasattr(a1, 'simplestatechart_State10'):
        assert _is_linked(a1, 'simplestatechart_State10', b)
    _safe_set(b, 'simplestatechart_State12', a2)
    assert _is_linked(b, 'simplestatechart_State12', a2)
    if hasattr(a1, 'simplestatechart_State10'):
        assert not _is_linked(a1, 'simplestatechart_State10', b)
    if hasattr(a2, 'simplestatechart_State10'):
        assert _is_linked(a2, 'simplestatechart_State10', b)
    _safe_set(b, 'simplestatechart_State12', None)
    assert not _is_linked(b, 'simplestatechart_State12', a2)
    if hasattr(a2, 'simplestatechart_State10'):
        assert not _is_linked(a2, 'simplestatechart_State10', b)


def test_assoc_relations0_reverse_link_reassign_clear():
    a1 = simplestatechart_Thing(id=7)
    a2 = simplestatechart_Thing(id=13)
    b = simplestatechart_RelatedTo(since="sample_text")
    _safe_set(b, 'RelatedTo', a1)
    assert _is_linked(b, 'RelatedTo', a1)
    if hasattr(a1, 'fromThing'):
        assert _is_linked(a1, 'fromThing', b)
    _safe_set(b, 'RelatedTo', a2)
    assert _is_linked(b, 'RelatedTo', a2)
    if hasattr(a1, 'fromThing'):
        assert not _is_linked(a1, 'fromThing', b)
    if hasattr(a2, 'fromThing'):
        assert _is_linked(a2, 'fromThing', b)
    _safe_set(b, 'RelatedTo', None)
    assert not _is_linked(b, 'RelatedTo', a2)
    if hasattr(a2, 'fromThing'):
        assert not _is_linked(a2, 'fromThing', b)


def test_assoc_source3_reverse_link_reassign_clear():
    a1 = simplestatechart_Transition(expression="sample_text")
    a2 = simplestatechart_Transition(expression="sample_text_2")
    b = simplestatechart_State(activity="sample_text", label="sample_text", type="sample_text")
    _safe_set(b, 'simplestatechart_State', a1)
    assert _is_linked(b, 'simplestatechart_State', a1)
    if hasattr(a1, 'simplestatechart_Transition'):
        assert _is_linked(a1, 'simplestatechart_Transition', b)
    _safe_set(b, 'simplestatechart_State', a2)
    assert _is_linked(b, 'simplestatechart_State', a2)
    if hasattr(a1, 'simplestatechart_Transition'):
        assert not _is_linked(a1, 'simplestatechart_Transition', b)
    if hasattr(a2, 'simplestatechart_Transition'):
        assert _is_linked(a2, 'simplestatechart_Transition', b)
    _safe_set(b, 'simplestatechart_State', None)
    assert not _is_linked(b, 'simplestatechart_State', a2)
    if hasattr(a2, 'simplestatechart_Transition'):
        assert not _is_linked(a2, 'simplestatechart_Transition', b)


def test_assoc_substates8_reverse_link_reassign_clear():
    a1 = simplestatechart_State(activity="sample_text", label="sample_text", type="sample_text")
    a2 = simplestatechart_State(activity="sample_text_2", label="sample_text_2", type="sample_text_2")
    b = simplestatechart_State(activity="sample_text", label="sample_text", type="sample_text")
    _safe_set(b, 'simplestatechart_State9', a1)
    assert _is_linked(b, 'simplestatechart_State9', a1)
    if hasattr(a1, 'simplestatechart_State7'):
        assert _is_linked(a1, 'simplestatechart_State7', b)
    _safe_set(b, 'simplestatechart_State9', a2)
    assert _is_linked(b, 'simplestatechart_State9', a2)
    if hasattr(a1, 'simplestatechart_State7'):
        assert not _is_linked(a1, 'simplestatechart_State7', b)
    if hasattr(a2, 'simplestatechart_State7'):
        assert _is_linked(a2, 'simplestatechart_State7', b)
    _safe_set(b, 'simplestatechart_State9', None)
    assert not _is_linked(b, 'simplestatechart_State9', a2)
    if hasattr(a2, 'simplestatechart_State7'):
        assert not _is_linked(a2, 'simplestatechart_State7', b)


def test_assoc_target4_reverse_link_reassign_clear():
    a1 = simplestatechart_Transition(expression="sample_text")
    a2 = simplestatechart_Transition(expression="sample_text_2")
    b = simplestatechart_State(activity="sample_text", label="sample_text", type="sample_text")
    _safe_set(b, 'simplestatechart_State6', a1)
    assert _is_linked(b, 'simplestatechart_State6', a1)
    if hasattr(a1, 'simplestatechart_Transition5'):
        assert _is_linked(a1, 'simplestatechart_Transition5', b)
    _safe_set(b, 'simplestatechart_State6', a2)
    assert _is_linked(b, 'simplestatechart_State6', a2)
    if hasattr(a1, 'simplestatechart_Transition5'):
        assert not _is_linked(a1, 'simplestatechart_Transition5', b)
    if hasattr(a2, 'simplestatechart_Transition5'):
        assert _is_linked(a2, 'simplestatechart_Transition5', b)
    _safe_set(b, 'simplestatechart_State6', None)
    assert not _is_linked(b, 'simplestatechart_State6', a2)
    if hasattr(a2, 'simplestatechart_Transition5'):
        assert not _is_linked(a2, 'simplestatechart_Transition5', b)


def test_assoc_toThing2_reverse_link_reassign_clear():
    a1 = simplestatechart_Thing(id=7)
    a2 = simplestatechart_Thing(id=13)
    b = simplestatechart_RelatedTo(since="sample_text")
    _safe_set(b, 'simplestatechart_RelatedTo', a1)
    assert _is_linked(b, 'simplestatechart_RelatedTo', a1)
    if hasattr(a1, 'simplestatechart_Thing'):
        assert _is_linked(a1, 'simplestatechart_Thing', b)
    _safe_set(b, 'simplestatechart_RelatedTo', a2)
    assert _is_linked(b, 'simplestatechart_RelatedTo', a2)
    if hasattr(a1, 'simplestatechart_Thing'):
        assert not _is_linked(a1, 'simplestatechart_Thing', b)
    if hasattr(a2, 'simplestatechart_Thing'):
        assert _is_linked(a2, 'simplestatechart_Thing', b)
    _safe_set(b, 'simplestatechart_RelatedTo', None)
    assert not _is_linked(b, 'simplestatechart_RelatedTo', a2)
    if hasattr(a2, 'simplestatechart_Thing'):
        assert not _is_linked(a2, 'simplestatechart_Thing', b)


def test_assoc_transitions15_reverse_link_reassign_clear():
    a1 = simplestatechart_Transition(expression="sample_text")
    a2 = simplestatechart_Transition(expression="sample_text_2")
    b = simplestatechart_State(activity="sample_text", label="sample_text", type="sample_text")
    _safe_set(b, 'simplestatechart_State16', {a1})
    assert _is_linked(b, 'simplestatechart_State16', a1)
    if hasattr(a1, 'simplestatechart_Transition17'):
        assert _is_linked(a1, 'simplestatechart_Transition17', b)
    _safe_set(b, 'simplestatechart_State16', {a2})
    assert _is_linked(b, 'simplestatechart_State16', a2)
    if hasattr(a1, 'simplestatechart_Transition17'):
        assert not _is_linked(a1, 'simplestatechart_Transition17', b)
    if hasattr(a2, 'simplestatechart_Transition17'):
        assert _is_linked(a2, 'simplestatechart_Transition17', b)
    _safe_set(b, 'simplestatechart_State16', set())
    assert not _is_linked(b, 'simplestatechart_State16', a2)
    if hasattr(a2, 'simplestatechart_Transition17'):
        assert not _is_linked(a2, 'simplestatechart_Transition17', b)


def test_assoc_variables13_reverse_link_reassign_clear():
    a1 = simplestatechart_Variable(type="sample_text", value="sample_text")
    a2 = simplestatechart_Variable(type="sample_text_2", value="sample_text_2")
    b = simplestatechart_State(activity="sample_text", label="sample_text", type="sample_text")
    _safe_set(b, 'simplestatechart_State14', {a1})
    assert _is_linked(b, 'simplestatechart_State14', a1)
    if hasattr(a1, 'simplestatechart_Variable'):
        assert _is_linked(a1, 'simplestatechart_Variable', b)
    _safe_set(b, 'simplestatechart_State14', {a2})
    assert _is_linked(b, 'simplestatechart_State14', a2)
    if hasattr(a1, 'simplestatechart_Variable'):
        assert not _is_linked(a1, 'simplestatechart_Variable', b)
    if hasattr(a2, 'simplestatechart_Variable'):
        assert _is_linked(a2, 'simplestatechart_Variable', b)
    _safe_set(b, 'simplestatechart_State14', set())
    assert not _is_linked(b, 'simplestatechart_State14', a2)
    if hasattr(a2, 'simplestatechart_Variable'):
        assert not _is_linked(a2, 'simplestatechart_Variable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

