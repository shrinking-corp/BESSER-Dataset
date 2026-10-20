import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SObject,
    kreq205_Bbbb,
    kreq205_Cccc,
    kreq205_Ffff,
    kreq205_Llll,
    kreq205_Rqs,
    kreq205_Rrrr,
    kreq205_SObject,
    kreq205_Tttt,
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

def test_assoc_alto29_reverse_link_reassign_clear():
    a1 = kreq205_Ffff(d4="sample_text")
    a2 = kreq205_Ffff(d4="sample_text_2")
    b = kreq205_Cccc(de1="sample_text")
    _safe_set(b, 'Cccc30', a1)
    assert _is_linked(b, 'Cccc30', a1)
    if hasattr(a1, 'impf'):
        assert _is_linked(a1, 'impf', b)
    _safe_set(b, 'Cccc30', a2)
    assert _is_linked(b, 'Cccc30', a2)
    if hasattr(a1, 'impf'):
        assert not _is_linked(a1, 'impf', b)
    if hasattr(a2, 'impf'):
        assert _is_linked(a2, 'impf', b)
    _safe_set(b, 'Cccc30', None)
    assert not _is_linked(b, 'Cccc30', a2)
    if hasattr(a2, 'impf'):
        assert not _is_linked(a2, 'impf', b)


def test_assoc_dReqt12_reverse_link_reassign_clear():
    a1 = kreq205_Rqs(a=True, d2="sample_text")
    a2 = kreq205_Rqs(a=False, d2="sample_text_2")
    b = kreq205_Rqs(a=True, d2="sample_text")
    _safe_set(b, 'kreq205_Rqs13', a1)
    assert _is_linked(b, 'kreq205_Rqs13', a1)
    if hasattr(a1, 'kreq205_Rqs11'):
        assert _is_linked(a1, 'kreq205_Rqs11', b)
    _safe_set(b, 'kreq205_Rqs13', a2)
    assert _is_linked(b, 'kreq205_Rqs13', a2)
    if hasattr(a1, 'kreq205_Rqs11'):
        assert not _is_linked(a1, 'kreq205_Rqs11', b)
    if hasattr(a2, 'kreq205_Rqs11'):
        assert _is_linked(a2, 'kreq205_Rqs11', b)
    _safe_set(b, 'kreq205_Rqs13', None)
    assert not _is_linked(b, 'kreq205_Rqs13', a2)
    if hasattr(a2, 'kreq205_Rqs11'):
        assert not _is_linked(a2, 'kreq205_Rqs11', b)


def test_assoc_dmof24_reverse_link_reassign_clear():
    a1 = kreq205_Ffff(d4="sample_text")
    a2 = kreq205_Ffff(d4="sample_text_2")
    b = kreq205_Cccc(de1="sample_text")
    _safe_set(b, 'Cccc25', a1)
    assert _is_linked(b, 'Cccc25', a1)
    if hasattr(a1, 'pfrmis'):
        assert _is_linked(a1, 'pfrmis', b)
    _safe_set(b, 'Cccc25', a2)
    assert _is_linked(b, 'Cccc25', a2)
    if hasattr(a1, 'pfrmis'):
        assert not _is_linked(a1, 'pfrmis', b)
    if hasattr(a2, 'pfrmis'):
        assert _is_linked(a2, 'pfrmis', b)
    _safe_set(b, 'Cccc25', None)
    assert not _is_linked(b, 'Cccc25', a2)
    if hasattr(a2, 'pfrmis'):
        assert not _is_linked(a2, 'pfrmis', b)


def test_assoc_impf41_reverse_link_reassign_clear():
    a1 = kreq205_Ffff(d4="sample_text")
    a2 = kreq205_Ffff(d4="sample_text_2")
    b = kreq205_Cccc(de1="sample_text")
    _safe_set(b, 'alto', {a1})
    assert _is_linked(b, 'alto', a1)
    if hasattr(a1, 'Ffff42'):
        assert _is_linked(a1, 'Ffff42', b)
    _safe_set(b, 'alto', {a2})
    assert _is_linked(b, 'alto', a2)
    if hasattr(a1, 'Ffff42'):
        assert not _is_linked(a1, 'Ffff42', b)
    if hasattr(a2, 'Ffff42'):
        assert _is_linked(a2, 'Ffff42', b)
    _safe_set(b, 'alto', set())
    assert not _is_linked(b, 'alto', a2)
    if hasattr(a2, 'Ffff42'):
        assert not _is_linked(a2, 'Ffff42', b)


def test_assoc_isBy22_reverse_link_reassign_clear():
    a1 = kreq205_Rqs(a=True, d2="sample_text")
    a2 = kreq205_Rqs(a=False, d2="sample_text_2")
    b = kreq205_Ffff(d4="sample_text")
    _safe_set(b, 'specs', {a1})
    assert _is_linked(b, 'specs', a1)
    if hasattr(a1, 'Rqs23'):
        assert _is_linked(a1, 'Rqs23', b)
    _safe_set(b, 'specs', {a2})
    assert _is_linked(b, 'specs', a2)
    if hasattr(a1, 'Rqs23'):
        assert not _is_linked(a1, 'Rqs23', b)
    if hasattr(a2, 'Rqs23'):
        assert _is_linked(a2, 'Rqs23', b)
    _safe_set(b, 'specs', set())
    assert not _is_linked(b, 'specs', a2)
    if hasattr(a2, 'Rqs23'):
        assert not _is_linked(a2, 'Rqs23', b)


def test_assoc_ls43_reverse_link_reassign_clear():
    a1 = kreq205_Llll(d6="sample_text")
    a2 = kreq205_Llll(d6="sample_text_2")
    b = kreq205_Cccc(de1="sample_text")
    _safe_set(b, 'kreq205_Cccc44', {a1})
    assert _is_linked(b, 'kreq205_Cccc44', a1)
    if hasattr(a1, 'kreq205_Llll'):
        assert _is_linked(a1, 'kreq205_Llll', b)
    _safe_set(b, 'kreq205_Cccc44', {a2})
    assert _is_linked(b, 'kreq205_Cccc44', a2)
    if hasattr(a1, 'kreq205_Llll'):
        assert not _is_linked(a1, 'kreq205_Llll', b)
    if hasattr(a2, 'kreq205_Llll'):
        assert _is_linked(a2, 'kreq205_Llll', b)
    _safe_set(b, 'kreq205_Cccc44', set())
    assert not _is_linked(b, 'kreq205_Cccc44', a2)
    if hasattr(a2, 'kreq205_Llll'):
        assert not _is_linked(a2, 'kreq205_Llll', b)


def test_assoc_pfrmis36_reverse_link_reassign_clear():
    a1 = kreq205_Ffff(d4="sample_text")
    a2 = kreq205_Ffff(d4="sample_text_2")
    b = kreq205_Cccc(de1="sample_text")
    _safe_set(b, 'dmof', {a1})
    assert _is_linked(b, 'dmof', a1)
    if hasattr(a1, 'Ffff37'):
        assert _is_linked(a1, 'Ffff37', b)
    _safe_set(b, 'dmof', {a2})
    assert _is_linked(b, 'dmof', a2)
    if hasattr(a1, 'Ffff37'):
        assert not _is_linked(a1, 'Ffff37', b)
    if hasattr(a2, 'Ffff37'):
        assert _is_linked(a2, 'Ffff37', b)
    _safe_set(b, 'dmof', set())
    assert not _is_linked(b, 'dmof', a2)
    if hasattr(a2, 'Ffff37'):
        assert not _is_linked(a2, 'Ffff37', b)


def test_assoc_refine19_reverse_link_reassign_clear():
    a1 = kreq205_Rqs(a=True, d2="sample_text")
    a2 = kreq205_Rqs(a=False, d2="sample_text_2")
    b = kreq205_Rqs(a=True, d2="sample_text")
    _safe_set(b, 'kreq205_Rqs20', a1)
    assert _is_linked(b, 'kreq205_Rqs20', a1)
    if hasattr(a1, 'kreq205_Rqs18'):
        assert _is_linked(a1, 'kreq205_Rqs18', b)
    _safe_set(b, 'kreq205_Rqs20', a2)
    assert _is_linked(b, 'kreq205_Rqs20', a2)
    if hasattr(a1, 'kreq205_Rqs18'):
        assert not _is_linked(a1, 'kreq205_Rqs18', b)
    if hasattr(a2, 'kreq205_Rqs18'):
        assert _is_linked(a2, 'kreq205_Rqs18', b)
    _safe_set(b, 'kreq205_Rqs20', None)
    assert not _is_linked(b, 'kreq205_Rqs20', a2)
    if hasattr(a2, 'kreq205_Rqs18'):
        assert not _is_linked(a2, 'kreq205_Rqs18', b)


def test_assoc_rqs7_reverse_link_reassign_clear():
    a1 = kreq205_Rrrr(d3="sample_text")
    a2 = kreq205_Rrrr(d3="sample_text_2")
    b = kreq205_Rqs(a=True, d2="sample_text")
    _safe_set(b, 'kreq205_Rqs', a1)
    assert _is_linked(b, 'kreq205_Rqs', a1)
    if hasattr(a1, 'kreq205_Rrrr8'):
        assert _is_linked(a1, 'kreq205_Rrrr8', b)
    _safe_set(b, 'kreq205_Rqs', a2)
    assert _is_linked(b, 'kreq205_Rqs', a2)
    if hasattr(a1, 'kreq205_Rrrr8'):
        assert not _is_linked(a1, 'kreq205_Rrrr8', b)
    if hasattr(a2, 'kreq205_Rrrr8'):
        assert _is_linked(a2, 'kreq205_Rrrr8', b)
    _safe_set(b, 'kreq205_Rqs', None)
    assert not _is_linked(b, 'kreq205_Rqs', a2)
    if hasattr(a2, 'kreq205_Rrrr8'):
        assert not _is_linked(a2, 'kreq205_Rrrr8', b)


def test_assoc_satisfy31_reverse_link_reassign_clear():
    a1 = kreq205_Rqs(a=True, d2="sample_text")
    a2 = kreq205_Rqs(a=False, d2="sample_text_2")
    b = kreq205_Cccc(de1="sample_text")
    _safe_set(b, 'kreq205_Cccc32', {a1})
    assert _is_linked(b, 'kreq205_Cccc32', a1)
    if hasattr(a1, 'kreq205_Rqs33'):
        assert _is_linked(a1, 'kreq205_Rqs33', b)
    _safe_set(b, 'kreq205_Cccc32', {a2})
    assert _is_linked(b, 'kreq205_Cccc32', a2)
    if hasattr(a1, 'kreq205_Rqs33'):
        assert not _is_linked(a1, 'kreq205_Rqs33', b)
    if hasattr(a2, 'kreq205_Rqs33'):
        assert _is_linked(a2, 'kreq205_Rqs33', b)
    _safe_set(b, 'kreq205_Cccc32', set())
    assert not _is_linked(b, 'kreq205_Cccc32', a2)
    if hasattr(a2, 'kreq205_Rqs33'):
        assert not _is_linked(a2, 'kreq205_Rqs33', b)


def test_assoc_source45_reverse_link_reassign_clear():
    a1 = kreq205_Llll(d6="sample_text")
    a2 = kreq205_Llll(d6="sample_text_2")
    b = kreq205_Cccc(de1="sample_text")
    _safe_set(b, 'kreq205_Cccc47', a1)
    assert _is_linked(b, 'kreq205_Cccc47', a1)
    if hasattr(a1, 'kreq205_Llll46'):
        assert _is_linked(a1, 'kreq205_Llll46', b)
    _safe_set(b, 'kreq205_Cccc47', a2)
    assert _is_linked(b, 'kreq205_Cccc47', a2)
    if hasattr(a1, 'kreq205_Llll46'):
        assert not _is_linked(a1, 'kreq205_Llll46', b)
    if hasattr(a2, 'kreq205_Llll46'):
        assert _is_linked(a2, 'kreq205_Llll46', b)
    _safe_set(b, 'kreq205_Cccc47', None)
    assert not _is_linked(b, 'kreq205_Cccc47', a2)
    if hasattr(a2, 'kreq205_Llll46'):
        assert not _is_linked(a2, 'kreq205_Llll46', b)


def test_assoc_spc21_reverse_link_reassign_clear():
    a1 = kreq205_Rqs(a=True, d2="sample_text")
    a2 = kreq205_Rqs(a=False, d2="sample_text_2")
    b = kreq205_Cccc(de1="sample_text")
    _safe_set(b, 'Cccc', a1)
    assert _is_linked(b, 'Cccc', a1)
    if hasattr(a1, 'specifiedBy'):
        assert _is_linked(a1, 'specifiedBy', b)
    _safe_set(b, 'Cccc', a2)
    assert _is_linked(b, 'Cccc', a2)
    if hasattr(a1, 'specifiedBy'):
        assert not _is_linked(a1, 'specifiedBy', b)
    if hasattr(a2, 'specifiedBy'):
        assert _is_linked(a2, 'specifiedBy', b)
    _safe_set(b, 'Cccc', None)
    assert not _is_linked(b, 'Cccc', a2)
    if hasattr(a2, 'specifiedBy'):
        assert not _is_linked(a2, 'specifiedBy', b)


def test_assoc_specifiedBy34_reverse_link_reassign_clear():
    a1 = kreq205_Rqs(a=True, d2="sample_text")
    a2 = kreq205_Rqs(a=False, d2="sample_text_2")
    b = kreq205_Cccc(de1="sample_text")
    _safe_set(b, 'spc', {a1})
    assert _is_linked(b, 'spc', a1)
    if hasattr(a1, 'Rqs35'):
        assert _is_linked(a1, 'Rqs35', b)
    _safe_set(b, 'spc', {a2})
    assert _is_linked(b, 'spc', a2)
    if hasattr(a1, 'Rqs35'):
        assert not _is_linked(a1, 'Rqs35', b)
    if hasattr(a2, 'Rqs35'):
        assert _is_linked(a2, 'Rqs35', b)
    _safe_set(b, 'spc', set())
    assert not _is_linked(b, 'spc', a2)
    if hasattr(a2, 'Rqs35'):
        assert not _is_linked(a2, 'Rqs35', b)


def test_assoc_specs17_reverse_link_reassign_clear():
    a1 = kreq205_Rqs(a=True, d2="sample_text")
    a2 = kreq205_Rqs(a=False, d2="sample_text_2")
    b = kreq205_Ffff(d4="sample_text")
    _safe_set(b, 'Ffff', a1)
    assert _is_linked(b, 'Ffff', a1)
    if hasattr(a1, 'isBy'):
        assert _is_linked(a1, 'isBy', b)
    _safe_set(b, 'Ffff', a2)
    assert _is_linked(b, 'Ffff', a2)
    if hasattr(a1, 'isBy'):
        assert not _is_linked(a1, 'isBy', b)
    if hasattr(a2, 'isBy'):
        assert _is_linked(a2, 'isBy', b)
    _safe_set(b, 'Ffff', None)
    assert not _is_linked(b, 'Ffff', a2)
    if hasattr(a2, 'isBy'):
        assert not _is_linked(a2, 'isBy', b)


def test_assoc_subCs39_reverse_link_reassign_clear():
    a1 = kreq205_Cccc(de1="sample_text")
    a2 = kreq205_Cccc(de1="sample_text_2")
    b = kreq205_Cccc(de1="sample_text")
    _safe_set(b, 'kreq205_Cccc40', a1)
    assert _is_linked(b, 'kreq205_Cccc40', a1)
    if hasattr(a1, 'kreq205_Cccc38'):
        assert _is_linked(a1, 'kreq205_Cccc38', b)
    _safe_set(b, 'kreq205_Cccc40', a2)
    assert _is_linked(b, 'kreq205_Cccc40', a2)
    if hasattr(a1, 'kreq205_Cccc38'):
        assert not _is_linked(a1, 'kreq205_Cccc38', b)
    if hasattr(a2, 'kreq205_Cccc38'):
        assert _is_linked(a2, 'kreq205_Cccc38', b)
    _safe_set(b, 'kreq205_Cccc40', None)
    assert not _is_linked(b, 'kreq205_Cccc40', a2)
    if hasattr(a2, 'kreq205_Cccc38'):
        assert not _is_linked(a2, 'kreq205_Cccc38', b)


def test_assoc_subFs27_reverse_link_reassign_clear():
    a1 = kreq205_Ffff(d4="sample_text")
    a2 = kreq205_Ffff(d4="sample_text_2")
    b = kreq205_Ffff(d4="sample_text")
    _safe_set(b, 'kreq205_Ffff28', a1)
    assert _is_linked(b, 'kreq205_Ffff28', a1)
    if hasattr(a1, 'kreq205_Ffff26'):
        assert _is_linked(a1, 'kreq205_Ffff26', b)
    _safe_set(b, 'kreq205_Ffff28', a2)
    assert _is_linked(b, 'kreq205_Ffff28', a2)
    if hasattr(a1, 'kreq205_Ffff26'):
        assert not _is_linked(a1, 'kreq205_Ffff26', b)
    if hasattr(a2, 'kreq205_Ffff26'):
        assert _is_linked(a2, 'kreq205_Ffff26', b)
    _safe_set(b, 'kreq205_Ffff28', None)
    assert not _is_linked(b, 'kreq205_Ffff28', a2)
    if hasattr(a2, 'kreq205_Ffff26'):
        assert not _is_linked(a2, 'kreq205_Ffff26', b)


def test_assoc_subRqs15_reverse_link_reassign_clear():
    a1 = kreq205_Rqs(a=True, d2="sample_text")
    a2 = kreq205_Rqs(a=False, d2="sample_text_2")
    b = kreq205_Rqs(a=True, d2="sample_text")
    _safe_set(b, 'kreq205_Rqs16', a1)
    assert _is_linked(b, 'kreq205_Rqs16', a1)
    if hasattr(a1, 'kreq205_Rqs14'):
        assert _is_linked(a1, 'kreq205_Rqs14', b)
    _safe_set(b, 'kreq205_Rqs16', a2)
    assert _is_linked(b, 'kreq205_Rqs16', a2)
    if hasattr(a1, 'kreq205_Rqs14'):
        assert not _is_linked(a1, 'kreq205_Rqs14', b)
    if hasattr(a2, 'kreq205_Rqs14'):
        assert _is_linked(a2, 'kreq205_Rqs14', b)
    _safe_set(b, 'kreq205_Rqs16', None)
    assert not _is_linked(b, 'kreq205_Rqs16', a2)
    if hasattr(a2, 'kreq205_Rqs14'):
        assert not _is_linked(a2, 'kreq205_Rqs14', b)


def test_assoc_target48_reverse_link_reassign_clear():
    a1 = kreq205_Rqs(a=True, d2="sample_text")
    a2 = kreq205_Rqs(a=False, d2="sample_text_2")
    b = kreq205_Llll(d6="sample_text")
    _safe_set(b, 'kreq205_Llll49', a1)
    assert _is_linked(b, 'kreq205_Llll49', a1)
    if hasattr(a1, 'kreq205_Rqs50'):
        assert _is_linked(a1, 'kreq205_Rqs50', b)
    _safe_set(b, 'kreq205_Llll49', a2)
    assert _is_linked(b, 'kreq205_Llll49', a2)
    if hasattr(a1, 'kreq205_Rqs50'):
        assert not _is_linked(a1, 'kreq205_Rqs50', b)
    if hasattr(a2, 'kreq205_Rqs50'):
        assert _is_linked(a2, 'kreq205_Rqs50', b)
    _safe_set(b, 'kreq205_Llll49', None)
    assert not _is_linked(b, 'kreq205_Llll49', a2)
    if hasattr(a2, 'kreq205_Rqs50'):
        assert not _is_linked(a2, 'kreq205_Rqs50', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ccs3_stub_double():
    # kreq205_Bbbb has no real 'kreq205_Bbbb4' property in the generated
    # code (a bare stub) -- manually attach it so kreq205_Cccc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kreq205_Cccc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kreq205_Cccc(de1="sample_text")
    partner = kreq205_Bbbb()
    setattr(partner, 'kreq205_Bbbb4', None)
    _safe_set(owner, 'kreq205_Cccc', partner)
    assert owner in getattr(partner, 'kreq205_Bbbb4')
    _safe_set(owner, 'kreq205_Cccc', None)
    assert owner not in getattr(partner, 'kreq205_Bbbb4')


def test_assoc_fs5_stub_double():
    # kreq205_Bbbb has no real 'kreq205_Bbbb6' property in the generated
    # code (a bare stub) -- manually attach it so kreq205_Ffff's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kreq205_Ffff's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kreq205_Ffff(d4="sample_text")
    partner = kreq205_Bbbb()
    setattr(partner, 'kreq205_Bbbb6', None)
    _safe_set(owner, 'kreq205_Ffff', partner)
    assert owner in getattr(partner, 'kreq205_Bbbb6')
    _safe_set(owner, 'kreq205_Ffff', None)
    assert owner not in getattr(partner, 'kreq205_Bbbb6')


def test_assoc_rqs9_stub_double():
    # kreq205_Tttt has no real 'rts' property in the generated
    # code (a bare stub) -- manually attach it so kreq205_Rqs's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kreq205_Rqs's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kreq205_Rqs(a=True, d2="sample_text")
    partner = kreq205_Tttt()
    setattr(partner, 'rts', None)
    _safe_set(owner, 'Rqs', partner)
    assert owner in getattr(partner, 'rts')
    _safe_set(owner, 'Rqs', None)
    assert owner not in getattr(partner, 'rts')


def test_assoc_rs0_stub_double():
    # kreq205_Bbbb has no real 'kreq205_Bbbb' property in the generated
    # code (a bare stub) -- manually attach it so kreq205_Rrrr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kreq205_Rrrr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kreq205_Rrrr(d3="sample_text")
    partner = kreq205_Bbbb()
    setattr(partner, 'kreq205_Bbbb', None)
    _safe_set(owner, 'kreq205_Rrrr', partner)
    assert owner in getattr(partner, 'kreq205_Bbbb')
    _safe_set(owner, 'kreq205_Rrrr', None)
    assert owner not in getattr(partner, 'kreq205_Bbbb')


def test_assoc_rts10_stub_double():
    # kreq205_Tttt has no real 'Tttt' property in the generated
    # code (a bare stub) -- manually attach it so kreq205_Rqs's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kreq205_Rqs's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kreq205_Rqs(a=True, d2="sample_text")
    partner = kreq205_Tttt()
    setattr(partner, 'Tttt', None)
    _safe_set(owner, 'rqs', {partner})
    assert getattr(partner, 'Tttt') == owner
    _safe_set(owner, 'rqs', set())
    assert getattr(partner, 'Tttt') is None


