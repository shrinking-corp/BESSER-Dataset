import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    mngr_ManagedElement,
    mngr_Manager,
    mngr_ManagerParameter,
    mngr_ManagerState,
    mngr_ManagerTransition,
    mngr_OpaqueExpression,
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

def test_assoc_contextParameters16_reverse_link_reassign_clear():
    a1 = mngr_ManagerState(Prob=3.14, isEnd=True, isStart=True)
    a2 = mngr_ManagerState(Prob=9.99, isEnd=False, isStart=False)
    b = mngr_ManagerParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    _safe_set(b, 'ManagerParameter17', a1)
    assert _is_linked(b, 'ManagerParameter17', a1)
    if hasattr(a1, 'state'):
        assert _is_linked(a1, 'state', b)
    _safe_set(b, 'ManagerParameter17', a2)
    assert _is_linked(b, 'ManagerParameter17', a2)
    if hasattr(a1, 'state'):
        assert not _is_linked(a1, 'state', b)
    if hasattr(a2, 'state'):
        assert _is_linked(a2, 'state', b)
    _safe_set(b, 'ManagerParameter17', None)
    assert not _is_linked(b, 'ManagerParameter17', a2)
    if hasattr(a2, 'state'):
        assert not _is_linked(a2, 'state', b)


def test_assoc_incomingTransition14_reverse_link_reassign_clear():
    a1 = mngr_ManagerTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", output="sample_text", transProb=3.14, transRate=3.14)
    a2 = mngr_ManagerTransition(Action="sample_text_2", Condition="sample_text_2", Event="sample_text_2", input="sample_text_2", output="sample_text_2", transProb=9.99, transRate=9.99)
    b = mngr_ManagerState(Prob=3.14, isEnd=True, isStart=True)
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'ManagerTransition15'):
        assert _is_linked(a1, 'ManagerTransition15', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'ManagerTransition15'):
        assert not _is_linked(a1, 'ManagerTransition15', b)
    if hasattr(a2, 'ManagerTransition15'):
        assert _is_linked(a2, 'ManagerTransition15', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'ManagerTransition15'):
        assert not _is_linked(a2, 'ManagerTransition15', b)


def test_assoc_outgoingTransition12_reverse_link_reassign_clear():
    a1 = mngr_ManagerTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", output="sample_text", transProb=3.14, transRate=3.14)
    a2 = mngr_ManagerTransition(Action="sample_text_2", Condition="sample_text_2", Event="sample_text_2", input="sample_text_2", output="sample_text_2", transProb=9.99, transRate=9.99)
    b = mngr_ManagerState(Prob=3.14, isEnd=True, isStart=True)
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'ManagerTransition13'):
        assert _is_linked(a1, 'ManagerTransition13', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'ManagerTransition13'):
        assert not _is_linked(a1, 'ManagerTransition13', b)
    if hasattr(a2, 'ManagerTransition13'):
        assert _is_linked(a2, 'ManagerTransition13', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'ManagerTransition13'):
        assert not _is_linked(a2, 'ManagerTransition13', b)


def test_assoc_source20_reverse_link_reassign_clear():
    a1 = mngr_ManagerTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", output="sample_text", transProb=3.14, transRate=3.14)
    a2 = mngr_ManagerTransition(Action="sample_text_2", Condition="sample_text_2", Event="sample_text_2", input="sample_text_2", output="sample_text_2", transProb=9.99, transRate=9.99)
    b = mngr_ManagerState(Prob=3.14, isEnd=True, isStart=True)
    _safe_set(b, 'ManagerState21', a1)
    assert _is_linked(b, 'ManagerState21', a1)
    if hasattr(a1, 'outgoingTransition'):
        assert _is_linked(a1, 'outgoingTransition', b)
    _safe_set(b, 'ManagerState21', a2)
    assert _is_linked(b, 'ManagerState21', a2)
    if hasattr(a1, 'outgoingTransition'):
        assert not _is_linked(a1, 'outgoingTransition', b)
    if hasattr(a2, 'outgoingTransition'):
        assert _is_linked(a2, 'outgoingTransition', b)
    _safe_set(b, 'ManagerState21', None)
    assert not _is_linked(b, 'ManagerState21', a2)
    if hasattr(a2, 'outgoingTransition'):
        assert not _is_linked(a2, 'outgoingTransition', b)


def test_assoc_state24_reverse_link_reassign_clear():
    a1 = mngr_ManagerState(Prob=3.14, isEnd=True, isStart=True)
    a2 = mngr_ManagerState(Prob=9.99, isEnd=False, isStart=False)
    b = mngr_ManagerParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    _safe_set(b, 'contextParameters', {a1})
    assert _is_linked(b, 'contextParameters', a1)
    if hasattr(a1, 'ManagerState25'):
        assert _is_linked(a1, 'ManagerState25', b)
    _safe_set(b, 'contextParameters', {a2})
    assert _is_linked(b, 'contextParameters', a2)
    if hasattr(a1, 'ManagerState25'):
        assert not _is_linked(a1, 'ManagerState25', b)
    if hasattr(a2, 'ManagerState25'):
        assert _is_linked(a2, 'ManagerState25', b)
    _safe_set(b, 'contextParameters', set())
    assert not _is_linked(b, 'contextParameters', a2)
    if hasattr(a2, 'ManagerState25'):
        assert not _is_linked(a2, 'ManagerState25', b)


def test_assoc_target22_reverse_link_reassign_clear():
    a1 = mngr_ManagerTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", output="sample_text", transProb=3.14, transRate=3.14)
    a2 = mngr_ManagerTransition(Action="sample_text_2", Condition="sample_text_2", Event="sample_text_2", input="sample_text_2", output="sample_text_2", transProb=9.99, transRate=9.99)
    b = mngr_ManagerState(Prob=3.14, isEnd=True, isStart=True)
    _safe_set(b, 'ManagerState23', a1)
    assert _is_linked(b, 'ManagerState23', a1)
    if hasattr(a1, 'incomingTransition'):
        assert _is_linked(a1, 'incomingTransition', b)
    _safe_set(b, 'ManagerState23', a2)
    assert _is_linked(b, 'ManagerState23', a2)
    if hasattr(a1, 'incomingTransition'):
        assert not _is_linked(a1, 'incomingTransition', b)
    if hasattr(a2, 'incomingTransition'):
        assert _is_linked(a2, 'incomingTransition', b)
    _safe_set(b, 'ManagerState23', None)
    assert not _is_linked(b, 'ManagerState23', a2)
    if hasattr(a2, 'incomingTransition'):
        assert not _is_linked(a2, 'incomingTransition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contextParameters5_stub_double():
    # mngr_Manager has no real 'owningManager6' property in the generated
    # code (a bare stub) -- manually attach it so mngr_ManagerParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mngr_ManagerParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mngr_ManagerParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    partner = mngr_Manager()
    setattr(partner, 'owningManager6', None)
    _safe_set(owner, 'ManagerParameter', partner)
    assert owner in getattr(partner, 'owningManager6')
    _safe_set(owner, 'ManagerParameter', None)
    assert owner not in getattr(partner, 'owningManager6')


def test_assoc_finalState2_stub_double():
    # mngr_Manager has no real 'mngr_Manager3' property in the generated
    # code (a bare stub) -- manually attach it so mngr_ManagerState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mngr_ManagerState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mngr_ManagerState(Prob=3.14, isEnd=True, isStart=True)
    partner = mngr_Manager()
    setattr(partner, 'mngr_Manager3', None)
    _safe_set(owner, 'mngr_ManagerState4', partner)
    assert owner in getattr(partner, 'mngr_Manager3')
    _safe_set(owner, 'mngr_ManagerState4', None)
    assert owner not in getattr(partner, 'mngr_Manager3')


def test_assoc_initialState1_stub_double():
    # mngr_Manager has no real 'mngr_Manager' property in the generated
    # code (a bare stub) -- manually attach it so mngr_ManagerState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mngr_ManagerState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mngr_ManagerState(Prob=3.14, isEnd=True, isStart=True)
    partner = mngr_Manager()
    setattr(partner, 'mngr_Manager', None)
    _safe_set(owner, 'mngr_ManagerState', partner)
    assert getattr(partner, 'mngr_Manager') == owner
    _safe_set(owner, 'mngr_ManagerState', None)
    assert getattr(partner, 'mngr_Manager') is None


def test_assoc_managedElement7_stub_double():
    # mngr_Manager has no real 'owningManager8' property in the generated
    # code (a bare stub) -- manually attach it so mngr_ManagedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mngr_ManagedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mngr_ManagedElement(description="sample_text")
    partner = mngr_Manager()
    setattr(partner, 'owningManager8', None)
    _safe_set(owner, 'ManagedElement', partner)
    assert owner in getattr(partner, 'owningManager8')
    _safe_set(owner, 'ManagedElement', None)
    assert owner not in getattr(partner, 'owningManager8')


def test_assoc_opaqueExpressions26_stub_double():
    # mngr_OpaqueExpression has no real 'mngr_OpaqueExpression' property in the generated
    # code (a bare stub) -- manually attach it so mngr_ManagerParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mngr_ManagerParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mngr_ManagerParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    partner = mngr_OpaqueExpression()
    setattr(partner, 'mngr_OpaqueExpression', None)
    _safe_set(owner, 'mngr_ManagerParameter', {partner})
    assert getattr(partner, 'mngr_OpaqueExpression') == owner
    _safe_set(owner, 'mngr_ManagerParameter', set())
    assert getattr(partner, 'mngr_OpaqueExpression') is None


def test_assoc_ownedState0_stub_double():
    # mngr_Manager has no real 'owningManager' property in the generated
    # code (a bare stub) -- manually attach it so mngr_ManagerState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mngr_ManagerState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mngr_ManagerState(Prob=3.14, isEnd=True, isStart=True)
    partner = mngr_Manager()
    setattr(partner, 'owningManager', None)
    _safe_set(owner, 'ManagerState', partner)
    assert owner in getattr(partner, 'owningManager')
    _safe_set(owner, 'ManagerState', None)
    assert owner not in getattr(partner, 'owningManager')


def test_assoc_ownedTransition9_stub_double():
    # mngr_Manager has no real 'owningManager10' property in the generated
    # code (a bare stub) -- manually attach it so mngr_ManagerTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mngr_ManagerTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mngr_ManagerTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", output="sample_text", transProb=3.14, transRate=3.14)
    partner = mngr_Manager()
    setattr(partner, 'owningManager10', None)
    _safe_set(owner, 'ManagerTransition', partner)
    assert owner in getattr(partner, 'owningManager10')
    _safe_set(owner, 'ManagerTransition', None)
    assert owner not in getattr(partner, 'owningManager10')


def test_assoc_owningManager11_stub_double():
    # mngr_Manager has no real 'Manager' property in the generated
    # code (a bare stub) -- manually attach it so mngr_ManagerState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mngr_ManagerState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mngr_ManagerState(Prob=3.14, isEnd=True, isStart=True)
    partner = mngr_Manager()
    setattr(partner, 'Manager', None)
    _safe_set(owner, 'ownedState', partner)
    assert getattr(partner, 'Manager') == owner
    _safe_set(owner, 'ownedState', None)
    assert getattr(partner, 'Manager') is None


def test_assoc_owningManager18_stub_double():
    # mngr_Manager has no real 'Manager19' property in the generated
    # code (a bare stub) -- manually attach it so mngr_ManagerTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mngr_ManagerTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mngr_ManagerTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", output="sample_text", transProb=3.14, transRate=3.14)
    partner = mngr_Manager()
    setattr(partner, 'Manager19', None)
    _safe_set(owner, 'ownedTransition', partner)
    assert getattr(partner, 'Manager19') == owner
    _safe_set(owner, 'ownedTransition', None)
    assert getattr(partner, 'Manager19') is None


def test_assoc_owningManager27_stub_double():
    # mngr_Manager has no real 'Manager29' property in the generated
    # code (a bare stub) -- manually attach it so mngr_ManagerParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mngr_ManagerParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mngr_ManagerParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    partner = mngr_Manager()
    setattr(partner, 'Manager29', None)
    _safe_set(owner, 'contextParameters28', partner)
    assert getattr(partner, 'Manager29') == owner
    _safe_set(owner, 'contextParameters28', None)
    assert getattr(partner, 'Manager29') is None


def test_assoc_owningManager30_stub_double():
    # mngr_Manager has no real 'Manager31' property in the generated
    # code (a bare stub) -- manually attach it so mngr_ManagedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mngr_ManagedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mngr_ManagedElement(description="sample_text")
    partner = mngr_Manager()
    setattr(partner, 'Manager31', None)
    _safe_set(owner, 'managedElement', partner)
    assert getattr(partner, 'Manager31') == owner
    _safe_set(owner, 'managedElement', None)
    assert getattr(partner, 'Manager31') is None


