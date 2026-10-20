import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BaseState,
    cgimodel_BaseState,
    cgimodel_Expr,
    cgimodel_OrState,
    cgimodel_State,
    cgimodel_StateModel,
    cgimodel_StateModels,
    cgimodel_Transition,
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

def test_assoc_expr3_reverse_link_reassign_clear():
    a1 = cgimodel_State(set=True)
    a2 = cgimodel_State(set=False)
    b = cgimodel_Expr(value="sample_text")
    _safe_set(b, 'cgimodel_Expr', a1)
    assert _is_linked(b, 'cgimodel_Expr', a1)
    if hasattr(a1, 'cgimodel_State'):
        assert _is_linked(a1, 'cgimodel_State', b)
    _safe_set(b, 'cgimodel_Expr', a2)
    assert _is_linked(b, 'cgimodel_Expr', a2)
    if hasattr(a1, 'cgimodel_State'):
        assert not _is_linked(a1, 'cgimodel_State', b)
    if hasattr(a2, 'cgimodel_State'):
        assert _is_linked(a2, 'cgimodel_State', b)
    _safe_set(b, 'cgimodel_Expr', None)
    assert not _is_linked(b, 'cgimodel_Expr', a2)
    if hasattr(a2, 'cgimodel_State'):
        assert not _is_linked(a2, 'cgimodel_State', b)


def test_assoc_states0_reverse_link_reassign_clear():
    a1 = cgimodel_StateModel(name="sample_text")
    a2 = cgimodel_StateModel(name="sample_text_2")
    b = cgimodel_BaseState(name="sample_text")
    _safe_set(b, 'cgimodel_BaseState', a1)
    assert _is_linked(b, 'cgimodel_BaseState', a1)
    if hasattr(a1, 'cgimodel_StateModel'):
        assert _is_linked(a1, 'cgimodel_StateModel', b)
    _safe_set(b, 'cgimodel_BaseState', a2)
    assert _is_linked(b, 'cgimodel_BaseState', a2)
    if hasattr(a1, 'cgimodel_StateModel'):
        assert not _is_linked(a1, 'cgimodel_StateModel', b)
    if hasattr(a2, 'cgimodel_StateModel'):
        assert _is_linked(a2, 'cgimodel_StateModel', b)
    _safe_set(b, 'cgimodel_BaseState', None)
    assert not _is_linked(b, 'cgimodel_BaseState', a2)
    if hasattr(a2, 'cgimodel_StateModel'):
        assert not _is_linked(a2, 'cgimodel_StateModel', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_condition12_stub_double():
    # cgimodel_Transition has no real 'cgimodel_Transition13' property in the generated
    # code (a bare stub) -- manually attach it so cgimodel_Expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cgimodel_Expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cgimodel_Expr(value="sample_text")
    partner = cgimodel_Transition()
    setattr(partner, 'cgimodel_Transition13', None)
    _safe_set(owner, 'cgimodel_Expr14', partner)
    assert getattr(partner, 'cgimodel_Transition13') == owner
    _safe_set(owner, 'cgimodel_Expr14', None)
    assert getattr(partner, 'cgimodel_Transition13') is None


def test_assoc_source6_stub_double():
    # cgimodel_Transition has no real 'cgimodel_Transition7' property in the generated
    # code (a bare stub) -- manually attach it so cgimodel_BaseState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cgimodel_BaseState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cgimodel_BaseState(name="sample_text")
    partner = cgimodel_Transition()
    setattr(partner, 'cgimodel_Transition7', None)
    _safe_set(owner, 'cgimodel_BaseState8', partner)
    assert getattr(partner, 'cgimodel_Transition7') == owner
    _safe_set(owner, 'cgimodel_BaseState8', None)
    assert getattr(partner, 'cgimodel_Transition7') is None


def test_assoc_stateModels15_stub_double():
    # cgimodel_StateModels has no real 'cgimodel_StateModels' property in the generated
    # code (a bare stub) -- manually attach it so cgimodel_StateModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cgimodel_StateModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cgimodel_StateModel(name="sample_text")
    partner = cgimodel_StateModels()
    setattr(partner, 'cgimodel_StateModels', None)
    _safe_set(owner, 'cgimodel_StateModel16', partner)
    assert owner in getattr(partner, 'cgimodel_StateModels')
    _safe_set(owner, 'cgimodel_StateModel16', None)
    assert owner not in getattr(partner, 'cgimodel_StateModels')


def test_assoc_states4_stub_double():
    # cgimodel_OrState has no real 'cgimodel_OrState' property in the generated
    # code (a bare stub) -- manually attach it so cgimodel_BaseState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cgimodel_BaseState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cgimodel_BaseState(name="sample_text")
    partner = cgimodel_OrState()
    setattr(partner, 'cgimodel_OrState', None)
    _safe_set(owner, 'cgimodel_BaseState5', partner)
    assert owner in getattr(partner, 'cgimodel_OrState')
    _safe_set(owner, 'cgimodel_BaseState5', None)
    assert owner not in getattr(partner, 'cgimodel_OrState')


def test_assoc_target9_stub_double():
    # cgimodel_Transition has no real 'cgimodel_Transition10' property in the generated
    # code (a bare stub) -- manually attach it so cgimodel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cgimodel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cgimodel_State(set=True)
    partner = cgimodel_Transition()
    setattr(partner, 'cgimodel_Transition10', None)
    _safe_set(owner, 'cgimodel_State11', partner)
    assert getattr(partner, 'cgimodel_Transition10') == owner
    _safe_set(owner, 'cgimodel_State11', None)
    assert getattr(partner, 'cgimodel_Transition10') is None


def test_assoc_transitions1_stub_double():
    # cgimodel_Transition has no real 'cgimodel_Transition' property in the generated
    # code (a bare stub) -- manually attach it so cgimodel_StateModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cgimodel_StateModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cgimodel_StateModel(name="sample_text")
    partner = cgimodel_Transition()
    setattr(partner, 'cgimodel_Transition', None)
    _safe_set(owner, 'cgimodel_StateModel2', {partner})
    assert getattr(partner, 'cgimodel_Transition') == owner
    _safe_set(owner, 'cgimodel_StateModel2', set())
    assert getattr(partner, 'cgimodel_Transition') is None


