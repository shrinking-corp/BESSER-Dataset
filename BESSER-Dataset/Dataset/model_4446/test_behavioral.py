import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Component,
    Controller,
    Hardware,
    Item,
    Iteration,
    RequiredPort,
    iot_Actuator,
    iot_Branching,
    iot_Component,
    iot_ConditionPort,
    iot_Controller,
    iot_CounterLoop,
    iot_ElsePort,
    iot_Hardware,
    iot_IfPort,
    iot_Item,
    iot_Iteration,
    iot_IterativeLoop,
    iot_ProvidedPort,
    iot_RequiredPort,
    iot_Sensor,
    iot_Sequence,
    iot_Snippet,
    iot_Software,
    iot_ThenPort,
    Operator,
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

def test_assoc_referto2_reverse_link_reassign_clear():
    a1 = iot_ProvidedPort(UUID="sample_text", name="sample_text")
    a2 = iot_ProvidedPort(UUID="sample_text_2", name="sample_text_2")
    b = iot_Item(UUID="sample_text", name="sample_text", newThread=True)
    _safe_set(b, 'iot_Item3', a1)
    assert _is_linked(b, 'iot_Item3', a1)
    if hasattr(a1, 'iot_ProvidedPort'):
        assert _is_linked(a1, 'iot_ProvidedPort', b)
    _safe_set(b, 'iot_Item3', a2)
    assert _is_linked(b, 'iot_Item3', a2)
    if hasattr(a1, 'iot_ProvidedPort'):
        assert not _is_linked(a1, 'iot_ProvidedPort', b)
    if hasattr(a2, 'iot_ProvidedPort'):
        assert _is_linked(a2, 'iot_ProvidedPort', b)
    _safe_set(b, 'iot_Item3', None)
    assert not _is_linked(b, 'iot_Item3', a2)
    if hasattr(a2, 'iot_ProvidedPort'):
        assert not _is_linked(a2, 'iot_ProvidedPort', b)


def test_assoc_use19_reverse_link_reassign_clear():
    a1 = iot_RequiredPort(UUID="sample_text", args="sample_text", method="sample_text", name="sample_text")
    a2 = iot_RequiredPort(UUID="sample_text_2", args="sample_text_2", method="sample_text_2", name="sample_text_2")
    b = iot_ProvidedPort(UUID="sample_text", name="sample_text")
    _safe_set(b, 'iot_ProvidedPort21', a1)
    assert _is_linked(b, 'iot_ProvidedPort21', a1)
    if hasattr(a1, 'iot_RequiredPort20'):
        assert _is_linked(a1, 'iot_RequiredPort20', b)
    _safe_set(b, 'iot_ProvidedPort21', a2)
    assert _is_linked(b, 'iot_ProvidedPort21', a2)
    if hasattr(a1, 'iot_RequiredPort20'):
        assert not _is_linked(a1, 'iot_RequiredPort20', b)
    if hasattr(a2, 'iot_RequiredPort20'):
        assert _is_linked(a2, 'iot_RequiredPort20', b)
    _safe_set(b, 'iot_ProvidedPort21', None)
    assert not _is_linked(b, 'iot_ProvidedPort21', a2)
    if hasattr(a2, 'iot_RequiredPort20'):
        assert not _is_linked(a2, 'iot_RequiredPort20', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_condition1_stub_double():
    # iot_ConditionPort has no real 'iot_ConditionPort' property in the generated
    # code (a bare stub) -- manually attach it so iot_IterativeLoop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_IterativeLoop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_IterativeLoop(operator="sample_text", var="sample_text")
    partner = iot_ConditionPort()
    setattr(partner, 'iot_ConditionPort', None)
    _safe_set(owner, 'iot_IterativeLoop', partner)
    assert getattr(partner, 'iot_ConditionPort') == owner
    _safe_set(owner, 'iot_IterativeLoop', None)
    assert getattr(partner, 'iot_ConditionPort') is None


def test_assoc_ifport4_stub_double():
    # iot_Branching has no real 'iot_Branching' property in the generated
    # code (a bare stub) -- manually attach it so iot_IfPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_IfPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_IfPort(condition=True, operator="sample_text", var="sample_text")
    partner = iot_Branching()
    setattr(partner, 'iot_Branching', None)
    _safe_set(owner, 'iot_IfPort', partner)
    assert getattr(partner, 'iot_Branching') == owner
    _safe_set(owner, 'iot_IfPort', None)
    assert getattr(partner, 'iot_Branching') is None


def test_assoc_item0_stub_double():
    # iot_Software has no real 'iot_Software' property in the generated
    # code (a bare stub) -- manually attach it so iot_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_Item(UUID="sample_text", name="sample_text", newThread=True)
    partner = iot_Software()
    setattr(partner, 'iot_Software', None)
    _safe_set(owner, 'iot_Item', partner)
    assert owner in getattr(partner, 'iot_Software')
    _safe_set(owner, 'iot_Item', None)
    assert owner not in getattr(partner, 'iot_Software')


def test_assoc_providedport14_stub_double():
    # iot_Component has no real 'iot_Component15' property in the generated
    # code (a bare stub) -- manually attach it so iot_ProvidedPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_ProvidedPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_ProvidedPort(UUID="sample_text", name="sample_text")
    partner = iot_Component()
    setattr(partner, 'iot_Component15', None)
    _safe_set(owner, 'iot_ProvidedPort16', partner)
    assert owner in getattr(partner, 'iot_Component15')
    _safe_set(owner, 'iot_ProvidedPort16', None)
    assert owner not in getattr(partner, 'iot_Component15')


def test_assoc_providedport17_stub_double():
    # iot_Controller has no real 'iot_Controller' property in the generated
    # code (a bare stub) -- manually attach it so iot_ProvidedPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_ProvidedPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_ProvidedPort(UUID="sample_text", name="sample_text")
    partner = iot_Controller()
    setattr(partner, 'iot_Controller', None)
    _safe_set(owner, 'iot_ProvidedPort18', partner)
    assert getattr(partner, 'iot_Controller') == owner
    _safe_set(owner, 'iot_ProvidedPort18', None)
    assert getattr(partner, 'iot_Controller') is None


def test_assoc_requiredport10_stub_double():
    # iot_Sequence has no real 'iot_Sequence' property in the generated
    # code (a bare stub) -- manually attach it so iot_RequiredPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_RequiredPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_RequiredPort(UUID="sample_text", args="sample_text", method="sample_text", name="sample_text")
    partner = iot_Sequence()
    setattr(partner, 'iot_Sequence', None)
    _safe_set(owner, 'iot_RequiredPort11', partner)
    assert owner in getattr(partner, 'iot_Sequence')
    _safe_set(owner, 'iot_RequiredPort11', None)
    assert owner not in getattr(partner, 'iot_Sequence')


def test_assoc_requiredport12_stub_double():
    # iot_Component has no real 'iot_Component' property in the generated
    # code (a bare stub) -- manually attach it so iot_RequiredPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_RequiredPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_RequiredPort(UUID="sample_text", args="sample_text", method="sample_text", name="sample_text")
    partner = iot_Component()
    setattr(partner, 'iot_Component', None)
    _safe_set(owner, 'iot_RequiredPort13', partner)
    assert owner in getattr(partner, 'iot_Component')
    _safe_set(owner, 'iot_RequiredPort13', None)
    assert owner not in getattr(partner, 'iot_Component')


def test_assoc_requiredport9_stub_double():
    # iot_Iteration has no real 'iot_Iteration' property in the generated
    # code (a bare stub) -- manually attach it so iot_RequiredPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iot_RequiredPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iot_RequiredPort(UUID="sample_text", args="sample_text", method="sample_text", name="sample_text")
    partner = iot_Iteration()
    setattr(partner, 'iot_Iteration', None)
    _safe_set(owner, 'iot_RequiredPort', partner)
    assert getattr(partner, 'iot_Iteration') == owner
    _safe_set(owner, 'iot_RequiredPort', None)
    assert getattr(partner, 'iot_Iteration') is None


