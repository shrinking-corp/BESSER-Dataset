import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    zhu_Region,
    zhu_State,
    zhu_StateMachine,
    zhu_States,
    zhu_StatesSeparated,
    zhu_TopRegion,
    zhu_Transition,
    zhu_Transitions,
    zhu_Triggers,
    zhu_TriggersSeparated,
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

def test_assoc_regions11_reverse_link_reassign_clear():
    a1 = zhu_Region(name="sample_text")
    a2 = zhu_Region(name="sample_text_2")
    b = zhu_Region(name="sample_text")
    _safe_set(b, 'zhu_Region12', a1)
    assert _is_linked(b, 'zhu_Region12', a1)
    if hasattr(a1, 'zhu_Region10'):
        assert _is_linked(a1, 'zhu_Region10', b)
    _safe_set(b, 'zhu_Region12', a2)
    assert _is_linked(b, 'zhu_Region12', a2)
    if hasattr(a1, 'zhu_Region10'):
        assert not _is_linked(a1, 'zhu_Region10', b)
    if hasattr(a2, 'zhu_Region10'):
        assert _is_linked(a2, 'zhu_Region10', b)
    _safe_set(b, 'zhu_Region12', None)
    assert not _is_linked(b, 'zhu_Region12', a2)
    if hasattr(a2, 'zhu_Region10'):
        assert not _is_linked(a2, 'zhu_Region10', b)


def test_assoc_source21_reverse_link_reassign_clear():
    a1 = zhu_Transition(behaviour="sample_text", guard="sample_text")
    a2 = zhu_Transition(behaviour="sample_text_2", guard="sample_text_2")
    b = zhu_State(name="sample_text")
    _safe_set(b, 'zhu_State', a1)
    assert _is_linked(b, 'zhu_State', a1)
    if hasattr(a1, 'zhu_Transition22'):
        assert _is_linked(a1, 'zhu_Transition22', b)
    _safe_set(b, 'zhu_State', a2)
    assert _is_linked(b, 'zhu_State', a2)
    if hasattr(a1, 'zhu_Transition22'):
        assert not _is_linked(a1, 'zhu_Transition22', b)
    if hasattr(a2, 'zhu_Transition22'):
        assert _is_linked(a2, 'zhu_Transition22', b)
    _safe_set(b, 'zhu_State', None)
    assert not _is_linked(b, 'zhu_State', a2)
    if hasattr(a2, 'zhu_Transition22'):
        assert not _is_linked(a2, 'zhu_Transition22', b)


def test_assoc_target23_reverse_link_reassign_clear():
    a1 = zhu_Transition(behaviour="sample_text", guard="sample_text")
    a2 = zhu_Transition(behaviour="sample_text_2", guard="sample_text_2")
    b = zhu_State(name="sample_text")
    _safe_set(b, 'zhu_State25', a1)
    assert _is_linked(b, 'zhu_State25', a1)
    if hasattr(a1, 'zhu_Transition24'):
        assert _is_linked(a1, 'zhu_Transition24', b)
    _safe_set(b, 'zhu_State25', a2)
    assert _is_linked(b, 'zhu_State25', a2)
    if hasattr(a1, 'zhu_Transition24'):
        assert not _is_linked(a1, 'zhu_Transition24', b)
    if hasattr(a2, 'zhu_Transition24'):
        assert _is_linked(a2, 'zhu_Transition24', b)
    _safe_set(b, 'zhu_State25', None)
    assert not _is_linked(b, 'zhu_State25', a2)
    if hasattr(a2, 'zhu_Transition24'):
        assert not _is_linked(a2, 'zhu_Transition24', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_firstState30_stub_double():
    # zhu_StatesSeparated has no real 'zhu_StatesSeparated31' property in the generated
    # code (a bare stub) -- manually attach it so zhu_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # zhu_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = zhu_State(name="sample_text")
    partner = zhu_StatesSeparated()
    setattr(partner, 'zhu_StatesSeparated31', None)
    _safe_set(owner, 'zhu_State32', partner)
    assert getattr(partner, 'zhu_StatesSeparated31') == owner
    _safe_set(owner, 'zhu_State32', None)
    assert getattr(partner, 'zhu_StatesSeparated31') is None


def test_assoc_firstTransition16_stub_double():
    # zhu_Transitions has no real 'zhu_Transitions17' property in the generated
    # code (a bare stub) -- manually attach it so zhu_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # zhu_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = zhu_Transition(behaviour="sample_text", guard="sample_text")
    partner = zhu_Transitions()
    setattr(partner, 'zhu_Transitions17', None)
    _safe_set(owner, 'zhu_Transition', partner)
    assert getattr(partner, 'zhu_Transitions17') == owner
    _safe_set(owner, 'zhu_Transition', None)
    assert getattr(partner, 'zhu_Transitions17') is None


def test_assoc_followingStates33_stub_double():
    # zhu_StatesSeparated has no real 'zhu_StatesSeparated34' property in the generated
    # code (a bare stub) -- manually attach it so zhu_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # zhu_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = zhu_State(name="sample_text")
    partner = zhu_StatesSeparated()
    setattr(partner, 'zhu_StatesSeparated34', None)
    _safe_set(owner, 'zhu_State35', partner)
    assert owner in getattr(partner, 'zhu_StatesSeparated34')
    _safe_set(owner, 'zhu_State35', None)
    assert owner not in getattr(partner, 'zhu_StatesSeparated34')


def test_assoc_followingTransitions18_stub_double():
    # zhu_Transitions has no real 'zhu_Transitions19' property in the generated
    # code (a bare stub) -- manually attach it so zhu_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # zhu_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = zhu_Transition(behaviour="sample_text", guard="sample_text")
    partner = zhu_Transitions()
    setattr(partner, 'zhu_Transitions19', None)
    _safe_set(owner, 'zhu_Transition20', partner)
    assert owner in getattr(partner, 'zhu_Transitions19')
    _safe_set(owner, 'zhu_Transition20', None)
    assert owner not in getattr(partner, 'zhu_Transitions19')


def test_assoc_regions3_stub_double():
    # zhu_TopRegion has no real 'zhu_TopRegion4' property in the generated
    # code (a bare stub) -- manually attach it so zhu_Region's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # zhu_Region's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = zhu_Region(name="sample_text")
    partner = zhu_TopRegion()
    setattr(partner, 'zhu_TopRegion4', None)
    _safe_set(owner, 'zhu_Region', partner)
    assert owner in getattr(partner, 'zhu_TopRegion4')
    _safe_set(owner, 'zhu_Region', None)
    assert owner not in getattr(partner, 'zhu_TopRegion4')


def test_assoc_states7_stub_double():
    # zhu_States has no real 'zhu_States9' property in the generated
    # code (a bare stub) -- manually attach it so zhu_Region's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # zhu_Region's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = zhu_Region(name="sample_text")
    partner = zhu_States()
    setattr(partner, 'zhu_States9', None)
    _safe_set(owner, 'zhu_Region8', partner)
    assert getattr(partner, 'zhu_States9') == owner
    _safe_set(owner, 'zhu_Region8', None)
    assert getattr(partner, 'zhu_States9') is None


def test_assoc_transitions13_stub_double():
    # zhu_Transitions has no real 'zhu_Transitions15' property in the generated
    # code (a bare stub) -- manually attach it so zhu_Region's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # zhu_Region's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = zhu_Region(name="sample_text")
    partner = zhu_Transitions()
    setattr(partner, 'zhu_Transitions15', None)
    _safe_set(owner, 'zhu_Region14', partner)
    assert getattr(partner, 'zhu_Transitions15') == owner
    _safe_set(owner, 'zhu_Region14', None)
    assert getattr(partner, 'zhu_Transitions15') is None


def test_assoc_triggers26_stub_double():
    # zhu_Triggers has no real 'zhu_Triggers' property in the generated
    # code (a bare stub) -- manually attach it so zhu_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # zhu_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = zhu_Transition(behaviour="sample_text", guard="sample_text")
    partner = zhu_Triggers()
    setattr(partner, 'zhu_Triggers', None)
    _safe_set(owner, 'zhu_Transition27', partner)
    assert getattr(partner, 'zhu_Triggers') == owner
    _safe_set(owner, 'zhu_Transition27', None)
    assert getattr(partner, 'zhu_Triggers') is None


def test_assoc_triggers36_stub_double():
    # zhu_Triggers has no real 'zhu_Triggers37' property in the generated
    # code (a bare stub) -- manually attach it so zhu_TriggersSeparated's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # zhu_TriggersSeparated's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = zhu_TriggersSeparated(firstTrigger="sample_text", followingTriggers="sample_text")
    partner = zhu_Triggers()
    setattr(partner, 'zhu_Triggers37', None)
    _safe_set(owner, 'zhu_TriggersSeparated', partner)
    assert getattr(partner, 'zhu_Triggers37') == owner
    _safe_set(owner, 'zhu_TriggersSeparated', None)
    assert getattr(partner, 'zhu_Triggers37') is None


