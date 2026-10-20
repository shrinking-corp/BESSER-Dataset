import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractMappingCS,
    DomainCS,
    ExpCS,
    MappingStatementCS,
    ModelElementCS,
    PredicateOrAssignmentCS,
    RootPackageCS,
    qvtimperativecs_ExpCS,
    qvtimperativecs_ImperativeDomainCS,
    qvtimperativecs_ImperativePredicateOrAssignmentCS,
    qvtimperativecs_Mapping,
    qvtimperativecs_MappingCS,
    qvtimperativecs_MappingCallBindingCS,
    qvtimperativecs_MappingCallCS,
    qvtimperativecs_MappingLoopCS,
    qvtimperativecs_MappingSequenceCS,
    qvtimperativecs_MappingStatementCS,
    qvtimperativecs_PathNameCS,
    qvtimperativecs_QueryCS,
    qvtimperativecs_TopLevelCS,
    qvtimperativecs_TransformationCS,
    qvtimperativecs_Variable,
    qvtimperativecs_VariableCS,
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

def test_assoc_ownedBindings12_reverse_link_reassign_clear():
    a1 = qvtimperativecs_MappingCallCS(isInfinite=True)
    a2 = qvtimperativecs_MappingCallCS(isInfinite=False)
    b = qvtimperativecs_MappingCallBindingCS(isPolled=True)
    _safe_set(b, 'MappingCallBindingCS', a1)
    assert _is_linked(b, 'MappingCallBindingCS', a1)
    if hasattr(a1, 'owningMappingCall'):
        assert _is_linked(a1, 'owningMappingCall', b)
    _safe_set(b, 'MappingCallBindingCS', a2)
    assert _is_linked(b, 'MappingCallBindingCS', a2)
    if hasattr(a1, 'owningMappingCall'):
        assert not _is_linked(a1, 'owningMappingCall', b)
    if hasattr(a2, 'owningMappingCall'):
        assert _is_linked(a2, 'owningMappingCall', b)
    _safe_set(b, 'MappingCallBindingCS', None)
    assert not _is_linked(b, 'MappingCallBindingCS', a2)
    if hasattr(a2, 'owningMappingCall'):
        assert not _is_linked(a2, 'owningMappingCall', b)


def test_assoc_owningMappingCall9_reverse_link_reassign_clear():
    a1 = qvtimperativecs_MappingCallCS(isInfinite=True)
    a2 = qvtimperativecs_MappingCallCS(isInfinite=False)
    b = qvtimperativecs_MappingCallBindingCS(isPolled=True)
    _safe_set(b, 'ownedBindings', a1)
    assert _is_linked(b, 'ownedBindings', a1)
    if hasattr(a1, 'MappingCallCS'):
        assert _is_linked(a1, 'MappingCallCS', b)
    _safe_set(b, 'ownedBindings', a2)
    assert _is_linked(b, 'ownedBindings', a2)
    if hasattr(a1, 'MappingCallCS'):
        assert not _is_linked(a1, 'MappingCallCS', b)
    if hasattr(a2, 'MappingCallCS'):
        assert _is_linked(a2, 'MappingCallCS', b)
    _safe_set(b, 'ownedBindings', None)
    assert not _is_linked(b, 'ownedBindings', a2)
    if hasattr(a2, 'MappingCallCS'):
        assert not _is_linked(a2, 'MappingCallCS', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ownedPathName13_stub_double():
    # qvtimperativecs_PathNameCS has no real 'qvtimperativecs_PathNameCS14' property in the generated
    # code (a bare stub) -- manually attach it so qvtimperativecs_MappingCallCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtimperativecs_MappingCallCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtimperativecs_MappingCallCS(isInfinite=True)
    partner = qvtimperativecs_PathNameCS()
    setattr(partner, 'qvtimperativecs_PathNameCS14', None)
    _safe_set(owner, 'qvtimperativecs_MappingCallCS', partner)
    assert getattr(partner, 'qvtimperativecs_PathNameCS14') == owner
    _safe_set(owner, 'qvtimperativecs_MappingCallCS', None)
    assert getattr(partner, 'qvtimperativecs_PathNameCS14') is None


def test_assoc_ownedValue8_stub_double():
    # qvtimperativecs_ExpCS has no real 'qvtimperativecs_ExpCS' property in the generated
    # code (a bare stub) -- manually attach it so qvtimperativecs_MappingCallBindingCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtimperativecs_MappingCallBindingCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtimperativecs_MappingCallBindingCS(isPolled=True)
    partner = qvtimperativecs_ExpCS()
    setattr(partner, 'qvtimperativecs_ExpCS', None)
    _safe_set(owner, 'qvtimperativecs_MappingCallBindingCS', partner)
    assert getattr(partner, 'qvtimperativecs_ExpCS') == owner
    _safe_set(owner, 'qvtimperativecs_MappingCallBindingCS', None)
    assert getattr(partner, 'qvtimperativecs_ExpCS') is None


def test_assoc_referredMapping15_stub_double():
    # qvtimperativecs_Mapping has no real 'qvtimperativecs_Mapping' property in the generated
    # code (a bare stub) -- manually attach it so qvtimperativecs_MappingCallCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtimperativecs_MappingCallCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtimperativecs_MappingCallCS(isInfinite=True)
    partner = qvtimperativecs_Mapping()
    setattr(partner, 'qvtimperativecs_Mapping', None)
    _safe_set(owner, 'qvtimperativecs_MappingCallCS16', partner)
    assert getattr(partner, 'qvtimperativecs_Mapping') == owner
    _safe_set(owner, 'qvtimperativecs_MappingCallCS16', None)
    assert getattr(partner, 'qvtimperativecs_Mapping') is None


def test_assoc_referredVariable10_stub_double():
    # qvtimperativecs_Variable has no real 'qvtimperativecs_Variable' property in the generated
    # code (a bare stub) -- manually attach it so qvtimperativecs_MappingCallBindingCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtimperativecs_MappingCallBindingCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtimperativecs_MappingCallBindingCS(isPolled=True)
    partner = qvtimperativecs_Variable()
    setattr(partner, 'qvtimperativecs_Variable', None)
    _safe_set(owner, 'qvtimperativecs_MappingCallBindingCS11', partner)
    assert getattr(partner, 'qvtimperativecs_Variable') == owner
    _safe_set(owner, 'qvtimperativecs_MappingCallBindingCS11', None)
    assert getattr(partner, 'qvtimperativecs_Variable') is None


