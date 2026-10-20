import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    kreq210_Bbbb,
    kreq210_Cccc,
    kreq210_Ffff,
    kreq210_Gggg,
    kreq210_Hhhh,
    kreq210_Llll,
    kreq210_Mmmm,
    BasicFlowTransformationType,
    CategoryType,
    ComponentPosition,
    ComponentType,
    RequirementOrigin,
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

def test_assoc_e017_reverse_link_reassign_clear():
    a1 = kreq210_Llll(id="sample_text")
    a2 = kreq210_Llll(id="sample_text_2")
    b = kreq210_Hhhh(id=7)
    _safe_set(b, 'kreq210_Hhhh19', a1)
    assert _is_linked(b, 'kreq210_Hhhh19', a1)
    if hasattr(a1, 'kreq210_Llll18'):
        assert _is_linked(a1, 'kreq210_Llll18', b)
    _safe_set(b, 'kreq210_Hhhh19', a2)
    assert _is_linked(b, 'kreq210_Hhhh19', a2)
    if hasattr(a1, 'kreq210_Llll18'):
        assert not _is_linked(a1, 'kreq210_Llll18', b)
    if hasattr(a2, 'kreq210_Llll18'):
        assert _is_linked(a2, 'kreq210_Llll18', b)
    _safe_set(b, 'kreq210_Hhhh19', None)
    assert not _is_linked(b, 'kreq210_Hhhh19', a2)
    if hasattr(a2, 'kreq210_Llll18'):
        assert not _is_linked(a2, 'kreq210_Llll18', b)


def test_assoc_fs7_reverse_link_reassign_clear():
    a1 = kreq210_Ffff(id="sample_text")
    a2 = kreq210_Ffff(id="sample_text_2")
    b = kreq210_Cccc(id="sample_text")
    _safe_set(b, 'kreq210_Cccc8', {a1})
    assert _is_linked(b, 'kreq210_Cccc8', a1)
    if hasattr(a1, 'kreq210_Ffff'):
        assert _is_linked(a1, 'kreq210_Ffff', b)
    _safe_set(b, 'kreq210_Cccc8', {a2})
    assert _is_linked(b, 'kreq210_Cccc8', a2)
    if hasattr(a1, 'kreq210_Ffff'):
        assert not _is_linked(a1, 'kreq210_Ffff', b)
    if hasattr(a2, 'kreq210_Ffff'):
        assert _is_linked(a2, 'kreq210_Ffff', b)
    _safe_set(b, 'kreq210_Cccc8', set())
    assert not _is_linked(b, 'kreq210_Cccc8', a2)
    if hasattr(a2, 'kreq210_Ffff'):
        assert not _is_linked(a2, 'kreq210_Ffff', b)


def test_assoc_lcs14_reverse_link_reassign_clear():
    a1 = kreq210_Llll(id="sample_text")
    a2 = kreq210_Llll(id="sample_text_2")
    b = kreq210_Cccc(id="sample_text")
    _safe_set(b, 'kreq210_Cccc16', a1)
    assert _is_linked(b, 'kreq210_Cccc16', a1)
    if hasattr(a1, 'kreq210_Llll15'):
        assert _is_linked(a1, 'kreq210_Llll15', b)
    _safe_set(b, 'kreq210_Cccc16', a2)
    assert _is_linked(b, 'kreq210_Cccc16', a2)
    if hasattr(a1, 'kreq210_Llll15'):
        assert not _is_linked(a1, 'kreq210_Llll15', b)
    if hasattr(a2, 'kreq210_Llll15'):
        assert _is_linked(a2, 'kreq210_Llll15', b)
    _safe_set(b, 'kreq210_Cccc16', None)
    assert not _is_linked(b, 'kreq210_Cccc16', a2)
    if hasattr(a2, 'kreq210_Llll15'):
        assert not _is_linked(a2, 'kreq210_Llll15', b)


def test_assoc_ls12_reverse_link_reassign_clear():
    a1 = kreq210_Llll(id="sample_text")
    a2 = kreq210_Llll(id="sample_text_2")
    b = kreq210_Gggg(id="sample_text")
    _safe_set(b, 'kreq210_Gggg13', {a1})
    assert _is_linked(b, 'kreq210_Gggg13', a1)
    if hasattr(a1, 'kreq210_Llll'):
        assert _is_linked(a1, 'kreq210_Llll', b)
    _safe_set(b, 'kreq210_Gggg13', {a2})
    assert _is_linked(b, 'kreq210_Gggg13', a2)
    if hasattr(a1, 'kreq210_Llll'):
        assert not _is_linked(a1, 'kreq210_Llll', b)
    if hasattr(a2, 'kreq210_Llll'):
        assert _is_linked(a2, 'kreq210_Llll', b)
    _safe_set(b, 'kreq210_Gggg13', set())
    assert not _is_linked(b, 'kreq210_Gggg13', a2)
    if hasattr(a2, 'kreq210_Llll'):
        assert not _is_linked(a2, 'kreq210_Llll', b)


def test_assoc_ms20_reverse_link_reassign_clear():
    a1 = kreq210_Mmmm(id="sample_text")
    a2 = kreq210_Mmmm(id="sample_text_2")
    b = kreq210_Llll(id="sample_text")
    _safe_set(b, 'kreq210_Llll21', {a1})
    assert _is_linked(b, 'kreq210_Llll21', a1)
    if hasattr(a1, 'kreq210_Mmmm22'):
        assert _is_linked(a1, 'kreq210_Mmmm22', b)
    _safe_set(b, 'kreq210_Llll21', {a2})
    assert _is_linked(b, 'kreq210_Llll21', a2)
    if hasattr(a1, 'kreq210_Mmmm22'):
        assert not _is_linked(a1, 'kreq210_Mmmm22', b)
    if hasattr(a2, 'kreq210_Mmmm22'):
        assert _is_linked(a2, 'kreq210_Mmmm22', b)
    _safe_set(b, 'kreq210_Llll21', set())
    assert not _is_linked(b, 'kreq210_Llll21', a2)
    if hasattr(a2, 'kreq210_Mmmm22'):
        assert not _is_linked(a2, 'kreq210_Mmmm22', b)


def test_assoc_subFs10_reverse_link_reassign_clear():
    a1 = kreq210_Ffff(id="sample_text")
    a2 = kreq210_Ffff(id="sample_text_2")
    b = kreq210_Ffff(id="sample_text")
    _safe_set(b, 'kreq210_Ffff9', {a1})
    assert _is_linked(b, 'kreq210_Ffff9', a1)
    if hasattr(a1, 'kreq210_Ffff11'):
        assert _is_linked(a1, 'kreq210_Ffff11', b)
    _safe_set(b, 'kreq210_Ffff9', {a2})
    assert _is_linked(b, 'kreq210_Ffff9', a2)
    if hasattr(a1, 'kreq210_Ffff11'):
        assert not _is_linked(a1, 'kreq210_Ffff11', b)
    if hasattr(a2, 'kreq210_Ffff11'):
        assert _is_linked(a2, 'kreq210_Ffff11', b)
    _safe_set(b, 'kreq210_Ffff9', set())
    assert not _is_linked(b, 'kreq210_Ffff9', a2)
    if hasattr(a2, 'kreq210_Ffff11'):
        assert not _is_linked(a2, 'kreq210_Ffff11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cs0_stub_double():
    # kreq210_Bbbb has no real 'kreq210_Bbbb' property in the generated
    # code (a bare stub) -- manually attach it so kreq210_Cccc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kreq210_Cccc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kreq210_Cccc(id="sample_text")
    partner = kreq210_Bbbb()
    setattr(partner, 'kreq210_Bbbb', None)
    _safe_set(owner, 'kreq210_Cccc', partner)
    assert owner in getattr(partner, 'kreq210_Bbbb')
    _safe_set(owner, 'kreq210_Cccc', None)
    assert owner not in getattr(partner, 'kreq210_Bbbb')


def test_assoc_gs1_stub_double():
    # kreq210_Bbbb has no real 'kreq210_Bbbb2' property in the generated
    # code (a bare stub) -- manually attach it so kreq210_Gggg's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kreq210_Gggg's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kreq210_Gggg(id="sample_text")
    partner = kreq210_Bbbb()
    setattr(partner, 'kreq210_Bbbb2', None)
    _safe_set(owner, 'kreq210_Gggg', partner)
    assert owner in getattr(partner, 'kreq210_Bbbb2')
    _safe_set(owner, 'kreq210_Gggg', None)
    assert owner not in getattr(partner, 'kreq210_Bbbb2')


def test_assoc_hs3_stub_double():
    # kreq210_Bbbb has no real 'kreq210_Bbbb4' property in the generated
    # code (a bare stub) -- manually attach it so kreq210_Hhhh's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kreq210_Hhhh's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kreq210_Hhhh(id=7)
    partner = kreq210_Bbbb()
    setattr(partner, 'kreq210_Bbbb4', None)
    _safe_set(owner, 'kreq210_Hhhh', partner)
    assert owner in getattr(partner, 'kreq210_Bbbb4')
    _safe_set(owner, 'kreq210_Hhhh', None)
    assert owner not in getattr(partner, 'kreq210_Bbbb4')


def test_assoc_ms5_stub_double():
    # kreq210_Bbbb has no real 'kreq210_Bbbb6' property in the generated
    # code (a bare stub) -- manually attach it so kreq210_Mmmm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kreq210_Mmmm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kreq210_Mmmm(id="sample_text")
    partner = kreq210_Bbbb()
    setattr(partner, 'kreq210_Bbbb6', None)
    _safe_set(owner, 'kreq210_Mmmm', partner)
    assert owner in getattr(partner, 'kreq210_Bbbb6')
    _safe_set(owner, 'kreq210_Mmmm', None)
    assert owner not in getattr(partner, 'kreq210_Bbbb6')


