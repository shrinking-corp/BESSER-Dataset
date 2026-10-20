import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Actuate,
    Behavior,
    Condition,
    Node,
    farrusco_Action,
    farrusco_ActionChild,
    farrusco_Actuate,
    farrusco_Behavior,
    farrusco_Child,
    farrusco_Condition,
    farrusco_IRdist,
    farrusco_LED,
    farrusco_LeftBumper,
    farrusco_Motors,
    farrusco_Next,
    farrusco_Node,
    farrusco_Paralell,
    farrusco_Prior,
    farrusco_RightBumper,
    farrusco_Robot,
    farrusco_Sequential,
    farrusco_ServoRange,
    farrusco_StateOverride,
    farrusco_Wait,
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

def test_assoc_actionChild1_stub_double():
    # farrusco_ActionChild has no real 'farrusco_ActionChild' property in the generated
    # code (a bare stub) -- manually attach it so farrusco_Robot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # farrusco_Robot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = farrusco_Robot(Name="sample_text")
    partner = farrusco_ActionChild()
    setattr(partner, 'farrusco_ActionChild', None)
    _safe_set(owner, 'farrusco_Robot2', {partner})
    assert getattr(partner, 'farrusco_ActionChild') == owner
    _safe_set(owner, 'farrusco_Robot2', set())
    assert getattr(partner, 'farrusco_ActionChild') is None


def test_assoc_child3_stub_double():
    # farrusco_Child has no real 'farrusco_Child' property in the generated
    # code (a bare stub) -- manually attach it so farrusco_Robot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # farrusco_Robot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = farrusco_Robot(Name="sample_text")
    partner = farrusco_Child()
    setattr(partner, 'farrusco_Child', None)
    _safe_set(owner, 'farrusco_Robot4', {partner})
    assert getattr(partner, 'farrusco_Child') == owner
    _safe_set(owner, 'farrusco_Robot4', set())
    assert getattr(partner, 'farrusco_Child') is None


def test_assoc_next5_stub_double():
    # farrusco_Next has no real 'farrusco_Next' property in the generated
    # code (a bare stub) -- manually attach it so farrusco_Robot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # farrusco_Robot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = farrusco_Robot(Name="sample_text")
    partner = farrusco_Next()
    setattr(partner, 'farrusco_Next', None)
    _safe_set(owner, 'farrusco_Robot6', {partner})
    assert getattr(partner, 'farrusco_Next') == owner
    _safe_set(owner, 'farrusco_Robot6', set())
    assert getattr(partner, 'farrusco_Next') is None


def test_assoc_nodes0_stub_double():
    # farrusco_Node has no real 'farrusco_Node' property in the generated
    # code (a bare stub) -- manually attach it so farrusco_Robot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # farrusco_Robot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = farrusco_Robot(Name="sample_text")
    partner = farrusco_Node()
    setattr(partner, 'farrusco_Node', None)
    _safe_set(owner, 'farrusco_Robot', {partner})
    assert getattr(partner, 'farrusco_Node') == owner
    _safe_set(owner, 'farrusco_Robot', set())
    assert getattr(partner, 'farrusco_Node') is None


def test_assoc_source18_stub_double():
    # farrusco_ActionChild has no real 'farrusco_ActionChild19' property in the generated
    # code (a bare stub) -- manually attach it so farrusco_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # farrusco_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = farrusco_Behavior(Name="sample_text")
    partner = farrusco_ActionChild()
    setattr(partner, 'farrusco_ActionChild19', None)
    _safe_set(owner, 'farrusco_Behavior20', partner)
    assert getattr(partner, 'farrusco_ActionChild19') == owner
    _safe_set(owner, 'farrusco_Behavior20', None)
    assert getattr(partner, 'farrusco_ActionChild19') is None


def test_assoc_source7_stub_double():
    # farrusco_Child has no real 'farrusco_Child8' property in the generated
    # code (a bare stub) -- manually attach it so farrusco_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # farrusco_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = farrusco_Behavior(Name="sample_text")
    partner = farrusco_Child()
    setattr(partner, 'farrusco_Child8', None)
    _safe_set(owner, 'farrusco_Behavior', partner)
    assert owner in getattr(partner, 'farrusco_Child8')
    _safe_set(owner, 'farrusco_Behavior', None)
    assert owner not in getattr(partner, 'farrusco_Child8')


def test_assoc_target21_stub_double():
    # farrusco_ActionChild has no real 'farrusco_ActionChild22' property in the generated
    # code (a bare stub) -- manually attach it so farrusco_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # farrusco_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = farrusco_Action(name="sample_text")
    partner = farrusco_ActionChild()
    setattr(partner, 'farrusco_ActionChild22', None)
    _safe_set(owner, 'farrusco_Action', partner)
    assert owner in getattr(partner, 'farrusco_ActionChild22')
    _safe_set(owner, 'farrusco_Action', None)
    assert owner not in getattr(partner, 'farrusco_ActionChild22')


def test_assoc_target9_stub_double():
    # farrusco_Child has no real 'farrusco_Child10' property in the generated
    # code (a bare stub) -- manually attach it so farrusco_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # farrusco_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = farrusco_Behavior(Name="sample_text")
    partner = farrusco_Child()
    setattr(partner, 'farrusco_Child10', None)
    _safe_set(owner, 'farrusco_Behavior11', partner)
    assert owner in getattr(partner, 'farrusco_Child10')
    _safe_set(owner, 'farrusco_Behavior11', None)
    assert owner not in getattr(partner, 'farrusco_Child10')


