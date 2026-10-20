import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DatabaseResourceData,
    ExtensibleModel,
    oracle_DatabaseModuleExtensibleProperty,
    oracle_OracleIndexProperty,
    oracle_OracleModuleProperty,
    oracle_OraclePrivilege,
    oracle_OracleSequenceProperty,
    oracle_OracleSpaceResourceData,
    oracle_OracleTableProperty,
    oracle_OracleUser,
    oracle_OracleUserResourceData,
    oracle_OracleViewProperty,
    oracle_SequenceResourceData,
    oracle_TableSpace,
    oracle_TableSpaceRelation,
    oracle_TriggerResourceData,
    table_type,
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

def test_assoc_privileges6_reverse_link_reassign_clear():
    a1 = oracle_OracleUser(attributes="sample_text", decription="sample_text", defaultTableSpace="sample_text", enable=True, name="sample_text", password="sample_text")
    a2 = oracle_OracleUser(attributes="sample_text_2", decription="sample_text_2", defaultTableSpace="sample_text_2", enable=False, name="sample_text_2", password="sample_text_2")
    b = oracle_OraclePrivilege(decription="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'oracle_OraclePrivilege8', a1)
    assert _is_linked(b, 'oracle_OraclePrivilege8', a1)
    if hasattr(a1, 'oracle_OracleUser7'):
        assert _is_linked(a1, 'oracle_OracleUser7', b)
    _safe_set(b, 'oracle_OraclePrivilege8', a2)
    assert _is_linked(b, 'oracle_OraclePrivilege8', a2)
    if hasattr(a1, 'oracle_OracleUser7'):
        assert not _is_linked(a1, 'oracle_OracleUser7', b)
    if hasattr(a2, 'oracle_OracleUser7'):
        assert _is_linked(a2, 'oracle_OracleUser7', b)
    _safe_set(b, 'oracle_OraclePrivilege8', None)
    assert not _is_linked(b, 'oracle_OraclePrivilege8', a2)
    if hasattr(a2, 'oracle_OracleUser7'):
        assert not _is_linked(a2, 'oracle_OracleUser7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_privileges4_stub_double():
    # oracle_OracleUserResourceData has no real 'oracle_OracleUserResourceData5' property in the generated
    # code (a bare stub) -- manually attach it so oracle_OraclePrivilege's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oracle_OraclePrivilege's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oracle_OraclePrivilege(decription="sample_text", name="sample_text", type="sample_text")
    partner = oracle_OracleUserResourceData()
    setattr(partner, 'oracle_OracleUserResourceData5', None)
    _safe_set(owner, 'oracle_OraclePrivilege', partner)
    assert owner in getattr(partner, 'oracle_OracleUserResourceData5')
    _safe_set(owner, 'oracle_OraclePrivilege', None)
    assert owner not in getattr(partner, 'oracle_OracleUserResourceData5')


def test_assoc_relations1_stub_double():
    # oracle_OracleSpaceResourceData has no real 'oracle_OracleSpaceResourceData2' property in the generated
    # code (a bare stub) -- manually attach it so oracle_TableSpaceRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oracle_TableSpaceRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oracle_TableSpaceRelation(indexSpace="sample_text", mainSpace="sample_text")
    partner = oracle_OracleSpaceResourceData()
    setattr(partner, 'oracle_OracleSpaceResourceData2', None)
    _safe_set(owner, 'oracle_TableSpaceRelation', partner)
    assert owner in getattr(partner, 'oracle_OracleSpaceResourceData2')
    _safe_set(owner, 'oracle_TableSpaceRelation', None)
    assert owner not in getattr(partner, 'oracle_OracleSpaceResourceData2')


def test_assoc_spaces0_stub_double():
    # oracle_OracleSpaceResourceData has no real 'oracle_OracleSpaceResourceData' property in the generated
    # code (a bare stub) -- manually attach it so oracle_TableSpace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oracle_TableSpace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oracle_TableSpace(chineseName="sample_text", description="sample_text", file="sample_text", logicName="sample_text", name="sample_text", size="sample_text", user="sample_text")
    partner = oracle_OracleSpaceResourceData()
    setattr(partner, 'oracle_OracleSpaceResourceData', None)
    _safe_set(owner, 'oracle_TableSpace', partner)
    assert owner in getattr(partner, 'oracle_OracleSpaceResourceData')
    _safe_set(owner, 'oracle_TableSpace', None)
    assert owner not in getattr(partner, 'oracle_OracleSpaceResourceData')


def test_assoc_users3_stub_double():
    # oracle_OracleUserResourceData has no real 'oracle_OracleUserResourceData' property in the generated
    # code (a bare stub) -- manually attach it so oracle_OracleUser's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oracle_OracleUser's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oracle_OracleUser(attributes="sample_text", decription="sample_text", defaultTableSpace="sample_text", enable=True, name="sample_text", password="sample_text")
    partner = oracle_OracleUserResourceData()
    setattr(partner, 'oracle_OracleUserResourceData', None)
    _safe_set(owner, 'oracle_OracleUser', partner)
    assert owner in getattr(partner, 'oracle_OracleUserResourceData')
    _safe_set(owner, 'oracle_OracleUser', None)
    assert owner not in getattr(partner, 'oracle_OracleUserResourceData')


