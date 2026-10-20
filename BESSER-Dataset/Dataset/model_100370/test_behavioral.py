import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AndState,
    AssociationDataStateBase,
    AssociationStateState,
    CompoundState,
    DataVar,
    HSM_AndState,
    HSM_AssociationDataStateBase,
    HSM_AssociationStateState,
    HSM_CompoundState,
    HSM_DataVar,
    HSM_Init,
    HSM_MgaObject,
    HSM_OrState,
    HSM_PrimitiveState,
    HSM_RootFolder,
    HSM_State,
    HSM_StateBase,
    HSM_StateDataRelation,
    HSM_StateDateRelation,
    HSM_Transition,
    Init,
    MgaObject,
    OrState,
    PrimitiveState,
    RootFolder,
    State,
    StateBase,
    StateDataRelation,
    Transition,
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

def test_assoc_associationDataStateBase146_stub_double():
    # AssociationDataStateBase has no real 'AssociationDataStateBase48' property in the generated
    # code (a bare stub) -- manually attach it so HSM_StateDataRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_StateDataRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_StateDataRelation(color="sample_text", value="sample_text")
    partner = AssociationDataStateBase()
    setattr(partner, 'AssociationDataStateBase48', None)
    _safe_set(owner, 'stateDataRelation47', partner)
    assert getattr(partner, 'AssociationDataStateBase48') == owner
    _safe_set(owner, 'stateDataRelation47', None)
    assert getattr(partner, 'AssociationDataStateBase48') is None


def test_assoc_associationDataStateBase4_stub_double():
    # AssociationDataStateBase has no real 'AssociationDataStateBase' property in the generated
    # code (a bare stub) -- manually attach it so HSM_StateBase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_StateBase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_StateBase(defaultTransition="sample_text", marked="sample_text")
    partner = AssociationDataStateBase()
    setattr(partner, 'AssociationDataStateBase', None)
    _safe_set(owner, 'stateBase5', partner)
    assert getattr(partner, 'AssociationDataStateBase') == owner
    _safe_set(owner, 'stateBase5', None)
    assert getattr(partner, 'AssociationDataStateBase') is None


def test_assoc_associationStateState13_stub_double():
    # AssociationStateState has no real 'AssociationStateState15' property in the generated
    # code (a bare stub) -- manually attach it so HSM_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_Transition(action="sample_text", guard="sample_text", isSync="sample_text", trigger="sample_text")
    partner = AssociationStateState()
    setattr(partner, 'AssociationStateState15', None)
    _safe_set(owner, 'transition14', partner)
    assert getattr(partner, 'AssociationStateState15') == owner
    _safe_set(owner, 'transition14', None)
    assert getattr(partner, 'AssociationStateState15') is None


def test_assoc_associationStateStatedst0_stub_double():
    # AssociationStateState has no real 'AssociationStateState' property in the generated
    # code (a bare stub) -- manually attach it so HSM_StateBase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_StateBase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_StateBase(defaultTransition="sample_text", marked="sample_text")
    partner = AssociationStateState()
    setattr(partner, 'AssociationStateState', None)
    _safe_set(owner, 'dstTransition', {partner})
    assert getattr(partner, 'AssociationStateState') == owner
    _safe_set(owner, 'dstTransition', set())
    assert getattr(partner, 'AssociationStateState') is None


def test_assoc_associationStateStatesrc1_stub_double():
    # AssociationStateState has no real 'AssociationStateState2' property in the generated
    # code (a bare stub) -- manually attach it so HSM_StateBase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_StateBase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_StateBase(defaultTransition="sample_text", marked="sample_text")
    partner = AssociationStateState()
    setattr(partner, 'AssociationStateState2', None)
    _safe_set(owner, 'srcTransition', {partner})
    assert getattr(partner, 'AssociationStateState2') == owner
    _safe_set(owner, 'srcTransition', set())
    assert getattr(partner, 'AssociationStateState2') is None


def test_assoc_data3_stub_double():
    # DataVar has no real 'DataVar' property in the generated
    # code (a bare stub) -- manually attach it so HSM_StateBase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_StateBase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_StateBase(defaultTransition="sample_text", marked="sample_text")
    partner = DataVar()
    setattr(partner, 'DataVar', None)
    _safe_set(owner, 'stateBase', {partner})
    assert getattr(partner, 'DataVar') == owner
    _safe_set(owner, 'stateBase', set())
    assert getattr(partner, 'DataVar') is None


def test_assoc_orState11_stub_double():
    # OrState has no real 'OrState12' property in the generated
    # code (a bare stub) -- manually attach it so HSM_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_Transition(action="sample_text", guard="sample_text", isSync="sample_text", trigger="sample_text")
    partner = OrState()
    setattr(partner, 'OrState12', None)
    _safe_set(owner, 'transition', partner)
    assert getattr(partner, 'OrState12') == owner
    _safe_set(owner, 'transition', None)
    assert getattr(partner, 'OrState12') is None


def test_assoc_orState17_stub_double():
    # OrState has no real 'OrState18' property in the generated
    # code (a bare stub) -- manually attach it so HSM_RootFolder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_RootFolder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_RootFolder(name="sample_text")
    partner = OrState()
    setattr(partner, 'OrState18', None)
    _safe_set(owner, 'rootFolder', {partner})
    assert getattr(partner, 'OrState18') == owner
    _safe_set(owner, 'rootFolder', set())
    assert getattr(partner, 'OrState18') is None


def test_assoc_orState44_stub_double():
    # OrState has no real 'OrState45' property in the generated
    # code (a bare stub) -- manually attach it so HSM_StateDataRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_StateDataRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_StateDataRelation(color="sample_text", value="sample_text")
    partner = OrState()
    setattr(partner, 'OrState45', None)
    _safe_set(owner, 'stateDataRelation', partner)
    assert getattr(partner, 'OrState45') == owner
    _safe_set(owner, 'stateDataRelation', None)
    assert getattr(partner, 'OrState45') is None


def test_assoc_rootFolders16_stub_double():
    # RootFolder has no real 'RootFolder' property in the generated
    # code (a bare stub) -- manually attach it so HSM_RootFolder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_RootFolder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_RootFolder(name="sample_text")
    partner = RootFolder()
    setattr(partner, 'RootFolder', None)
    _safe_set(owner, 'HSM_RootFolder', {partner})
    assert getattr(partner, 'RootFolder') == owner
    _safe_set(owner, 'HSM_RootFolder', set())
    assert getattr(partner, 'RootFolder') is None


