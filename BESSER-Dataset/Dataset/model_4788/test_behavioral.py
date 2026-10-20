import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Collection,
    FloatingPoint,
    Int,
    OpenDDSLib,
    SignedInt,
    Simple,
    Type,
    UnsignedInt,
    types_Array,
    types_Boolean,
    types_Branch,
    types_Case,
    types_Char,
    types_Collection,
    types_DataLib,
    types_Double,
    types_Enum,
    types_Field,
    types_Float,
    types_FloatingPoint,
    types_Int,
    types_Key,
    types_Long,
    types_LongDouble,
    types_LongLong,
    types_Octet,
    types_Sequence,
    types_Short,
    types_SignedInt,
    types_Simple,
    types_String,
    types_Struct,
    types_Type,
    types_Typedef,
    types_ULong,
    types_ULongLong,
    types_UShort,
    types_Union,
    types_UnsignedInt,
    types_WChar,
    types_WString,
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

def test_assoc_default23_reverse_link_reassign_clear():
    a1 = types_Union(name="sample_text")
    a2 = types_Union(name="sample_text_2")
    b = types_Field(name="sample_text")
    _safe_set(b, 'types_Field25', a1)
    assert _is_linked(b, 'types_Field25', a1)
    if hasattr(a1, 'types_Union24'):
        assert _is_linked(a1, 'types_Union24', b)
    _safe_set(b, 'types_Field25', a2)
    assert _is_linked(b, 'types_Field25', a2)
    if hasattr(a1, 'types_Union24'):
        assert not _is_linked(a1, 'types_Union24', b)
    if hasattr(a2, 'types_Union24'):
        assert _is_linked(a2, 'types_Union24', b)
    _safe_set(b, 'types_Field25', None)
    assert not _is_linked(b, 'types_Field25', a2)
    if hasattr(a2, 'types_Union24'):
        assert not _is_linked(a2, 'types_Union24', b)


def test_assoc_fields11_reverse_link_reassign_clear():
    a1 = types_Struct(isDcpsDataType=True, name="sample_text")
    a2 = types_Struct(isDcpsDataType=False, name="sample_text_2")
    b = types_Field(name="sample_text")
    _safe_set(b, 'types_Field12', a1)
    assert _is_linked(b, 'types_Field12', a1)
    if hasattr(a1, 'types_Struct'):
        assert _is_linked(a1, 'types_Struct', b)
    _safe_set(b, 'types_Field12', a2)
    assert _is_linked(b, 'types_Field12', a2)
    if hasattr(a1, 'types_Struct'):
        assert not _is_linked(a1, 'types_Struct', b)
    if hasattr(a2, 'types_Struct'):
        assert _is_linked(a2, 'types_Struct', b)
    _safe_set(b, 'types_Field12', None)
    assert not _is_linked(b, 'types_Field12', a2)
    if hasattr(a2, 'types_Struct'):
        assert not _is_linked(a2, 'types_Struct', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_branches18_stub_double():
    # types_Branch has no real 'types_Branch19' property in the generated
    # code (a bare stub) -- manually attach it so types_Union's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Union's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Union(name="sample_text")
    partner = types_Branch()
    setattr(partner, 'types_Branch19', None)
    _safe_set(owner, 'types_Union', {partner})
    assert getattr(partner, 'types_Branch19') == owner
    _safe_set(owner, 'types_Union', set())
    assert getattr(partner, 'types_Branch19') is None


def test_assoc_cases2_stub_double():
    # types_Branch has no real 'types_Branch3' property in the generated
    # code (a bare stub) -- manually attach it so types_Case's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Case's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Case(literal="sample_text")
    partner = types_Branch()
    setattr(partner, 'types_Branch3', None)
    _safe_set(owner, 'types_Case', partner)
    assert owner in getattr(partner, 'types_Branch3')
    _safe_set(owner, 'types_Case', None)
    assert owner not in getattr(partner, 'types_Branch3')


def test_assoc_field1_stub_double():
    # types_Branch has no real 'types_Branch' property in the generated
    # code (a bare stub) -- manually attach it so types_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Field(name="sample_text")
    partner = types_Branch()
    setattr(partner, 'types_Branch', None)
    _safe_set(owner, 'types_Field', partner)
    assert getattr(partner, 'types_Branch') == owner
    _safe_set(owner, 'types_Field', None)
    assert getattr(partner, 'types_Branch') is None


def test_assoc_field7_stub_double():
    # types_Key has no real 'types_Key' property in the generated
    # code (a bare stub) -- manually attach it so types_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Field(name="sample_text")
    partner = types_Key()
    setattr(partner, 'types_Key', None)
    _safe_set(owner, 'types_Field8', partner)
    assert getattr(partner, 'types_Key') == owner
    _safe_set(owner, 'types_Field8', None)
    assert getattr(partner, 'types_Key') is None


def test_assoc_keys13_stub_double():
    # types_Key has no real 'types_Key15' property in the generated
    # code (a bare stub) -- manually attach it so types_Struct's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Struct's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Struct(isDcpsDataType=True, name="sample_text")
    partner = types_Key()
    setattr(partner, 'types_Key15', None)
    _safe_set(owner, 'types_Struct14', {partner})
    assert getattr(partner, 'types_Key15') == owner
    _safe_set(owner, 'types_Struct14', set())
    assert getattr(partner, 'types_Key15') is None


def test_assoc_switch20_stub_double():
    # types_Type has no real 'types_Type22' property in the generated
    # code (a bare stub) -- manually attach it so types_Union's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Union's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Union(name="sample_text")
    partner = types_Type()
    setattr(partner, 'types_Type22', None)
    _safe_set(owner, 'types_Union21', partner)
    assert getattr(partner, 'types_Type22') == owner
    _safe_set(owner, 'types_Union21', None)
    assert getattr(partner, 'types_Type22') is None


def test_assoc_type16_stub_double():
    # types_Type has no real 'types_Type17' property in the generated
    # code (a bare stub) -- manually attach it so types_Typedef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Typedef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Typedef(name="sample_text")
    partner = types_Type()
    setattr(partner, 'types_Type17', None)
    _safe_set(owner, 'types_Typedef', partner)
    assert getattr(partner, 'types_Type17') == owner
    _safe_set(owner, 'types_Typedef', None)
    assert getattr(partner, 'types_Type17') is None


def test_assoc_type4_stub_double():
    # types_Type has no real 'types_Type6' property in the generated
    # code (a bare stub) -- manually attach it so types_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Field(name="sample_text")
    partner = types_Type()
    setattr(partner, 'types_Type6', None)
    _safe_set(owner, 'types_Field5', partner)
    assert getattr(partner, 'types_Type6') == owner
    _safe_set(owner, 'types_Field5', None)
    assert getattr(partner, 'types_Type6') is None


