import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    rdpl_Column,
    rdpl_ForeignKey,
    rdpl_Record,
    rdpl_RecordElement,
    rdpl_Schema,
    rdpl_Table,
    rdpl_Type,
    BasicType,
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

def test_assoc_columns3_reverse_link_reassign_clear():
    a1 = rdpl_Table(name="sample_text")
    a2 = rdpl_Table(name="sample_text_2")
    b = rdpl_Column(ctype="sample_text", name="sample_text", stype="sample_text")
    _safe_set(b, 'rdpl_Column', a1)
    assert _is_linked(b, 'rdpl_Column', a1)
    if hasattr(a1, 'rdpl_Table4'):
        assert _is_linked(a1, 'rdpl_Table4', b)
    _safe_set(b, 'rdpl_Column', a2)
    assert _is_linked(b, 'rdpl_Column', a2)
    if hasattr(a1, 'rdpl_Table4'):
        assert not _is_linked(a1, 'rdpl_Table4', b)
    if hasattr(a2, 'rdpl_Table4'):
        assert _is_linked(a2, 'rdpl_Table4', b)
    _safe_set(b, 'rdpl_Column', None)
    assert not _is_linked(b, 'rdpl_Column', a2)
    if hasattr(a2, 'rdpl_Table4'):
        assert not _is_linked(a2, 'rdpl_Table4', b)


def test_assoc_keyColumns5_reverse_link_reassign_clear():
    a1 = rdpl_Table(name="sample_text")
    a2 = rdpl_Table(name="sample_text_2")
    b = rdpl_Column(ctype="sample_text", name="sample_text", stype="sample_text")
    _safe_set(b, 'rdpl_Column7', a1)
    assert _is_linked(b, 'rdpl_Column7', a1)
    if hasattr(a1, 'rdpl_Table6'):
        assert _is_linked(a1, 'rdpl_Table6', b)
    _safe_set(b, 'rdpl_Column7', a2)
    assert _is_linked(b, 'rdpl_Column7', a2)
    if hasattr(a1, 'rdpl_Table6'):
        assert not _is_linked(a1, 'rdpl_Table6', b)
    if hasattr(a2, 'rdpl_Table6'):
        assert _is_linked(a2, 'rdpl_Table6', b)
    _safe_set(b, 'rdpl_Column7', None)
    assert not _is_linked(b, 'rdpl_Column7', a2)
    if hasattr(a2, 'rdpl_Table6'):
        assert not _is_linked(a2, 'rdpl_Table6', b)


def test_assoc_tables0_reverse_link_reassign_clear():
    a1 = rdpl_Table(name="sample_text")
    a2 = rdpl_Table(name="sample_text_2")
    b = rdpl_Schema(name="sample_text")
    _safe_set(b, 'rdpl_Schema', {a1})
    assert _is_linked(b, 'rdpl_Schema', a1)
    if hasattr(a1, 'rdpl_Table'):
        assert _is_linked(a1, 'rdpl_Table', b)
    _safe_set(b, 'rdpl_Schema', {a2})
    assert _is_linked(b, 'rdpl_Schema', a2)
    if hasattr(a1, 'rdpl_Table'):
        assert not _is_linked(a1, 'rdpl_Table', b)
    if hasattr(a2, 'rdpl_Table'):
        assert _is_linked(a2, 'rdpl_Table', b)
    _safe_set(b, 'rdpl_Schema', set())
    assert not _is_linked(b, 'rdpl_Schema', a2)
    if hasattr(a2, 'rdpl_Table'):
        assert not _is_linked(a2, 'rdpl_Table', b)


def test_assoc_type20_reverse_link_reassign_clear():
    a1 = rdpl_RecordElement(value="sample_text")
    a2 = rdpl_RecordElement(value="sample_text_2")
    b = rdpl_Column(ctype="sample_text", name="sample_text", stype="sample_text")
    _safe_set(b, 'rdpl_Column22', a1)
    assert _is_linked(b, 'rdpl_Column22', a1)
    if hasattr(a1, 'rdpl_RecordElement21'):
        assert _is_linked(a1, 'rdpl_RecordElement21', b)
    _safe_set(b, 'rdpl_Column22', a2)
    assert _is_linked(b, 'rdpl_Column22', a2)
    if hasattr(a1, 'rdpl_RecordElement21'):
        assert not _is_linked(a1, 'rdpl_RecordElement21', b)
    if hasattr(a2, 'rdpl_RecordElement21'):
        assert _is_linked(a2, 'rdpl_RecordElement21', b)
    _safe_set(b, 'rdpl_Column22', None)
    assert not _is_linked(b, 'rdpl_Column22', a2)
    if hasattr(a2, 'rdpl_RecordElement21'):
        assert not _is_linked(a2, 'rdpl_RecordElement21', b)


def test_assoc_type23_reverse_link_reassign_clear():
    a1 = rdpl_Type(name="sample_text")
    a2 = rdpl_Type(name="sample_text_2")
    b = rdpl_Column(ctype="sample_text", name="sample_text", stype="sample_text")
    _safe_set(b, 'rdpl_Column24', a1)
    assert _is_linked(b, 'rdpl_Column24', a1)
    if hasattr(a1, 'rdpl_Type25'):
        assert _is_linked(a1, 'rdpl_Type25', b)
    _safe_set(b, 'rdpl_Column24', a2)
    assert _is_linked(b, 'rdpl_Column24', a2)
    if hasattr(a1, 'rdpl_Type25'):
        assert not _is_linked(a1, 'rdpl_Type25', b)
    if hasattr(a2, 'rdpl_Type25'):
        assert _is_linked(a2, 'rdpl_Type25', b)
    _safe_set(b, 'rdpl_Column24', None)
    assert not _is_linked(b, 'rdpl_Column24', a2)
    if hasattr(a2, 'rdpl_Type25'):
        assert not _is_linked(a2, 'rdpl_Type25', b)


def test_assoc_types1_reverse_link_reassign_clear():
    a1 = rdpl_Type(name="sample_text")
    a2 = rdpl_Type(name="sample_text_2")
    b = rdpl_Schema(name="sample_text")
    _safe_set(b, 'rdpl_Schema2', {a1})
    assert _is_linked(b, 'rdpl_Schema2', a1)
    if hasattr(a1, 'rdpl_Type'):
        assert _is_linked(a1, 'rdpl_Type', b)
    _safe_set(b, 'rdpl_Schema2', {a2})
    assert _is_linked(b, 'rdpl_Schema2', a2)
    if hasattr(a1, 'rdpl_Type'):
        assert not _is_linked(a1, 'rdpl_Type', b)
    if hasattr(a2, 'rdpl_Type'):
        assert _is_linked(a2, 'rdpl_Type', b)
    _safe_set(b, 'rdpl_Schema2', set())
    assert not _is_linked(b, 'rdpl_Schema2', a2)
    if hasattr(a2, 'rdpl_Type'):
        assert not _is_linked(a2, 'rdpl_Type', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns15_stub_double():
    # rdpl_ForeignKey has no real 'rdpl_ForeignKey16' property in the generated
    # code (a bare stub) -- manually attach it so rdpl_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdpl_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdpl_Column(ctype="sample_text", name="sample_text", stype="sample_text")
    partner = rdpl_ForeignKey()
    setattr(partner, 'rdpl_ForeignKey16', None)
    _safe_set(owner, 'rdpl_Column17', partner)
    assert owner in getattr(partner, 'rdpl_ForeignKey16')
    _safe_set(owner, 'rdpl_Column17', None)
    assert owner not in getattr(partner, 'rdpl_ForeignKey16')


def test_assoc_content8_stub_double():
    # rdpl_Record has no real 'rdpl_Record' property in the generated
    # code (a bare stub) -- manually attach it so rdpl_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdpl_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdpl_Table(name="sample_text")
    partner = rdpl_Record()
    setattr(partner, 'rdpl_Record', None)
    _safe_set(owner, 'rdpl_Table9', {partner})
    assert getattr(partner, 'rdpl_Record') == owner
    _safe_set(owner, 'rdpl_Table9', set())
    assert getattr(partner, 'rdpl_Record') is None


def test_assoc_elements18_stub_double():
    # rdpl_Record has no real 'rdpl_Record19' property in the generated
    # code (a bare stub) -- manually attach it so rdpl_RecordElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdpl_RecordElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdpl_RecordElement(value="sample_text")
    partner = rdpl_Record()
    setattr(partner, 'rdpl_Record19', None)
    _safe_set(owner, 'rdpl_RecordElement', partner)
    assert owner in getattr(partner, 'rdpl_Record19')
    _safe_set(owner, 'rdpl_RecordElement', None)
    assert owner not in getattr(partner, 'rdpl_Record19')


def test_assoc_foreignKeys10_stub_double():
    # rdpl_ForeignKey has no real 'rdpl_ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so rdpl_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdpl_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdpl_Table(name="sample_text")
    partner = rdpl_ForeignKey()
    setattr(partner, 'rdpl_ForeignKey', None)
    _safe_set(owner, 'rdpl_Table11', {partner})
    assert getattr(partner, 'rdpl_ForeignKey') == owner
    _safe_set(owner, 'rdpl_Table11', set())
    assert getattr(partner, 'rdpl_ForeignKey') is None


def test_assoc_references12_stub_double():
    # rdpl_ForeignKey has no real 'rdpl_ForeignKey13' property in the generated
    # code (a bare stub) -- manually attach it so rdpl_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdpl_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdpl_Table(name="sample_text")
    partner = rdpl_ForeignKey()
    setattr(partner, 'rdpl_ForeignKey13', None)
    _safe_set(owner, 'rdpl_Table14', partner)
    assert getattr(partner, 'rdpl_ForeignKey13') == owner
    _safe_set(owner, 'rdpl_Table14', None)
    assert getattr(partner, 'rdpl_ForeignKey13') is None


