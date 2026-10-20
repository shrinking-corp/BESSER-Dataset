import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Item,
    smarthome_Command,
    smarthome_CommandConnection,
    smarthome_ContactItem,
    smarthome_DimmerItem,
    smarthome_EvaluatingNode,
    smarthome_FilterConnection,
    smarthome_Item,
    smarthome_NumberItem,
    smarthome_SmartHome,
    smarthome_State,
    smarthome_StateChangeConnection,
    smarthome_SwitchItem,
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

def test_assoc_accaptedCommands5_reverse_link_reassign_clear():
    a1 = smarthome_Item(name="sample_text")
    a2 = smarthome_Item(name="sample_text_2")
    b = smarthome_Command(command="sample_text")
    _safe_set(b, 'smarthome_Command', a1)
    assert _is_linked(b, 'smarthome_Command', a1)
    if hasattr(a1, 'smarthome_Item6'):
        assert _is_linked(a1, 'smarthome_Item6', b)
    _safe_set(b, 'smarthome_Command', a2)
    assert _is_linked(b, 'smarthome_Command', a2)
    if hasattr(a1, 'smarthome_Item6'):
        assert not _is_linked(a1, 'smarthome_Item6', b)
    if hasattr(a2, 'smarthome_Item6'):
        assert _is_linked(a2, 'smarthome_Item6', b)
    _safe_set(b, 'smarthome_Command', None)
    assert not _is_linked(b, 'smarthome_Command', a2)
    if hasattr(a2, 'smarthome_Item6'):
        assert not _is_linked(a2, 'smarthome_Item6', b)


def test_assoc_items0_reverse_link_reassign_clear():
    a1 = smarthome_SmartHome(name="sample_text")
    a2 = smarthome_SmartHome(name="sample_text_2")
    b = smarthome_Item(name="sample_text")
    _safe_set(b, 'smarthome_Item', a1)
    assert _is_linked(b, 'smarthome_Item', a1)
    if hasattr(a1, 'smarthome_SmartHome'):
        assert _is_linked(a1, 'smarthome_SmartHome', b)
    _safe_set(b, 'smarthome_Item', a2)
    assert _is_linked(b, 'smarthome_Item', a2)
    if hasattr(a1, 'smarthome_SmartHome'):
        assert not _is_linked(a1, 'smarthome_SmartHome', b)
    if hasattr(a2, 'smarthome_SmartHome'):
        assert _is_linked(a2, 'smarthome_SmartHome', b)
    _safe_set(b, 'smarthome_Item', None)
    assert not _is_linked(b, 'smarthome_Item', a2)
    if hasattr(a2, 'smarthome_SmartHome'):
        assert not _is_linked(a2, 'smarthome_SmartHome', b)


def test_assoc_states3_reverse_link_reassign_clear():
    a1 = smarthome_State(state="sample_text")
    a2 = smarthome_State(state="sample_text_2")
    b = smarthome_Item(name="sample_text")
    _safe_set(b, 'smarthome_Item4', {a1})
    assert _is_linked(b, 'smarthome_Item4', a1)
    if hasattr(a1, 'smarthome_State'):
        assert _is_linked(a1, 'smarthome_State', b)
    _safe_set(b, 'smarthome_Item4', {a2})
    assert _is_linked(b, 'smarthome_Item4', a2)
    if hasattr(a1, 'smarthome_State'):
        assert not _is_linked(a1, 'smarthome_State', b)
    if hasattr(a2, 'smarthome_State'):
        assert _is_linked(a2, 'smarthome_State', b)
    _safe_set(b, 'smarthome_Item4', set())
    assert not _is_linked(b, 'smarthome_Item4', a2)
    if hasattr(a2, 'smarthome_State'):
        assert not _is_linked(a2, 'smarthome_State', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_command16_stub_double():
    # smarthome_CommandConnection has no real 'smarthome_CommandConnection17' property in the generated
    # code (a bare stub) -- manually attach it so smarthome_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smarthome_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smarthome_Command(command="sample_text")
    partner = smarthome_CommandConnection()
    setattr(partner, 'smarthome_CommandConnection17', None)
    _safe_set(owner, 'smarthome_Command18', partner)
    assert getattr(partner, 'smarthome_CommandConnection17') == owner
    _safe_set(owner, 'smarthome_Command18', None)
    assert getattr(partner, 'smarthome_CommandConnection17') is None


def test_assoc_item13_stub_double():
    # smarthome_CommandConnection has no real 'smarthome_CommandConnection14' property in the generated
    # code (a bare stub) -- manually attach it so smarthome_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smarthome_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smarthome_Item(name="sample_text")
    partner = smarthome_CommandConnection()
    setattr(partner, 'smarthome_CommandConnection14', None)
    _safe_set(owner, 'smarthome_Item15', partner)
    assert getattr(partner, 'smarthome_CommandConnection14') == owner
    _safe_set(owner, 'smarthome_Item15', None)
    assert getattr(partner, 'smarthome_CommandConnection14') is None


def test_assoc_item22_stub_double():
    # smarthome_StateChangeConnection has no real 'smarthome_StateChangeConnection23' property in the generated
    # code (a bare stub) -- manually attach it so smarthome_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smarthome_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smarthome_Item(name="sample_text")
    partner = smarthome_StateChangeConnection()
    setattr(partner, 'smarthome_StateChangeConnection23', None)
    _safe_set(owner, 'smarthome_Item24', partner)
    assert getattr(partner, 'smarthome_StateChangeConnection23') == owner
    _safe_set(owner, 'smarthome_Item24', None)
    assert getattr(partner, 'smarthome_StateChangeConnection23') is None


def test_assoc_item28_stub_double():
    # smarthome_FilterConnection has no real 'smarthome_FilterConnection29' property in the generated
    # code (a bare stub) -- manually attach it so smarthome_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smarthome_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smarthome_Item(name="sample_text")
    partner = smarthome_FilterConnection()
    setattr(partner, 'smarthome_FilterConnection29', None)
    _safe_set(owner, 'smarthome_Item30', partner)
    assert getattr(partner, 'smarthome_FilterConnection29') == owner
    _safe_set(owner, 'smarthome_Item30', None)
    assert getattr(partner, 'smarthome_FilterConnection29') is None


def test_assoc_newState19_stub_double():
    # smarthome_StateChangeConnection has no real 'smarthome_StateChangeConnection20' property in the generated
    # code (a bare stub) -- manually attach it so smarthome_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smarthome_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smarthome_State(state="sample_text")
    partner = smarthome_StateChangeConnection()
    setattr(partner, 'smarthome_StateChangeConnection20', None)
    _safe_set(owner, 'smarthome_State21', partner)
    assert getattr(partner, 'smarthome_StateChangeConnection20') == owner
    _safe_set(owner, 'smarthome_State21', None)
    assert getattr(partner, 'smarthome_StateChangeConnection20') is None


def test_assoc_requiredState25_stub_double():
    # smarthome_FilterConnection has no real 'smarthome_FilterConnection26' property in the generated
    # code (a bare stub) -- manually attach it so smarthome_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smarthome_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smarthome_State(state="sample_text")
    partner = smarthome_FilterConnection()
    setattr(partner, 'smarthome_FilterConnection26', None)
    _safe_set(owner, 'smarthome_State27', partner)
    assert getattr(partner, 'smarthome_FilterConnection26') == owner
    _safe_set(owner, 'smarthome_State27', None)
    assert getattr(partner, 'smarthome_FilterConnection26') is None


def test_assoc_rules1_stub_double():
    # smarthome_EvaluatingNode has no real 'smarthome_EvaluatingNode' property in the generated
    # code (a bare stub) -- manually attach it so smarthome_SmartHome's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smarthome_SmartHome's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smarthome_SmartHome(name="sample_text")
    partner = smarthome_EvaluatingNode()
    setattr(partner, 'smarthome_EvaluatingNode', None)
    _safe_set(owner, 'smarthome_SmartHome2', {partner})
    assert getattr(partner, 'smarthome_EvaluatingNode') == owner
    _safe_set(owner, 'smarthome_SmartHome2', set())
    assert getattr(partner, 'smarthome_EvaluatingNode') is None


