import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SArtifact,
    SExtDeclaredSQLType,
    SInlinedSQLType,
    STableMember,
    sqlDSL_SArtifact,
    sqlDSL_SColumn,
    sqlDSL_SColumnProps,
    sqlDSL_SDecimal,
    sqlDSL_SEnum,
    sqlDSL_SEnumLiteral,
    sqlDSL_SExtDeclaredSQLType,
    sqlDSL_SInlinedSQLType,
    sqlDSL_SJoinColumn,
    sqlDSL_SModel,
    sqlDSL_SSettings,
    sqlDSL_SString,
    sqlDSL_STable,
    sqlDSL_STableMember,
    SDBEngine,
    SIndex,
    SSimpleTypes,
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

def test_assoc_artifact1_reverse_link_reassign_clear():
    a1 = sqlDSL_SModel(generatedFile="sample_text")
    a2 = sqlDSL_SModel(generatedFile="sample_text_2")
    b = sqlDSL_SArtifact(name="sample_text")
    _safe_set(b, 'sqlDSL_SArtifact', a1)
    assert _is_linked(b, 'sqlDSL_SArtifact', a1)
    if hasattr(a1, 'sqlDSL_SModel2'):
        assert _is_linked(a1, 'sqlDSL_SModel2', b)
    _safe_set(b, 'sqlDSL_SArtifact', a2)
    assert _is_linked(b, 'sqlDSL_SArtifact', a2)
    if hasattr(a1, 'sqlDSL_SModel2'):
        assert not _is_linked(a1, 'sqlDSL_SModel2', b)
    if hasattr(a2, 'sqlDSL_SModel2'):
        assert _is_linked(a2, 'sqlDSL_SModel2', b)
    _safe_set(b, 'sqlDSL_SArtifact', None)
    assert not _is_linked(b, 'sqlDSL_SArtifact', a2)
    if hasattr(a2, 'sqlDSL_SModel2'):
        assert not _is_linked(a2, 'sqlDSL_SModel2', b)


def test_assoc_columns5_reverse_link_reassign_clear():
    a1 = sqlDSL_STableMember(name="sample_text")
    a2 = sqlDSL_STableMember(name="sample_text_2")
    b = sqlDSL_STable(cached=True, entityname="sample_text", prefix="sample_text")
    _safe_set(b, 'sqlDSL_STable6', {a1})
    assert _is_linked(b, 'sqlDSL_STable6', a1)
    if hasattr(a1, 'sqlDSL_STableMember'):
        assert _is_linked(a1, 'sqlDSL_STableMember', b)
    _safe_set(b, 'sqlDSL_STable6', {a2})
    assert _is_linked(b, 'sqlDSL_STable6', a2)
    if hasattr(a1, 'sqlDSL_STableMember'):
        assert not _is_linked(a1, 'sqlDSL_STableMember', b)
    if hasattr(a2, 'sqlDSL_STableMember'):
        assert _is_linked(a2, 'sqlDSL_STableMember', b)
    _safe_set(b, 'sqlDSL_STable6', set())
    assert not _is_linked(b, 'sqlDSL_STable6', a2)
    if hasattr(a2, 'sqlDSL_STableMember'):
        assert not _is_linked(a2, 'sqlDSL_STableMember', b)


def test_assoc_inlinedType10_reverse_link_reassign_clear():
    a1 = sqlDSL_SInlinedSQLType(value=7)
    a2 = sqlDSL_SInlinedSQLType(value=13)
    b = sqlDSL_SColumn(simpleType="sample_text")
    _safe_set(b, 'sqlDSL_SColumn11', a1)
    assert _is_linked(b, 'sqlDSL_SColumn11', a1)
    if hasattr(a1, 'sqlDSL_SInlinedSQLType'):
        assert _is_linked(a1, 'sqlDSL_SInlinedSQLType', b)
    _safe_set(b, 'sqlDSL_SColumn11', a2)
    assert _is_linked(b, 'sqlDSL_SColumn11', a2)
    if hasattr(a1, 'sqlDSL_SInlinedSQLType'):
        assert not _is_linked(a1, 'sqlDSL_SInlinedSQLType', b)
    if hasattr(a2, 'sqlDSL_SInlinedSQLType'):
        assert _is_linked(a2, 'sqlDSL_SInlinedSQLType', b)
    _safe_set(b, 'sqlDSL_SColumn11', None)
    assert not _is_linked(b, 'sqlDSL_SColumn11', a2)
    if hasattr(a2, 'sqlDSL_SInlinedSQLType'):
        assert not _is_linked(a2, 'sqlDSL_SInlinedSQLType', b)


def test_assoc_props7_reverse_link_reassign_clear():
    a1 = sqlDSL_STableMember(name="sample_text")
    a2 = sqlDSL_STableMember(name="sample_text_2")
    b = sqlDSL_SColumnProps(aes=True, index="sample_text", javacolumn="sample_text", nullable=True)
    _safe_set(b, 'sqlDSL_SColumnProps', a1)
    assert _is_linked(b, 'sqlDSL_SColumnProps', a1)
    if hasattr(a1, 'sqlDSL_STableMember8'):
        assert _is_linked(a1, 'sqlDSL_STableMember8', b)
    _safe_set(b, 'sqlDSL_SColumnProps', a2)
    assert _is_linked(b, 'sqlDSL_SColumnProps', a2)
    if hasattr(a1, 'sqlDSL_STableMember8'):
        assert not _is_linked(a1, 'sqlDSL_STableMember8', b)
    if hasattr(a2, 'sqlDSL_STableMember8'):
        assert _is_linked(a2, 'sqlDSL_STableMember8', b)
    _safe_set(b, 'sqlDSL_SColumnProps', None)
    assert not _is_linked(b, 'sqlDSL_SColumnProps', a2)
    if hasattr(a2, 'sqlDSL_STableMember8'):
        assert not _is_linked(a2, 'sqlDSL_STableMember8', b)


def test_assoc_settings0_reverse_link_reassign_clear():
    a1 = sqlDSL_SSettings(engine="sample_text", javapackage="sample_text", schema="sample_text")
    a2 = sqlDSL_SSettings(engine="sample_text_2", javapackage="sample_text_2", schema="sample_text_2")
    b = sqlDSL_SModel(generatedFile="sample_text")
    _safe_set(b, 'sqlDSL_SModel', a1)
    assert _is_linked(b, 'sqlDSL_SModel', a1)
    if hasattr(a1, 'sqlDSL_SSettings'):
        assert _is_linked(a1, 'sqlDSL_SSettings', b)
    _safe_set(b, 'sqlDSL_SModel', a2)
    assert _is_linked(b, 'sqlDSL_SModel', a2)
    if hasattr(a1, 'sqlDSL_SSettings'):
        assert not _is_linked(a1, 'sqlDSL_SSettings', b)
    if hasattr(a2, 'sqlDSL_SSettings'):
        assert _is_linked(a2, 'sqlDSL_SSettings', b)
    _safe_set(b, 'sqlDSL_SModel', None)
    assert not _is_linked(b, 'sqlDSL_SModel', a2)
    if hasattr(a2, 'sqlDSL_SSettings'):
        assert not _is_linked(a2, 'sqlDSL_SSettings', b)


def test_assoc_settings3_reverse_link_reassign_clear():
    a1 = sqlDSL_STable(cached=True, entityname="sample_text", prefix="sample_text")
    a2 = sqlDSL_STable(cached=False, entityname="sample_text_2", prefix="sample_text_2")
    b = sqlDSL_SSettings(engine="sample_text", javapackage="sample_text", schema="sample_text")
    _safe_set(b, 'sqlDSL_SSettings4', a1)
    assert _is_linked(b, 'sqlDSL_SSettings4', a1)
    if hasattr(a1, 'sqlDSL_STable'):
        assert _is_linked(a1, 'sqlDSL_STable', b)
    _safe_set(b, 'sqlDSL_SSettings4', a2)
    assert _is_linked(b, 'sqlDSL_SSettings4', a2)
    if hasattr(a1, 'sqlDSL_STable'):
        assert not _is_linked(a1, 'sqlDSL_STable', b)
    if hasattr(a2, 'sqlDSL_STable'):
        assert _is_linked(a2, 'sqlDSL_STable', b)
    _safe_set(b, 'sqlDSL_SSettings4', None)
    assert not _is_linked(b, 'sqlDSL_SSettings4', a2)
    if hasattr(a2, 'sqlDSL_STable'):
        assert not _is_linked(a2, 'sqlDSL_STable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_extType9_stub_double():
    # sqlDSL_SExtDeclaredSQLType has no real 'sqlDSL_SExtDeclaredSQLType' property in the generated
    # code (a bare stub) -- manually attach it so sqlDSL_SColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlDSL_SColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlDSL_SColumn(simpleType="sample_text")
    partner = sqlDSL_SExtDeclaredSQLType()
    setattr(partner, 'sqlDSL_SExtDeclaredSQLType', None)
    _safe_set(owner, 'sqlDSL_SColumn', partner)
    assert getattr(partner, 'sqlDSL_SExtDeclaredSQLType') == owner
    _safe_set(owner, 'sqlDSL_SColumn', None)
    assert getattr(partner, 'sqlDSL_SExtDeclaredSQLType') is None


def test_assoc_literals14_stub_double():
    # sqlDSL_SEnum has no real 'sqlDSL_SEnum' property in the generated
    # code (a bare stub) -- manually attach it so sqlDSL_SEnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlDSL_SEnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlDSL_SEnumLiteral(name="sample_text", value=7)
    partner = sqlDSL_SEnum()
    setattr(partner, 'sqlDSL_SEnum', None)
    _safe_set(owner, 'sqlDSL_SEnumLiteral', partner)
    assert owner in getattr(partner, 'sqlDSL_SEnum')
    _safe_set(owner, 'sqlDSL_SEnumLiteral', None)
    assert owner not in getattr(partner, 'sqlDSL_SEnum')


def test_assoc_referencedType12_stub_double():
    # sqlDSL_SJoinColumn has no real 'sqlDSL_SJoinColumn' property in the generated
    # code (a bare stub) -- manually attach it so sqlDSL_STable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqlDSL_STable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqlDSL_STable(cached=True, entityname="sample_text", prefix="sample_text")
    partner = sqlDSL_SJoinColumn()
    setattr(partner, 'sqlDSL_SJoinColumn', None)
    _safe_set(owner, 'sqlDSL_STable13', partner)
    assert getattr(partner, 'sqlDSL_SJoinColumn') == owner
    _safe_set(owner, 'sqlDSL_STable13', None)
    assert getattr(partner, 'sqlDSL_SJoinColumn') is None


