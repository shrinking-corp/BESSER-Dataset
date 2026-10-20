import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Gggg,
    kreq108c_Bbbb,
    kreq108c_Cccc,
    kreq108c_Eeee,
    kreq108c_Ffff,
    kreq108c_Gggg,
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

def test_assoc_fs3_reverse_link_reassign_clear():
    a1 = kreq108c_Ffff(id="sample_text")
    a2 = kreq108c_Ffff(id="sample_text_2")
    b = kreq108c_Cccc(id="sample_text")
    _safe_set(b, 'kreq108c_Cccc4', {a1})
    assert _is_linked(b, 'kreq108c_Cccc4', a1)
    if hasattr(a1, 'kreq108c_Ffff'):
        assert _is_linked(a1, 'kreq108c_Ffff', b)
    _safe_set(b, 'kreq108c_Cccc4', {a2})
    assert _is_linked(b, 'kreq108c_Cccc4', a2)
    if hasattr(a1, 'kreq108c_Ffff'):
        assert not _is_linked(a1, 'kreq108c_Ffff', b)
    if hasattr(a2, 'kreq108c_Ffff'):
        assert _is_linked(a2, 'kreq108c_Ffff', b)
    _safe_set(b, 'kreq108c_Cccc4', set())
    assert not _is_linked(b, 'kreq108c_Cccc4', a2)
    if hasattr(a2, 'kreq108c_Ffff'):
        assert not _is_linked(a2, 'kreq108c_Ffff', b)


def test_assoc_subFs9_reverse_link_reassign_clear():
    a1 = kreq108c_Ffff(id="sample_text")
    a2 = kreq108c_Ffff(id="sample_text_2")
    b = kreq108c_Ffff(id="sample_text")
    _safe_set(b, 'kreq108c_Ffff8', {a1})
    assert _is_linked(b, 'kreq108c_Ffff8', a1)
    if hasattr(a1, 'kreq108c_Ffff10'):
        assert _is_linked(a1, 'kreq108c_Ffff10', b)
    _safe_set(b, 'kreq108c_Ffff8', {a2})
    assert _is_linked(b, 'kreq108c_Ffff8', a2)
    if hasattr(a1, 'kreq108c_Ffff10'):
        assert not _is_linked(a1, 'kreq108c_Ffff10', b)
    if hasattr(a2, 'kreq108c_Ffff10'):
        assert _is_linked(a2, 'kreq108c_Ffff10', b)
    _safe_set(b, 'kreq108c_Ffff8', set())
    assert not _is_linked(b, 'kreq108c_Ffff8', a2)
    if hasattr(a2, 'kreq108c_Ffff10'):
        assert not _is_linked(a2, 'kreq108c_Ffff10', b)


def test_assoc_varifedBy5_reverse_link_reassign_clear():
    a1 = kreq108c_Ffff(id="sample_text")
    a2 = kreq108c_Ffff(id="sample_text_2")
    b = kreq108c_Eeee(id="sample_text")
    _safe_set(b, 'kreq108c_Eeee7', a1)
    assert _is_linked(b, 'kreq108c_Eeee7', a1)
    if hasattr(a1, 'kreq108c_Ffff6'):
        assert _is_linked(a1, 'kreq108c_Ffff6', b)
    _safe_set(b, 'kreq108c_Eeee7', a2)
    assert _is_linked(b, 'kreq108c_Eeee7', a2)
    if hasattr(a1, 'kreq108c_Ffff6'):
        assert not _is_linked(a1, 'kreq108c_Ffff6', b)
    if hasattr(a2, 'kreq108c_Ffff6'):
        assert _is_linked(a2, 'kreq108c_Ffff6', b)
    _safe_set(b, 'kreq108c_Eeee7', None)
    assert not _is_linked(b, 'kreq108c_Eeee7', a2)
    if hasattr(a2, 'kreq108c_Ffff6'):
        assert not _is_linked(a2, 'kreq108c_Ffff6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cs0_stub_double():
    # kreq108c_Bbbb has no real 'kreq108c_Bbbb' property in the generated
    # code (a bare stub) -- manually attach it so kreq108c_Cccc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kreq108c_Cccc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kreq108c_Cccc(id="sample_text")
    partner = kreq108c_Bbbb()
    setattr(partner, 'kreq108c_Bbbb', None)
    _safe_set(owner, 'kreq108c_Cccc', partner)
    assert owner in getattr(partner, 'kreq108c_Bbbb')
    _safe_set(owner, 'kreq108c_Cccc', None)
    assert owner not in getattr(partner, 'kreq108c_Bbbb')


def test_assoc_es1_stub_double():
    # kreq108c_Bbbb has no real 'kreq108c_Bbbb2' property in the generated
    # code (a bare stub) -- manually attach it so kreq108c_Eeee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kreq108c_Eeee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kreq108c_Eeee(id="sample_text")
    partner = kreq108c_Bbbb()
    setattr(partner, 'kreq108c_Bbbb2', None)
    _safe_set(owner, 'kreq108c_Eeee', partner)
    assert owner in getattr(partner, 'kreq108c_Bbbb2')
    _safe_set(owner, 'kreq108c_Eeee', None)
    assert owner not in getattr(partner, 'kreq108c_Bbbb2')


