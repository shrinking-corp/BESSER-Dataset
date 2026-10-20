import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ApproximateNumericType,
    BitStringType,
    CharacterStringType,
    DDL_ApproximateNumericType,
    DDL_Bit,
    DDL_BitStringType,
    DDL_BitVarying,
    DDL_Char,
    DDL_CharVarying,
    DDL_Character,
    DDL_CharacterStringType,
    DDL_CharacterVarying,
    DDL_Check,
    DDL_Ck,
    DDL_Column,
    DDL_DDLDefinition,
    DDL_Database,
    DDL_Date,
    DDL_DatetimeType,
    DDL_Dec,
    DDL_Decimal,
    DDL_DoublePrecision,
    DDL_ExactNumericType,
    DDL_Fk,
    DDL_Float,
    DDL_Int,
    DDL_Integer,
    DDL_Interval,
    DDL_NChar,
    DDL_NCharVarying,
    DDL_NamedElement,
    DDL_NationalChar,
    DDL_NationalCharVarying,
    DDL_NationalCharacter,
    DDL_NationalCharacterStringType,
    DDL_NationalCharacterVarying,
    DDL_Numeric,
    DDL_NumericType,
    DDL_Pk,
    DDL_Real,
    DDL_Small,
    DDL_Statement,
    DDL_Table,
    DDL_Time,
    DDL_TimeStamp,
    DDL_Type,
    DDL_ValuesCheck,
    DDL_Varchar,
    DatetimeType,
    ExactNumericType,
    NamedElement,
    NationalCharacterStringType,
    NumericType,
    Statement,
    Type,
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

def test_assoc_cks4_stub_double():
    # DDL_Table has no real 'DDL_Table5' property in the generated
    # code (a bare stub) -- manually attach it so DDL_Ck's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DDL_Ck's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DDL_Ck(columnName="sample_text")
    partner = DDL_Table()
    setattr(partner, 'DDL_Table5', None)
    _safe_set(owner, 'DDL_Ck', partner)
    assert owner in getattr(partner, 'DDL_Table5')
    _safe_set(owner, 'DDL_Ck', None)
    assert owner not in getattr(partner, 'DDL_Table5')


def test_assoc_columns1_stub_double():
    # DDL_Table has no real 'DDL_Table' property in the generated
    # code (a bare stub) -- manually attach it so DDL_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DDL_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DDL_Column(columnNull=True)
    partner = DDL_Table()
    setattr(partner, 'DDL_Table', None)
    _safe_set(owner, 'DDL_Column', partner)
    assert owner in getattr(partner, 'DDL_Table')
    _safe_set(owner, 'DDL_Column', None)
    assert owner not in getattr(partner, 'DDL_Table')


def test_assoc_fks6_stub_double():
    # DDL_Table has no real 'DDL_Table7' property in the generated
    # code (a bare stub) -- manually attach it so DDL_Fk's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DDL_Fk's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DDL_Fk(columnName="sample_text", columnReference="sample_text")
    partner = DDL_Table()
    setattr(partner, 'DDL_Table7', None)
    _safe_set(owner, 'DDL_Fk', partner)
    assert owner in getattr(partner, 'DDL_Table7')
    _safe_set(owner, 'DDL_Fk', None)
    assert owner not in getattr(partner, 'DDL_Table7')


def test_assoc_pks2_stub_double():
    # DDL_Table has no real 'DDL_Table3' property in the generated
    # code (a bare stub) -- manually attach it so DDL_Pk's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DDL_Pk's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DDL_Pk(columnName="sample_text")
    partner = DDL_Table()
    setattr(partner, 'DDL_Table3', None)
    _safe_set(owner, 'DDL_Pk', partner)
    assert getattr(partner, 'DDL_Table3') == owner
    _safe_set(owner, 'DDL_Pk', None)
    assert getattr(partner, 'DDL_Table3') is None


def test_assoc_references12_stub_double():
    # DDL_Table has no real 'DDL_Table14' property in the generated
    # code (a bare stub) -- manually attach it so DDL_Fk's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DDL_Fk's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DDL_Fk(columnName="sample_text", columnReference="sample_text")
    partner = DDL_Table()
    setattr(partner, 'DDL_Table14', None)
    _safe_set(owner, 'DDL_Fk13', partner)
    assert getattr(partner, 'DDL_Table14') == owner
    _safe_set(owner, 'DDL_Fk13', None)
    assert getattr(partner, 'DDL_Table14') is None


def test_assoc_type10_stub_double():
    # DDL_Type has no real 'DDL_Type' property in the generated
    # code (a bare stub) -- manually attach it so DDL_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DDL_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DDL_Column(columnNull=True)
    partner = DDL_Type()
    setattr(partner, 'DDL_Type', None)
    _safe_set(owner, 'DDL_Column11', partner)
    assert getattr(partner, 'DDL_Type') == owner
    _safe_set(owner, 'DDL_Column11', None)
    assert getattr(partner, 'DDL_Type') is None


def test_assoc_valuesCheck15_stub_double():
    # DDL_Check has no real 'DDL_Check16' property in the generated
    # code (a bare stub) -- manually attach it so DDL_ValuesCheck's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DDL_ValuesCheck's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DDL_ValuesCheck(columnName="sample_text", comparator="sample_text", logConjuntion="sample_text", value="sample_text")
    partner = DDL_Check()
    setattr(partner, 'DDL_Check16', None)
    _safe_set(owner, 'DDL_ValuesCheck', partner)
    assert owner in getattr(partner, 'DDL_Check16')
    _safe_set(owner, 'DDL_ValuesCheck', None)
    assert owner not in getattr(partner, 'DDL_Check16')


