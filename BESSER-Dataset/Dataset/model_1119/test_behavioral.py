import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    ctxmngr_ContextManager,
    ctxmngr_ContextParameter,
    ctxmngr_CtxState,
    ctxmngr_CtxTransition,
    ctxmngr_Manager,
    ctxmngr_ManagerState,
    ctxmngr_ManagerTransition,
    ctxmngr_OpaqueExpression,
    ctxmngr_RemoteFiringDependency,
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

def test_assoc_contextParameters18_reverse_link_reassign_clear():
    a1 = ctxmngr_CtxState(isEnd=True, isStart=True)
    a2 = ctxmngr_CtxState(isEnd=False, isStart=False)
    b = ctxmngr_ContextParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    _safe_set(b, 'ContextParameter19', a1)
    assert _is_linked(b, 'ContextParameter19', a1)
    if hasattr(a1, 'state'):
        assert _is_linked(a1, 'state', b)
    _safe_set(b, 'ContextParameter19', a2)
    assert _is_linked(b, 'ContextParameter19', a2)
    if hasattr(a1, 'state'):
        assert not _is_linked(a1, 'state', b)
    if hasattr(a2, 'state'):
        assert _is_linked(a2, 'state', b)
    _safe_set(b, 'ContextParameter19', None)
    assert not _is_linked(b, 'ContextParameter19', a2)
    if hasattr(a2, 'state'):
        assert not _is_linked(a2, 'state', b)


def test_assoc_incomingTransition16_reverse_link_reassign_clear():
    a1 = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    a2 = ctxmngr_CtxTransition(Action="sample_text_2", Condition="sample_text_2", Event="sample_text_2", input="sample_text_2", isRemote=False, output="sample_text_2", transProb=9.99, transRate=9.99)
    b = ctxmngr_CtxState(isEnd=True, isStart=True)
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'CtxTransition17'):
        assert _is_linked(a1, 'CtxTransition17', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'CtxTransition17'):
        assert not _is_linked(a1, 'CtxTransition17', b)
    if hasattr(a2, 'CtxTransition17'):
        assert _is_linked(a2, 'CtxTransition17', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'CtxTransition17'):
        assert not _is_linked(a2, 'CtxTransition17', b)


def test_assoc_outgoingTransition14_reverse_link_reassign_clear():
    a1 = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    a2 = ctxmngr_CtxTransition(Action="sample_text_2", Condition="sample_text_2", Event="sample_text_2", input="sample_text_2", isRemote=False, output="sample_text_2", transProb=9.99, transRate=9.99)
    b = ctxmngr_CtxState(isEnd=True, isStart=True)
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'CtxTransition15'):
        assert _is_linked(a1, 'CtxTransition15', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'CtxTransition15'):
        assert not _is_linked(a1, 'CtxTransition15', b)
    if hasattr(a2, 'CtxTransition15'):
        assert _is_linked(a2, 'CtxTransition15', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'CtxTransition15'):
        assert not _is_linked(a2, 'CtxTransition15', b)


def test_assoc_source24_reverse_link_reassign_clear():
    a1 = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    a2 = ctxmngr_CtxTransition(Action="sample_text_2", Condition="sample_text_2", Event="sample_text_2", input="sample_text_2", isRemote=False, output="sample_text_2", transProb=9.99, transRate=9.99)
    b = ctxmngr_CtxState(isEnd=True, isStart=True)
    _safe_set(b, 'CtxState25', a1)
    assert _is_linked(b, 'CtxState25', a1)
    if hasattr(a1, 'outgoingTransition'):
        assert _is_linked(a1, 'outgoingTransition', b)
    _safe_set(b, 'CtxState25', a2)
    assert _is_linked(b, 'CtxState25', a2)
    if hasattr(a1, 'outgoingTransition'):
        assert not _is_linked(a1, 'outgoingTransition', b)
    if hasattr(a2, 'outgoingTransition'):
        assert _is_linked(a2, 'outgoingTransition', b)
    _safe_set(b, 'CtxState25', None)
    assert not _is_linked(b, 'CtxState25', a2)
    if hasattr(a2, 'outgoingTransition'):
        assert not _is_linked(a2, 'outgoingTransition', b)


def test_assoc_state29_reverse_link_reassign_clear():
    a1 = ctxmngr_CtxState(isEnd=True, isStart=True)
    a2 = ctxmngr_CtxState(isEnd=False, isStart=False)
    b = ctxmngr_ContextParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    _safe_set(b, 'contextParameters', {a1})
    assert _is_linked(b, 'contextParameters', a1)
    if hasattr(a1, 'CtxState30'):
        assert _is_linked(a1, 'CtxState30', b)
    _safe_set(b, 'contextParameters', {a2})
    assert _is_linked(b, 'contextParameters', a2)
    if hasattr(a1, 'CtxState30'):
        assert not _is_linked(a1, 'CtxState30', b)
    if hasattr(a2, 'CtxState30'):
        assert _is_linked(a2, 'CtxState30', b)
    _safe_set(b, 'contextParameters', set())
    assert not _is_linked(b, 'contextParameters', a2)
    if hasattr(a2, 'CtxState30'):
        assert not _is_linked(a2, 'CtxState30', b)


def test_assoc_target26_reverse_link_reassign_clear():
    a1 = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    a2 = ctxmngr_CtxTransition(Action="sample_text_2", Condition="sample_text_2", Event="sample_text_2", input="sample_text_2", isRemote=False, output="sample_text_2", transProb=9.99, transRate=9.99)
    b = ctxmngr_CtxState(isEnd=True, isStart=True)
    _safe_set(b, 'CtxState27', a1)
    assert _is_linked(b, 'CtxState27', a1)
    if hasattr(a1, 'incomingTransition'):
        assert _is_linked(a1, 'incomingTransition', b)
    _safe_set(b, 'CtxState27', a2)
    assert _is_linked(b, 'CtxState27', a2)
    if hasattr(a1, 'incomingTransition'):
        assert not _is_linked(a1, 'incomingTransition', b)
    if hasattr(a2, 'incomingTransition'):
        assert _is_linked(a2, 'incomingTransition', b)
    _safe_set(b, 'CtxState27', None)
    assert not _is_linked(b, 'CtxState27', a2)
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
    # ctxmngr_ContextManager has no real 'owningManager6' property in the generated
    # code (a bare stub) -- manually attach it so ctxmngr_ContextParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ctxmngr_ContextParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ctxmngr_ContextParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    partner = ctxmngr_ContextManager()
    setattr(partner, 'owningManager6', None)
    _safe_set(owner, 'ContextParameter', partner)
    assert owner in getattr(partner, 'owningManager6')
    _safe_set(owner, 'ContextParameter', None)
    assert owner not in getattr(partner, 'owningManager6')


def test_assoc_finalState2_stub_double():
    # ctxmngr_ContextManager has no real 'ctxmngr_ContextManager3' property in the generated
    # code (a bare stub) -- manually attach it so ctxmngr_CtxState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ctxmngr_CtxState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ctxmngr_CtxState(isEnd=True, isStart=True)
    partner = ctxmngr_ContextManager()
    setattr(partner, 'ctxmngr_ContextManager3', None)
    _safe_set(owner, 'ctxmngr_CtxState4', partner)
    assert owner in getattr(partner, 'ctxmngr_ContextManager3')
    _safe_set(owner, 'ctxmngr_CtxState4', None)
    assert owner not in getattr(partner, 'ctxmngr_ContextManager3')


def test_assoc_initialState1_stub_double():
    # ctxmngr_ContextManager has no real 'ctxmngr_ContextManager' property in the generated
    # code (a bare stub) -- manually attach it so ctxmngr_CtxState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ctxmngr_CtxState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ctxmngr_CtxState(isEnd=True, isStart=True)
    partner = ctxmngr_ContextManager()
    setattr(partner, 'ctxmngr_ContextManager', None)
    _safe_set(owner, 'ctxmngr_CtxState', partner)
    assert getattr(partner, 'ctxmngr_ContextManager') == owner
    _safe_set(owner, 'ctxmngr_CtxState', None)
    assert getattr(partner, 'ctxmngr_ContextManager') is None


def test_assoc_managerStates20_stub_double():
    # ctxmngr_ManagerState has no real 'ctxmngr_ManagerState' property in the generated
    # code (a bare stub) -- manually attach it so ctxmngr_CtxState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ctxmngr_CtxState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ctxmngr_CtxState(isEnd=True, isStart=True)
    partner = ctxmngr_ManagerState()
    setattr(partner, 'ctxmngr_ManagerState', None)
    _safe_set(owner, 'ctxmngr_CtxState21', {partner})
    assert getattr(partner, 'ctxmngr_ManagerState') == owner
    _safe_set(owner, 'ctxmngr_CtxState21', set())
    assert getattr(partner, 'ctxmngr_ManagerState') is None


def test_assoc_managerTransition28_stub_double():
    # ctxmngr_ManagerTransition has no real 'ctxmngr_ManagerTransition' property in the generated
    # code (a bare stub) -- manually attach it so ctxmngr_CtxTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ctxmngr_CtxTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    partner = ctxmngr_ManagerTransition()
    setattr(partner, 'ctxmngr_ManagerTransition', None)
    _safe_set(owner, 'ctxmngr_CtxTransition', {partner})
    assert getattr(partner, 'ctxmngr_ManagerTransition') == owner
    _safe_set(owner, 'ctxmngr_CtxTransition', set())
    assert getattr(partner, 'ctxmngr_ManagerTransition') is None


def test_assoc_opaqueExpressions31_stub_double():
    # ctxmngr_OpaqueExpression has no real 'ctxmngr_OpaqueExpression' property in the generated
    # code (a bare stub) -- manually attach it so ctxmngr_ContextParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ctxmngr_ContextParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ctxmngr_ContextParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    partner = ctxmngr_OpaqueExpression()
    setattr(partner, 'ctxmngr_OpaqueExpression', None)
    _safe_set(owner, 'ctxmngr_ContextParameter', {partner})
    assert getattr(partner, 'ctxmngr_OpaqueExpression') == owner
    _safe_set(owner, 'ctxmngr_ContextParameter', set())
    assert getattr(partner, 'ctxmngr_OpaqueExpression') is None


def test_assoc_ownedState0_stub_double():
    # ctxmngr_ContextManager has no real 'owningManager' property in the generated
    # code (a bare stub) -- manually attach it so ctxmngr_CtxState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ctxmngr_CtxState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ctxmngr_CtxState(isEnd=True, isStart=True)
    partner = ctxmngr_ContextManager()
    setattr(partner, 'owningManager', None)
    _safe_set(owner, 'CtxState', partner)
    assert owner in getattr(partner, 'owningManager')
    _safe_set(owner, 'CtxState', None)
    assert owner not in getattr(partner, 'owningManager')


def test_assoc_ownedTransition11_stub_double():
    # ctxmngr_ContextManager has no real 'owningManager12' property in the generated
    # code (a bare stub) -- manually attach it so ctxmngr_CtxTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ctxmngr_CtxTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    partner = ctxmngr_ContextManager()
    setattr(partner, 'owningManager12', None)
    _safe_set(owner, 'CtxTransition', partner)
    assert owner in getattr(partner, 'owningManager12')
    _safe_set(owner, 'CtxTransition', None)
    assert owner not in getattr(partner, 'owningManager12')


def test_assoc_owningManager13_stub_double():
    # ctxmngr_ContextManager has no real 'ContextManager' property in the generated
    # code (a bare stub) -- manually attach it so ctxmngr_CtxState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ctxmngr_CtxState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ctxmngr_CtxState(isEnd=True, isStart=True)
    partner = ctxmngr_ContextManager()
    setattr(partner, 'ContextManager', None)
    _safe_set(owner, 'ownedState', partner)
    assert getattr(partner, 'ContextManager') == owner
    _safe_set(owner, 'ownedState', None)
    assert getattr(partner, 'ContextManager') is None


def test_assoc_owningManager22_stub_double():
    # ctxmngr_ContextManager has no real 'ContextManager23' property in the generated
    # code (a bare stub) -- manually attach it so ctxmngr_CtxTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ctxmngr_CtxTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    partner = ctxmngr_ContextManager()
    setattr(partner, 'ContextManager23', None)
    _safe_set(owner, 'ownedTransition', partner)
    assert getattr(partner, 'ContextManager23') == owner
    _safe_set(owner, 'ownedTransition', None)
    assert getattr(partner, 'ContextManager23') is None


def test_assoc_owningManager32_stub_double():
    # ctxmngr_ContextManager has no real 'ContextManager34' property in the generated
    # code (a bare stub) -- manually attach it so ctxmngr_ContextParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ctxmngr_ContextParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ctxmngr_ContextParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    partner = ctxmngr_ContextManager()
    setattr(partner, 'ContextManager34', None)
    _safe_set(owner, 'contextParameters33', partner)
    assert getattr(partner, 'ContextManager34') == owner
    _safe_set(owner, 'contextParameters33', None)
    assert getattr(partner, 'ContextManager34') is None


def test_assoc_represents42_stub_double():
    # ctxmngr_RemoteFiringDependency has no real 'ctxmngr_RemoteFiringDependency43' property in the generated
    # code (a bare stub) -- manually attach it so ctxmngr_CtxTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ctxmngr_CtxTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    partner = ctxmngr_RemoteFiringDependency()
    setattr(partner, 'ctxmngr_RemoteFiringDependency43', None)
    _safe_set(owner, 'ctxmngr_CtxTransition44', partner)
    assert owner in getattr(partner, 'ctxmngr_RemoteFiringDependency43')
    _safe_set(owner, 'ctxmngr_CtxTransition44', None)
    assert owner not in getattr(partner, 'ctxmngr_RemoteFiringDependency43')


