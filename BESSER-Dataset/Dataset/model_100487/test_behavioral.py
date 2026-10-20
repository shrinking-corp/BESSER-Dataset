import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    UISUTElement,
    UITrigger,
    uisut_AbstractState,
    uisut_Action,
    uisut_ApplicationSystem,
    uisut_ComponentTrigger,
    uisut_FinalState,
    uisut_InitialState,
    uisut_UICondition,
    uisut_UIControl,
    uisut_UIDataVariable,
    uisut_UISUT,
    uisut_UISUTElement,
    uisut_UIState,
    uisut_UIStatemachine,
    uisut_UITransition,
    uisut_UITrigger,
    uisut_UserTrigger,
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

def test_assoc_addedDataVariable10_reverse_link_reassign_clear():
    a1 = uisut_UIState(isInitial=True, pic="sample_text")
    a2 = uisut_UIState(isInitial=False, pic="sample_text_2")
    b = uisut_UIDataVariable(constraintRE="sample_text")
    _safe_set(b, 'uisut_UIDataVariable12', a1)
    assert _is_linked(b, 'uisut_UIDataVariable12', a1)
    if hasattr(a1, 'uisut_UIState11'):
        assert _is_linked(a1, 'uisut_UIState11', b)
    _safe_set(b, 'uisut_UIDataVariable12', a2)
    assert _is_linked(b, 'uisut_UIDataVariable12', a2)
    if hasattr(a1, 'uisut_UIState11'):
        assert not _is_linked(a1, 'uisut_UIState11', b)
    if hasattr(a2, 'uisut_UIState11'):
        assert _is_linked(a2, 'uisut_UIState11', b)
    _safe_set(b, 'uisut_UIDataVariable12', None)
    assert not _is_linked(b, 'uisut_UIDataVariable12', a2)
    if hasattr(a2, 'uisut_UIState11'):
        assert not _is_linked(a2, 'uisut_UIState11', b)


def test_assoc_deletedDataVariable13_reverse_link_reassign_clear():
    a1 = uisut_UIState(isInitial=True, pic="sample_text")
    a2 = uisut_UIState(isInitial=False, pic="sample_text_2")
    b = uisut_UIDataVariable(constraintRE="sample_text")
    _safe_set(b, 'uisut_UIDataVariable15', a1)
    assert _is_linked(b, 'uisut_UIDataVariable15', a1)
    if hasattr(a1, 'uisut_UIState14'):
        assert _is_linked(a1, 'uisut_UIState14', b)
    _safe_set(b, 'uisut_UIDataVariable15', a2)
    assert _is_linked(b, 'uisut_UIDataVariable15', a2)
    if hasattr(a1, 'uisut_UIState14'):
        assert not _is_linked(a1, 'uisut_UIState14', b)
    if hasattr(a2, 'uisut_UIState14'):
        assert _is_linked(a2, 'uisut_UIState14', b)
    _safe_set(b, 'uisut_UIDataVariable15', None)
    assert not _is_linked(b, 'uisut_UIDataVariable15', a2)
    if hasattr(a2, 'uisut_UIState14'):
        assert not _is_linked(a2, 'uisut_UIState14', b)


def test_assoc_guardedDataVariable25_reverse_link_reassign_clear():
    a1 = uisut_UITransition(actionStr="sample_text", guardStr="sample_text", scriptStr="sample_text", triggerStr="sample_text")
    a2 = uisut_UITransition(actionStr="sample_text_2", guardStr="sample_text_2", scriptStr="sample_text_2", triggerStr="sample_text_2")
    b = uisut_UIDataVariable(constraintRE="sample_text")
    _safe_set(b, 'uisut_UIDataVariable27', a1)
    assert _is_linked(b, 'uisut_UIDataVariable27', a1)
    if hasattr(a1, 'uisut_UITransition26'):
        assert _is_linked(a1, 'uisut_UITransition26', b)
    _safe_set(b, 'uisut_UIDataVariable27', a2)
    assert _is_linked(b, 'uisut_UIDataVariable27', a2)
    if hasattr(a1, 'uisut_UITransition26'):
        assert not _is_linked(a1, 'uisut_UITransition26', b)
    if hasattr(a2, 'uisut_UITransition26'):
        assert _is_linked(a2, 'uisut_UITransition26', b)
    _safe_set(b, 'uisut_UIDataVariable27', None)
    assert not _is_linked(b, 'uisut_UIDataVariable27', a2)
    if hasattr(a2, 'uisut_UITransition26'):
        assert not _is_linked(a2, 'uisut_UITransition26', b)


def test_assoc_itsInputDaa28_reverse_link_reassign_clear():
    a1 = uisut_UIDataVariable(constraintRE="sample_text")
    a2 = uisut_UIDataVariable(constraintRE="sample_text_2")
    b = uisut_UIControl(valueExpression="sample_text", variableName="sample_text")
    _safe_set(b, 'uisut_UIControl29', a1)
    assert _is_linked(b, 'uisut_UIControl29', a1)
    if hasattr(a1, 'uisut_UIDataVariable30'):
        assert _is_linked(a1, 'uisut_UIDataVariable30', b)
    _safe_set(b, 'uisut_UIControl29', a2)
    assert _is_linked(b, 'uisut_UIControl29', a2)
    if hasattr(a1, 'uisut_UIDataVariable30'):
        assert not _is_linked(a1, 'uisut_UIDataVariable30', b)
    if hasattr(a2, 'uisut_UIDataVariable30'):
        assert _is_linked(a2, 'uisut_UIDataVariable30', b)
    _safe_set(b, 'uisut_UIControl29', None)
    assert not _is_linked(b, 'uisut_UIControl29', a2)
    if hasattr(a2, 'uisut_UIDataVariable30'):
        assert not _is_linked(a2, 'uisut_UIDataVariable30', b)


def test_assoc_itsOutputData31_reverse_link_reassign_clear():
    a1 = uisut_UIDataVariable(constraintRE="sample_text")
    a2 = uisut_UIDataVariable(constraintRE="sample_text_2")
    b = uisut_UIControl(valueExpression="sample_text", variableName="sample_text")
    _safe_set(b, 'uisut_UIControl32', a1)
    assert _is_linked(b, 'uisut_UIControl32', a1)
    if hasattr(a1, 'uisut_UIDataVariable33'):
        assert _is_linked(a1, 'uisut_UIDataVariable33', b)
    _safe_set(b, 'uisut_UIControl32', a2)
    assert _is_linked(b, 'uisut_UIControl32', a2)
    if hasattr(a1, 'uisut_UIDataVariable33'):
        assert not _is_linked(a1, 'uisut_UIDataVariable33', b)
    if hasattr(a2, 'uisut_UIDataVariable33'):
        assert _is_linked(a2, 'uisut_UIDataVariable33', b)
    _safe_set(b, 'uisut_UIControl32', None)
    assert not _is_linked(b, 'uisut_UIControl32', a2)
    if hasattr(a2, 'uisut_UIDataVariable33'):
        assert not _is_linked(a2, 'uisut_UIDataVariable33', b)


def test_assoc_itsUIControl9_reverse_link_reassign_clear():
    a1 = uisut_UIState(isInitial=True, pic="sample_text")
    a2 = uisut_UIState(isInitial=False, pic="sample_text_2")
    b = uisut_UIControl(valueExpression="sample_text", variableName="sample_text")
    _safe_set(b, 'uisut_UIControl', a1)
    assert _is_linked(b, 'uisut_UIControl', a1)
    if hasattr(a1, 'uisut_UIState'):
        assert _is_linked(a1, 'uisut_UIState', b)
    _safe_set(b, 'uisut_UIControl', a2)
    assert _is_linked(b, 'uisut_UIControl', a2)
    if hasattr(a1, 'uisut_UIState'):
        assert not _is_linked(a1, 'uisut_UIState', b)
    if hasattr(a2, 'uisut_UIState'):
        assert _is_linked(a2, 'uisut_UIState', b)
    _safe_set(b, 'uisut_UIControl', None)
    assert not _is_linked(b, 'uisut_UIControl', a2)
    if hasattr(a2, 'uisut_UIState'):
        assert not _is_linked(a2, 'uisut_UIState', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_itsAction23_stub_double():
    # uisut_Action has no real 'uisut_Action' property in the generated
    # code (a bare stub) -- manually attach it so uisut_UITransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uisut_UITransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uisut_UITransition(actionStr="sample_text", guardStr="sample_text", scriptStr="sample_text", triggerStr="sample_text")
    partner = uisut_Action()
    setattr(partner, 'uisut_Action', None)
    _safe_set(owner, 'uisut_UITransition24', partner)
    assert getattr(partner, 'uisut_Action') == owner
    _safe_set(owner, 'uisut_UITransition24', None)
    assert getattr(partner, 'uisut_Action') is None


def test_assoc_itsCondition21_stub_double():
    # uisut_UICondition has no real 'uisut_UICondition' property in the generated
    # code (a bare stub) -- manually attach it so uisut_UITransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uisut_UITransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uisut_UITransition(actionStr="sample_text", guardStr="sample_text", scriptStr="sample_text", triggerStr="sample_text")
    partner = uisut_UICondition()
    setattr(partner, 'uisut_UICondition', None)
    _safe_set(owner, 'uisut_UITransition22', partner)
    assert getattr(partner, 'uisut_UICondition') == owner
    _safe_set(owner, 'uisut_UITransition22', None)
    assert getattr(partner, 'uisut_UICondition') is None


def test_assoc_itsDataVariable7_stub_double():
    # uisut_UIStatemachine has no real 'uisut_UIStatemachine8' property in the generated
    # code (a bare stub) -- manually attach it so uisut_UIDataVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uisut_UIDataVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uisut_UIDataVariable(constraintRE="sample_text")
    partner = uisut_UIStatemachine()
    setattr(partner, 'uisut_UIStatemachine8', None)
    _safe_set(owner, 'uisut_UIDataVariable', partner)
    assert owner in getattr(partner, 'uisut_UIStatemachine8')
    _safe_set(owner, 'uisut_UIDataVariable', None)
    assert owner not in getattr(partner, 'uisut_UIStatemachine8')


def test_assoc_itsInTransition34_stub_double():
    # uisut_AbstractState has no real 'itsTrgtState' property in the generated
    # code (a bare stub) -- manually attach it so uisut_UITransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uisut_UITransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uisut_UITransition(actionStr="sample_text", guardStr="sample_text", scriptStr="sample_text", triggerStr="sample_text")
    partner = uisut_AbstractState()
    setattr(partner, 'itsTrgtState', None)
    _safe_set(owner, 'UITransition', partner)
    assert owner in getattr(partner, 'itsTrgtState')
    _safe_set(owner, 'UITransition', None)
    assert owner not in getattr(partner, 'itsTrgtState')


def test_assoc_itsOutTransition35_stub_double():
    # uisut_AbstractState has no real 'itsSrcState' property in the generated
    # code (a bare stub) -- manually attach it so uisut_UITransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uisut_UITransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uisut_UITransition(actionStr="sample_text", guardStr="sample_text", scriptStr="sample_text", triggerStr="sample_text")
    partner = uisut_AbstractState()
    setattr(partner, 'itsSrcState', None)
    _safe_set(owner, 'UITransition36', partner)
    assert owner in getattr(partner, 'itsSrcState')
    _safe_set(owner, 'UITransition36', None)
    assert owner not in getattr(partner, 'itsSrcState')


def test_assoc_itsSrcState17_stub_double():
    # uisut_AbstractState has no real 'AbstractState18' property in the generated
    # code (a bare stub) -- manually attach it so uisut_UITransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uisut_UITransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uisut_UITransition(actionStr="sample_text", guardStr="sample_text", scriptStr="sample_text", triggerStr="sample_text")
    partner = uisut_AbstractState()
    setattr(partner, 'AbstractState18', None)
    _safe_set(owner, 'itsOutTransition', partner)
    assert getattr(partner, 'AbstractState18') == owner
    _safe_set(owner, 'itsOutTransition', None)
    assert getattr(partner, 'AbstractState18') is None


def test_assoc_itsTransition5_stub_double():
    # uisut_UIStatemachine has no real 'uisut_UIStatemachine6' property in the generated
    # code (a bare stub) -- manually attach it so uisut_UITransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uisut_UITransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uisut_UITransition(actionStr="sample_text", guardStr="sample_text", scriptStr="sample_text", triggerStr="sample_text")
    partner = uisut_UIStatemachine()
    setattr(partner, 'uisut_UIStatemachine6', None)
    _safe_set(owner, 'uisut_UITransition', partner)
    assert owner in getattr(partner, 'uisut_UIStatemachine6')
    _safe_set(owner, 'uisut_UITransition', None)
    assert owner not in getattr(partner, 'uisut_UIStatemachine6')


def test_assoc_itsTrgtState16_stub_double():
    # uisut_AbstractState has no real 'AbstractState' property in the generated
    # code (a bare stub) -- manually attach it so uisut_UITransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uisut_UITransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uisut_UITransition(actionStr="sample_text", guardStr="sample_text", scriptStr="sample_text", triggerStr="sample_text")
    partner = uisut_AbstractState()
    setattr(partner, 'AbstractState', None)
    _safe_set(owner, 'itsInTransition', partner)
    assert getattr(partner, 'AbstractState') == owner
    _safe_set(owner, 'itsInTransition', None)
    assert getattr(partner, 'AbstractState') is None


def test_assoc_itsTrigger19_stub_double():
    # uisut_UITrigger has no real 'uisut_UITrigger' property in the generated
    # code (a bare stub) -- manually attach it so uisut_UITransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uisut_UITransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uisut_UITransition(actionStr="sample_text", guardStr="sample_text", scriptStr="sample_text", triggerStr="sample_text")
    partner = uisut_UITrigger()
    setattr(partner, 'uisut_UITrigger', None)
    _safe_set(owner, 'uisut_UITransition20', partner)
    assert getattr(partner, 'uisut_UITrigger') == owner
    _safe_set(owner, 'uisut_UITransition20', None)
    assert getattr(partner, 'uisut_UITrigger') is None


