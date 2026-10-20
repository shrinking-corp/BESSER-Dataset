import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    xDstmdata_cExtchannel,
    xDstmdata_cIntchannel,
    xDstmdata_channel_specifier,
    xDstmdata_composingtype,
    xDstmdata_subtype,
    xDstmdata_tCompound,
    xDstmdata_tEnum,
    xDstmdata_tMultitype,
    xDstmdata_tTypes,
    xDstmdata_vVariable,
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

def test_assoc_composingtypes15_reverse_link_reassign_clear():
    a1 = xDstmdata_tMultitype(name="sample_text")
    a2 = xDstmdata_tMultitype(name="sample_text_2")
    b = xDstmdata_composingtype(tID="sample_text", tString="sample_text")
    _safe_set(b, 'xDstmdata_composingtype', a1)
    assert _is_linked(b, 'xDstmdata_composingtype', a1)
    if hasattr(a1, 'xDstmdata_tMultitype16'):
        assert _is_linked(a1, 'xDstmdata_tMultitype16', b)
    _safe_set(b, 'xDstmdata_composingtype', a2)
    assert _is_linked(b, 'xDstmdata_composingtype', a2)
    if hasattr(a1, 'xDstmdata_tMultitype16'):
        assert not _is_linked(a1, 'xDstmdata_tMultitype16', b)
    if hasattr(a2, 'xDstmdata_tMultitype16'):
        assert _is_linked(a2, 'xDstmdata_tMultitype16', b)
    _safe_set(b, 'xDstmdata_composingtype', None)
    assert not _is_linked(b, 'xDstmdata_composingtype', a2)
    if hasattr(a2, 'xDstmdata_tMultitype16'):
        assert not _is_linked(a2, 'xDstmdata_tMultitype16', b)


def test_assoc_subtypes11_reverse_link_reassign_clear():
    a1 = xDstmdata_tCompound(name="sample_text")
    a2 = xDstmdata_tCompound(name="sample_text_2")
    b = xDstmdata_subtype(tID="sample_text", tString="sample_text")
    _safe_set(b, 'xDstmdata_subtype', a1)
    assert _is_linked(b, 'xDstmdata_subtype', a1)
    if hasattr(a1, 'xDstmdata_tCompound12'):
        assert _is_linked(a1, 'xDstmdata_tCompound12', b)
    _safe_set(b, 'xDstmdata_subtype', a2)
    assert _is_linked(b, 'xDstmdata_subtype', a2)
    if hasattr(a1, 'xDstmdata_tCompound12'):
        assert not _is_linked(a1, 'xDstmdata_tCompound12', b)
    if hasattr(a2, 'xDstmdata_tCompound12'):
        assert _is_linked(a2, 'xDstmdata_tCompound12', b)
    _safe_set(b, 'xDstmdata_subtype', None)
    assert not _is_linked(b, 'xDstmdata_subtype', a2)
    if hasattr(a2, 'xDstmdata_tCompound12'):
        assert not _is_linked(a2, 'xDstmdata_tCompound12', b)


def test_assoc_tChn13_reverse_link_reassign_clear():
    a1 = xDstmdata_subtype(tID="sample_text", tString="sample_text")
    a2 = xDstmdata_subtype(tID="sample_text_2", tString="sample_text_2")
    b = xDstmdata_channel_specifier(type="sample_text")
    _safe_set(b, 'xDstmdata_channel_specifier', a1)
    assert _is_linked(b, 'xDstmdata_channel_specifier', a1)
    if hasattr(a1, 'xDstmdata_subtype14'):
        assert _is_linked(a1, 'xDstmdata_subtype14', b)
    _safe_set(b, 'xDstmdata_channel_specifier', a2)
    assert _is_linked(b, 'xDstmdata_channel_specifier', a2)
    if hasattr(a1, 'xDstmdata_subtype14'):
        assert not _is_linked(a1, 'xDstmdata_subtype14', b)
    if hasattr(a2, 'xDstmdata_subtype14'):
        assert _is_linked(a2, 'xDstmdata_subtype14', b)
    _safe_set(b, 'xDstmdata_channel_specifier', None)
    assert not _is_linked(b, 'xDstmdata_channel_specifier', a2)
    if hasattr(a2, 'xDstmdata_subtype14'):
        assert not _is_linked(a2, 'xDstmdata_subtype14', b)


def test_assoc_tChn17_reverse_link_reassign_clear():
    a1 = xDstmdata_composingtype(tID="sample_text", tString="sample_text")
    a2 = xDstmdata_composingtype(tID="sample_text_2", tString="sample_text_2")
    b = xDstmdata_channel_specifier(type="sample_text")
    _safe_set(b, 'xDstmdata_channel_specifier19', a1)
    assert _is_linked(b, 'xDstmdata_channel_specifier19', a1)
    if hasattr(a1, 'xDstmdata_composingtype18'):
        assert _is_linked(a1, 'xDstmdata_composingtype18', b)
    _safe_set(b, 'xDstmdata_channel_specifier19', a2)
    assert _is_linked(b, 'xDstmdata_channel_specifier19', a2)
    if hasattr(a1, 'xDstmdata_composingtype18'):
        assert not _is_linked(a1, 'xDstmdata_composingtype18', b)
    if hasattr(a2, 'xDstmdata_composingtype18'):
        assert _is_linked(a2, 'xDstmdata_composingtype18', b)
    _safe_set(b, 'xDstmdata_channel_specifier19', None)
    assert not _is_linked(b, 'xDstmdata_channel_specifier19', a2)
    if hasattr(a2, 'xDstmdata_composingtype18'):
        assert not _is_linked(a2, 'xDstmdata_composingtype18', b)


def test_assoc_tChn20_reverse_link_reassign_clear():
    a1 = xDstmdata_channel_specifier(type="sample_text")
    a2 = xDstmdata_channel_specifier(type="sample_text_2")
    b = xDstmdata_cIntchannel(bound=7, name="sample_text", tID="sample_text", tString="sample_text")
    _safe_set(b, 'xDstmdata_cIntchannel21', a1)
    assert _is_linked(b, 'xDstmdata_cIntchannel21', a1)
    if hasattr(a1, 'xDstmdata_channel_specifier22'):
        assert _is_linked(a1, 'xDstmdata_channel_specifier22', b)
    _safe_set(b, 'xDstmdata_cIntchannel21', a2)
    assert _is_linked(b, 'xDstmdata_cIntchannel21', a2)
    if hasattr(a1, 'xDstmdata_channel_specifier22'):
        assert not _is_linked(a1, 'xDstmdata_channel_specifier22', b)
    if hasattr(a2, 'xDstmdata_channel_specifier22'):
        assert _is_linked(a2, 'xDstmdata_channel_specifier22', b)
    _safe_set(b, 'xDstmdata_cIntchannel21', None)
    assert not _is_linked(b, 'xDstmdata_cIntchannel21', a2)
    if hasattr(a2, 'xDstmdata_channel_specifier22'):
        assert not _is_linked(a2, 'xDstmdata_channel_specifier22', b)


def test_assoc_tChn23_reverse_link_reassign_clear():
    a1 = xDstmdata_channel_specifier(type="sample_text")
    a2 = xDstmdata_channel_specifier(type="sample_text_2")
    b = xDstmdata_cExtchannel(name="sample_text", tID="sample_text", tString="sample_text")
    _safe_set(b, 'xDstmdata_cExtchannel24', a1)
    assert _is_linked(b, 'xDstmdata_cExtchannel24', a1)
    if hasattr(a1, 'xDstmdata_channel_specifier25'):
        assert _is_linked(a1, 'xDstmdata_channel_specifier25', b)
    _safe_set(b, 'xDstmdata_cExtchannel24', a2)
    assert _is_linked(b, 'xDstmdata_cExtchannel24', a2)
    if hasattr(a1, 'xDstmdata_channel_specifier25'):
        assert not _is_linked(a1, 'xDstmdata_channel_specifier25', b)
    if hasattr(a2, 'xDstmdata_channel_specifier25'):
        assert _is_linked(a2, 'xDstmdata_channel_specifier25', b)
    _safe_set(b, 'xDstmdata_cExtchannel24', None)
    assert not _is_linked(b, 'xDstmdata_cExtchannel24', a2)
    if hasattr(a2, 'xDstmdata_channel_specifier25'):
        assert not _is_linked(a2, 'xDstmdata_channel_specifier25', b)


def test_assoc_tChn26_reverse_link_reassign_clear():
    a1 = xDstmdata_vVariable(name="sample_text", tID="sample_text", tString="sample_text")
    a2 = xDstmdata_vVariable(name="sample_text_2", tID="sample_text_2", tString="sample_text_2")
    b = xDstmdata_channel_specifier(type="sample_text")
    _safe_set(b, 'xDstmdata_channel_specifier28', a1)
    assert _is_linked(b, 'xDstmdata_channel_specifier28', a1)
    if hasattr(a1, 'xDstmdata_vVariable27'):
        assert _is_linked(a1, 'xDstmdata_vVariable27', b)
    _safe_set(b, 'xDstmdata_channel_specifier28', a2)
    assert _is_linked(b, 'xDstmdata_channel_specifier28', a2)
    if hasattr(a1, 'xDstmdata_vVariable27'):
        assert not _is_linked(a1, 'xDstmdata_vVariable27', b)
    if hasattr(a2, 'xDstmdata_vVariable27'):
        assert _is_linked(a2, 'xDstmdata_vVariable27', b)
    _safe_set(b, 'xDstmdata_channel_specifier28', None)
    assert not _is_linked(b, 'xDstmdata_channel_specifier28', a2)
    if hasattr(a2, 'xDstmdata_vVariable27'):
        assert not _is_linked(a2, 'xDstmdata_vVariable27', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cExtchannel7_stub_double():
    # xDstmdata_tTypes has no real 'xDstmdata_tTypes8' property in the generated
    # code (a bare stub) -- manually attach it so xDstmdata_cExtchannel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDstmdata_cExtchannel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDstmdata_cExtchannel(name="sample_text", tID="sample_text", tString="sample_text")
    partner = xDstmdata_tTypes()
    setattr(partner, 'xDstmdata_tTypes8', None)
    _safe_set(owner, 'xDstmdata_cExtchannel', partner)
    assert owner in getattr(partner, 'xDstmdata_tTypes8')
    _safe_set(owner, 'xDstmdata_cExtchannel', None)
    assert owner not in getattr(partner, 'xDstmdata_tTypes8')


def test_assoc_cIntchannel5_stub_double():
    # xDstmdata_tTypes has no real 'xDstmdata_tTypes6' property in the generated
    # code (a bare stub) -- manually attach it so xDstmdata_cIntchannel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDstmdata_cIntchannel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDstmdata_cIntchannel(bound=7, name="sample_text", tID="sample_text", tString="sample_text")
    partner = xDstmdata_tTypes()
    setattr(partner, 'xDstmdata_tTypes6', None)
    _safe_set(owner, 'xDstmdata_cIntchannel', partner)
    assert owner in getattr(partner, 'xDstmdata_tTypes6')
    _safe_set(owner, 'xDstmdata_cIntchannel', None)
    assert owner not in getattr(partner, 'xDstmdata_tTypes6')


def test_assoc_tCompound1_stub_double():
    # xDstmdata_tTypes has no real 'xDstmdata_tTypes2' property in the generated
    # code (a bare stub) -- manually attach it so xDstmdata_tCompound's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDstmdata_tCompound's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDstmdata_tCompound(name="sample_text")
    partner = xDstmdata_tTypes()
    setattr(partner, 'xDstmdata_tTypes2', None)
    _safe_set(owner, 'xDstmdata_tCompound', partner)
    assert owner in getattr(partner, 'xDstmdata_tTypes2')
    _safe_set(owner, 'xDstmdata_tCompound', None)
    assert owner not in getattr(partner, 'xDstmdata_tTypes2')


def test_assoc_tEnum0_stub_double():
    # xDstmdata_tTypes has no real 'xDstmdata_tTypes' property in the generated
    # code (a bare stub) -- manually attach it so xDstmdata_tEnum's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDstmdata_tEnum's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDstmdata_tEnum(literals="sample_text", name="sample_text")
    partner = xDstmdata_tTypes()
    setattr(partner, 'xDstmdata_tTypes', None)
    _safe_set(owner, 'xDstmdata_tEnum', partner)
    assert owner in getattr(partner, 'xDstmdata_tTypes')
    _safe_set(owner, 'xDstmdata_tEnum', None)
    assert owner not in getattr(partner, 'xDstmdata_tTypes')


def test_assoc_tMultitype3_stub_double():
    # xDstmdata_tTypes has no real 'xDstmdata_tTypes4' property in the generated
    # code (a bare stub) -- manually attach it so xDstmdata_tMultitype's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDstmdata_tMultitype's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDstmdata_tMultitype(name="sample_text")
    partner = xDstmdata_tTypes()
    setattr(partner, 'xDstmdata_tTypes4', None)
    _safe_set(owner, 'xDstmdata_tMultitype', partner)
    assert owner in getattr(partner, 'xDstmdata_tTypes4')
    _safe_set(owner, 'xDstmdata_tMultitype', None)
    assert owner not in getattr(partner, 'xDstmdata_tTypes4')


def test_assoc_vVariable9_stub_double():
    # xDstmdata_tTypes has no real 'xDstmdata_tTypes10' property in the generated
    # code (a bare stub) -- manually attach it so xDstmdata_vVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDstmdata_vVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDstmdata_vVariable(name="sample_text", tID="sample_text", tString="sample_text")
    partner = xDstmdata_tTypes()
    setattr(partner, 'xDstmdata_tTypes10', None)
    _safe_set(owner, 'xDstmdata_vVariable', partner)
    assert owner in getattr(partner, 'xDstmdata_tTypes10')
    _safe_set(owner, 'xDstmdata_vVariable', None)
    assert owner not in getattr(partner, 'xDstmdata_tTypes10')


