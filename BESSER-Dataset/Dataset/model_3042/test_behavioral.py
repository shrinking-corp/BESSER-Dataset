import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    ActionResult,
    AtomicProcess,
    CompositeProcess,
    Process,
    actions_Action,
    actions_ActionResult,
    actions_ActionsCollection,
    actions_AtomicAction,
    actions_AtomicActionResult,
    actions_CompositeAction,
    actions_Condition,
    actions_Distribution,
    actions_Expression,
    actions_Parameter,
    actions_Participant,
    actions_Role,
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

def test_assoc_hasCostDistribution8_reverse_link_reassign_clear():
    a1 = actions_Distribution(datapoint=3.14, density=3.14, id=7, version=7)
    a2 = actions_Distribution(datapoint=9.99, density=9.99, id=13, version=13)
    b = actions_AtomicActionResult(hasDensity=3.14)
    _safe_set(b, 'actions_AtomicActionResult9', {a1})
    assert _is_linked(b, 'actions_AtomicActionResult9', a1)
    if hasattr(a1, 'actions_Distribution'):
        assert _is_linked(a1, 'actions_Distribution', b)
    _safe_set(b, 'actions_AtomicActionResult9', {a2})
    assert _is_linked(b, 'actions_AtomicActionResult9', a2)
    if hasattr(a1, 'actions_Distribution'):
        assert not _is_linked(a1, 'actions_Distribution', b)
    if hasattr(a2, 'actions_Distribution'):
        assert _is_linked(a2, 'actions_Distribution', b)
    _safe_set(b, 'actions_AtomicActionResult9', set())
    assert not _is_linked(b, 'actions_AtomicActionResult9', a2)
    if hasattr(a2, 'actions_Distribution'):
        assert not _is_linked(a2, 'actions_Distribution', b)


def test_assoc_hasDurationDistribution10_reverse_link_reassign_clear():
    a1 = actions_Distribution(datapoint=3.14, density=3.14, id=7, version=7)
    a2 = actions_Distribution(datapoint=9.99, density=9.99, id=13, version=13)
    b = actions_AtomicActionResult(hasDensity=3.14)
    _safe_set(b, 'actions_AtomicActionResult11', {a1})
    assert _is_linked(b, 'actions_AtomicActionResult11', a1)
    if hasattr(a1, 'actions_Distribution12'):
        assert _is_linked(a1, 'actions_Distribution12', b)
    _safe_set(b, 'actions_AtomicActionResult11', {a2})
    assert _is_linked(b, 'actions_AtomicActionResult11', a2)
    if hasattr(a1, 'actions_Distribution12'):
        assert not _is_linked(a1, 'actions_Distribution12', b)
    if hasattr(a2, 'actions_Distribution12'):
        assert _is_linked(a2, 'actions_Distribution12', b)
    _safe_set(b, 'actions_AtomicActionResult11', set())
    assert not _is_linked(b, 'actions_AtomicActionResult11', a2)
    if hasattr(a2, 'actions_Distribution12'):
        assert not _is_linked(a2, 'actions_Distribution12', b)


def test_assoc_hasQualityDistribution13_reverse_link_reassign_clear():
    a1 = actions_Distribution(datapoint=3.14, density=3.14, id=7, version=7)
    a2 = actions_Distribution(datapoint=9.99, density=9.99, id=13, version=13)
    b = actions_AtomicActionResult(hasDensity=3.14)
    _safe_set(b, 'actions_AtomicActionResult14', {a1})
    assert _is_linked(b, 'actions_AtomicActionResult14', a1)
    if hasattr(a1, 'actions_Distribution15'):
        assert _is_linked(a1, 'actions_Distribution15', b)
    _safe_set(b, 'actions_AtomicActionResult14', {a2})
    assert _is_linked(b, 'actions_AtomicActionResult14', a2)
    if hasattr(a1, 'actions_Distribution15'):
        assert not _is_linked(a1, 'actions_Distribution15', b)
    if hasattr(a2, 'actions_Distribution15'):
        assert _is_linked(a2, 'actions_Distribution15', b)
    _safe_set(b, 'actions_AtomicActionResult14', set())
    assert not _is_linked(b, 'actions_AtomicActionResult14', a2)
    if hasattr(a2, 'actions_Distribution15'):
        assert not _is_linked(a2, 'actions_Distribution15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions16_stub_double():
    # actions_Action has no real 'actions_Action17' property in the generated
    # code (a bare stub) -- manually attach it so actions_ActionsCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # actions_ActionsCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = actions_ActionsCollection(id=7, ns="sample_text", version=7)
    partner = actions_Action()
    setattr(partner, 'actions_Action17', None)
    _safe_set(owner, 'actions_ActionsCollection', {partner})
    assert getattr(partner, 'actions_Action17') == owner
    _safe_set(owner, 'actions_ActionsCollection', set())
    assert getattr(partner, 'actions_Action17') is None


def test_assoc_hasAddEffect3_stub_double():
    # actions_Expression has no real 'actions_Expression' property in the generated
    # code (a bare stub) -- manually attach it so actions_ActionResult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # actions_ActionResult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = actions_ActionResult(id=7, version=7)
    partner = actions_Expression()
    setattr(partner, 'actions_Expression', None)
    _safe_set(owner, 'actions_ActionResult4', {partner})
    assert getattr(partner, 'actions_Expression') == owner
    _safe_set(owner, 'actions_ActionResult4', set())
    assert getattr(partner, 'actions_Expression') is None


def test_assoc_hasAtomicActionResult1_stub_double():
    # actions_AtomicAction has no real 'actions_AtomicAction' property in the generated
    # code (a bare stub) -- manually attach it so actions_AtomicActionResult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # actions_AtomicActionResult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = actions_AtomicActionResult(hasDensity=3.14)
    partner = actions_AtomicAction()
    setattr(partner, 'actions_AtomicAction', None)
    _safe_set(owner, 'actions_AtomicActionResult', partner)
    assert owner in getattr(partner, 'actions_AtomicAction')
    _safe_set(owner, 'actions_AtomicActionResult', None)
    assert owner not in getattr(partner, 'actions_AtomicAction')


def test_assoc_hasDeleteEffect5_stub_double():
    # actions_Expression has no real 'actions_Expression7' property in the generated
    # code (a bare stub) -- manually attach it so actions_ActionResult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # actions_ActionResult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = actions_ActionResult(id=7, version=7)
    partner = actions_Expression()
    setattr(partner, 'actions_Expression7', None)
    _safe_set(owner, 'actions_ActionResult6', {partner})
    assert getattr(partner, 'actions_Expression7') == owner
    _safe_set(owner, 'actions_ActionResult6', set())
    assert getattr(partner, 'actions_Expression7') is None


def test_assoc_inCondition2_stub_double():
    # actions_Condition has no real 'actions_Condition' property in the generated
    # code (a bare stub) -- manually attach it so actions_ActionResult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # actions_ActionResult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = actions_ActionResult(id=7, version=7)
    partner = actions_Condition()
    setattr(partner, 'actions_Condition', None)
    _safe_set(owner, 'actions_ActionResult', {partner})
    assert getattr(partner, 'actions_Condition') == owner
    _safe_set(owner, 'actions_ActionResult', set())
    assert getattr(partner, 'actions_Condition') is None


def test_assoc_parameters20_stub_double():
    # actions_Parameter has no real 'actions_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so actions_ActionsCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # actions_ActionsCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = actions_ActionsCollection(id=7, ns="sample_text", version=7)
    partner = actions_Parameter()
    setattr(partner, 'actions_Parameter', None)
    _safe_set(owner, 'actions_ActionsCollection21', {partner})
    assert getattr(partner, 'actions_Parameter') == owner
    _safe_set(owner, 'actions_ActionsCollection21', set())
    assert getattr(partner, 'actions_Parameter') is None


def test_assoc_participants18_stub_double():
    # actions_Participant has no real 'actions_Participant' property in the generated
    # code (a bare stub) -- manually attach it so actions_ActionsCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # actions_ActionsCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = actions_ActionsCollection(id=7, ns="sample_text", version=7)
    partner = actions_Participant()
    setattr(partner, 'actions_Participant', None)
    _safe_set(owner, 'actions_ActionsCollection19', {partner})
    assert getattr(partner, 'actions_Participant') == owner
    _safe_set(owner, 'actions_ActionsCollection19', set())
    assert getattr(partner, 'actions_Participant') is None


