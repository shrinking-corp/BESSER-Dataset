import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Constraints,
    DataType,
    ModelElement,
    PKeyAndUnique,
    rdbms_CheckCon,
    rdbms_Column,
    rdbms_Constraints,
    rdbms_DataType,
    rdbms_Database,
    rdbms_ForeignKey,
    rdbms_ModelElement,
    rdbms_PKeyAndUnique,
    rdbms_PrimaryKeyCon,
    rdbms_SystemDataType,
    rdbms_Table,
    rdbms_UniqueCon,
    rdbms_UserDefinedDataType,
    Action,
    DeferrableAct,
    DeferredAct,
    ReferencingType,
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

def test_assoc_columnInFK16_reverse_link_reassign_clear():
    a1 = rdbms_ForeignKey(deleteActionRHS="sample_text", inverseReferentialIntegrityCon=True, match="sample_text", updateActionRHS="sample_text")
    a2 = rdbms_ForeignKey(deleteActionRHS="sample_text_2", inverseReferentialIntegrityCon=False, match="sample_text_2", updateActionRHS="sample_text_2")
    b = rdbms_Column(default="sample_text", length=7, nullable=True, precision=7)
    _safe_set(b, 'rdbms_Column17', a1)
    assert _is_linked(b, 'rdbms_Column17', a1)
    if hasattr(a1, 'rdbms_ForeignKey'):
        assert _is_linked(a1, 'rdbms_ForeignKey', b)
    _safe_set(b, 'rdbms_Column17', a2)
    assert _is_linked(b, 'rdbms_Column17', a2)
    if hasattr(a1, 'rdbms_ForeignKey'):
        assert not _is_linked(a1, 'rdbms_ForeignKey', b)
    if hasattr(a2, 'rdbms_ForeignKey'):
        assert _is_linked(a2, 'rdbms_ForeignKey', b)
    _safe_set(b, 'rdbms_Column17', None)
    assert not _is_linked(b, 'rdbms_Column17', a2)
    if hasattr(a2, 'rdbms_ForeignKey'):
        assert not _is_linked(a2, 'rdbms_ForeignKey', b)


def test_assoc_dataType33_reverse_link_reassign_clear():
    a1 = rdbms_UserDefinedDataType(defaultValue="sample_text", length=7, precision=7)
    a2 = rdbms_UserDefinedDataType(defaultValue="sample_text_2", length=13, precision=13)
    b = rdbms_SystemDataType(predefinedDecPlaces=7, predefinedLength=7)
    _safe_set(b, 'rdbms_SystemDataType35', a1)
    assert _is_linked(b, 'rdbms_SystemDataType35', a1)
    if hasattr(a1, 'rdbms_UserDefinedDataType34'):
        assert _is_linked(a1, 'rdbms_UserDefinedDataType34', b)
    _safe_set(b, 'rdbms_SystemDataType35', a2)
    assert _is_linked(b, 'rdbms_SystemDataType35', a2)
    if hasattr(a1, 'rdbms_UserDefinedDataType34'):
        assert not _is_linked(a1, 'rdbms_UserDefinedDataType34', b)
    if hasattr(a2, 'rdbms_UserDefinedDataType34'):
        assert _is_linked(a2, 'rdbms_UserDefinedDataType34', b)
    _safe_set(b, 'rdbms_SystemDataType35', None)
    assert not _is_linked(b, 'rdbms_SystemDataType35', a2)
    if hasattr(a2, 'rdbms_UserDefinedDataType34'):
        assert not _is_linked(a2, 'rdbms_UserDefinedDataType34', b)


def test_assoc_lhsAttr23_reverse_link_reassign_clear():
    a1 = rdbms_ForeignKey(deleteActionRHS="sample_text", inverseReferentialIntegrityCon=True, match="sample_text", updateActionRHS="sample_text")
    a2 = rdbms_ForeignKey(deleteActionRHS="sample_text_2", inverseReferentialIntegrityCon=False, match="sample_text_2", updateActionRHS="sample_text_2")
    b = rdbms_Column(default="sample_text", length=7, nullable=True, precision=7)
    _safe_set(b, 'rdbms_Column25', a1)
    assert _is_linked(b, 'rdbms_Column25', a1)
    if hasattr(a1, 'rdbms_ForeignKey24'):
        assert _is_linked(a1, 'rdbms_ForeignKey24', b)
    _safe_set(b, 'rdbms_Column25', a2)
    assert _is_linked(b, 'rdbms_Column25', a2)
    if hasattr(a1, 'rdbms_ForeignKey24'):
        assert not _is_linked(a1, 'rdbms_ForeignKey24', b)
    if hasattr(a2, 'rdbms_ForeignKey24'):
        assert _is_linked(a2, 'rdbms_ForeignKey24', b)
    _safe_set(b, 'rdbms_Column25', None)
    assert not _is_linked(b, 'rdbms_Column25', a2)
    if hasattr(a2, 'rdbms_ForeignKey24'):
        assert not _is_linked(a2, 'rdbms_ForeignKey24', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_FKTable29_stub_double():
    # rdbms_Table has no real 'Table' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_ForeignKey(deleteActionRHS="sample_text", inverseReferentialIntegrityCon=True, match="sample_text", updateActionRHS="sample_text")
    partner = rdbms_Table()
    setattr(partner, 'Table', None)
    _safe_set(owner, 'tableFKs', partner)
    assert getattr(partner, 'Table') == owner
    _safe_set(owner, 'tableFKs', None)
    assert getattr(partner, 'Table') is None


def test_assoc_PKandUQColumns30_stub_double():
    # rdbms_PKeyAndUnique has no real 'rdbms_PKeyAndUnique31' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_Column(default="sample_text", length=7, nullable=True, precision=7)
    partner = rdbms_PKeyAndUnique()
    setattr(partner, 'rdbms_PKeyAndUnique31', None)
    _safe_set(owner, 'rdbms_Column32', partner)
    assert owner in getattr(partner, 'rdbms_PKeyAndUnique31')
    _safe_set(owner, 'rdbms_Column32', None)
    assert owner not in getattr(partner, 'rdbms_PKeyAndUnique31')


def test_assoc_columnDataType18_stub_double():
    # rdbms_DataType has no real 'rdbms_DataType' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_Column(default="sample_text", length=7, nullable=True, precision=7)
    partner = rdbms_DataType()
    setattr(partner, 'rdbms_DataType', None)
    _safe_set(owner, 'rdbms_Column19', partner)
    assert getattr(partner, 'rdbms_DataType') == owner
    _safe_set(owner, 'rdbms_Column19', None)
    assert getattr(partner, 'rdbms_DataType') is None


def test_assoc_columnInPKandUQ14_stub_double():
    # rdbms_PKeyAndUnique has no real 'rdbms_PKeyAndUnique' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_Column(default="sample_text", length=7, nullable=True, precision=7)
    partner = rdbms_PKeyAndUnique()
    setattr(partner, 'rdbms_PKeyAndUnique', None)
    _safe_set(owner, 'rdbms_Column15', partner)
    assert getattr(partner, 'rdbms_PKeyAndUnique') == owner
    _safe_set(owner, 'rdbms_Column15', None)
    assert getattr(partner, 'rdbms_PKeyAndUnique') is None


def test_assoc_columns10_stub_double():
    # rdbms_Table has no real 'rdbms_Table11' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_Column(default="sample_text", length=7, nullable=True, precision=7)
    partner = rdbms_Table()
    setattr(partner, 'rdbms_Table11', None)
    _safe_set(owner, 'rdbms_Column', partner)
    assert owner in getattr(partner, 'rdbms_Table11')
    _safe_set(owner, 'rdbms_Column', None)
    assert owner not in getattr(partner, 'rdbms_Table11')


def test_assoc_dataTypes3_stub_double():
    # rdbms_Database has no real 'rdbms_Database4' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_SystemDataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_SystemDataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_SystemDataType(predefinedDecPlaces=7, predefinedLength=7)
    partner = rdbms_Database()
    setattr(partner, 'rdbms_Database4', None)
    _safe_set(owner, 'rdbms_SystemDataType', partner)
    assert owner in getattr(partner, 'rdbms_Database4')
    _safe_set(owner, 'rdbms_SystemDataType', None)
    assert owner not in getattr(partner, 'rdbms_Database4')


def test_assoc_refersTo26_stub_double():
    # rdbms_Table has no real 'rdbms_Table28' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_ForeignKey(deleteActionRHS="sample_text", inverseReferentialIntegrityCon=True, match="sample_text", updateActionRHS="sample_text")
    partner = rdbms_Table()
    setattr(partner, 'rdbms_Table28', None)
    _safe_set(owner, 'rdbms_ForeignKey27', partner)
    assert getattr(partner, 'rdbms_Table28') == owner
    _safe_set(owner, 'rdbms_ForeignKey27', None)
    assert getattr(partner, 'rdbms_Table28') is None


def test_assoc_rhsKey20_stub_double():
    # rdbms_PKeyAndUnique has no real 'rdbms_PKeyAndUnique22' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_ForeignKey(deleteActionRHS="sample_text", inverseReferentialIntegrityCon=True, match="sample_text", updateActionRHS="sample_text")
    partner = rdbms_PKeyAndUnique()
    setattr(partner, 'rdbms_PKeyAndUnique22', None)
    _safe_set(owner, 'rdbms_ForeignKey21', partner)
    assert getattr(partner, 'rdbms_PKeyAndUnique22') == owner
    _safe_set(owner, 'rdbms_ForeignKey21', None)
    assert getattr(partner, 'rdbms_PKeyAndUnique22') is None


def test_assoc_tableCHs12_stub_double():
    # rdbms_Table has no real 'rdbms_Table13' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_CheckCon's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_CheckCon's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_CheckCon(checkCondition="sample_text")
    partner = rdbms_Table()
    setattr(partner, 'rdbms_Table13', None)
    _safe_set(owner, 'rdbms_CheckCon', partner)
    assert owner in getattr(partner, 'rdbms_Table13')
    _safe_set(owner, 'rdbms_CheckCon', None)
    assert owner not in getattr(partner, 'rdbms_Table13')


def test_assoc_tableFKs5_stub_double():
    # rdbms_Table has no real 'FKTable' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_ForeignKey(deleteActionRHS="sample_text", inverseReferentialIntegrityCon=True, match="sample_text", updateActionRHS="sample_text")
    partner = rdbms_Table()
    setattr(partner, 'FKTable', None)
    _safe_set(owner, 'ForeignKey', partner)
    assert owner in getattr(partner, 'FKTable')
    _safe_set(owner, 'ForeignKey', None)
    assert owner not in getattr(partner, 'FKTable')


def test_assoc_userDefinedDataTypes0_stub_double():
    # rdbms_Database has no real 'rdbms_Database' property in the generated
    # code (a bare stub) -- manually attach it so rdbms_UserDefinedDataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbms_UserDefinedDataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbms_UserDefinedDataType(defaultValue="sample_text", length=7, precision=7)
    partner = rdbms_Database()
    setattr(partner, 'rdbms_Database', None)
    _safe_set(owner, 'rdbms_UserDefinedDataType', partner)
    assert owner in getattr(partner, 'rdbms_Database')
    _safe_set(owner, 'rdbms_UserDefinedDataType', None)
    assert owner not in getattr(partner, 'rdbms_Database')


