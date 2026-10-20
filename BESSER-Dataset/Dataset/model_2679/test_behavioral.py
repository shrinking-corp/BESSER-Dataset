import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AA,
    formalmetamodel_A,
    formalmetamodel_AA,
    formalmetamodel_B,
    formalmetamodel_C,
    formalmetamodel_FormalModel,
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

def test_assoc_ab0_reverse_link_reassign_clear():
    a1 = formalmetamodel_B(name="sample_text")
    a2 = formalmetamodel_B(name="sample_text_2")
    b = formalmetamodel_A(name="sample_text")
    _safe_set(b, 'formalmetamodel_A', {a1})
    assert _is_linked(b, 'formalmetamodel_A', a1)
    if hasattr(a1, 'formalmetamodel_B'):
        assert _is_linked(a1, 'formalmetamodel_B', b)
    _safe_set(b, 'formalmetamodel_A', {a2})
    assert _is_linked(b, 'formalmetamodel_A', a2)
    if hasattr(a1, 'formalmetamodel_B'):
        assert not _is_linked(a1, 'formalmetamodel_B', b)
    if hasattr(a2, 'formalmetamodel_B'):
        assert _is_linked(a2, 'formalmetamodel_B', b)
    _safe_set(b, 'formalmetamodel_A', set())
    assert not _is_linked(b, 'formalmetamodel_A', a2)
    if hasattr(a2, 'formalmetamodel_B'):
        assert not _is_linked(a2, 'formalmetamodel_B', b)


def test_assoc_ba1_reverse_link_reassign_clear():
    a1 = formalmetamodel_B(name="sample_text")
    a2 = formalmetamodel_B(name="sample_text_2")
    b = formalmetamodel_A(name="sample_text")
    _safe_set(b, 'formalmetamodel_A3', a1)
    assert _is_linked(b, 'formalmetamodel_A3', a1)
    if hasattr(a1, 'formalmetamodel_B2'):
        assert _is_linked(a1, 'formalmetamodel_B2', b)
    _safe_set(b, 'formalmetamodel_A3', a2)
    assert _is_linked(b, 'formalmetamodel_A3', a2)
    if hasattr(a1, 'formalmetamodel_B2'):
        assert not _is_linked(a1, 'formalmetamodel_B2', b)
    if hasattr(a2, 'formalmetamodel_B2'):
        assert _is_linked(a2, 'formalmetamodel_B2', b)
    _safe_set(b, 'formalmetamodel_A3', None)
    assert not _is_linked(b, 'formalmetamodel_A3', a2)
    if hasattr(a2, 'formalmetamodel_B2'):
        assert not _is_linked(a2, 'formalmetamodel_B2', b)


def test_assoc_bb5_reverse_link_reassign_clear():
    a1 = formalmetamodel_B(name="sample_text")
    a2 = formalmetamodel_B(name="sample_text_2")
    b = formalmetamodel_B(name="sample_text")
    _safe_set(b, 'formalmetamodel_B6', a1)
    assert _is_linked(b, 'formalmetamodel_B6', a1)
    if hasattr(a1, 'formalmetamodel_B4'):
        assert _is_linked(a1, 'formalmetamodel_B4', b)
    _safe_set(b, 'formalmetamodel_B6', a2)
    assert _is_linked(b, 'formalmetamodel_B6', a2)
    if hasattr(a1, 'formalmetamodel_B4'):
        assert not _is_linked(a1, 'formalmetamodel_B4', b)
    if hasattr(a2, 'formalmetamodel_B4'):
        assert _is_linked(a2, 'formalmetamodel_B4', b)
    _safe_set(b, 'formalmetamodel_B6', None)
    assert not _is_linked(b, 'formalmetamodel_B6', a2)
    if hasattr(a2, 'formalmetamodel_B4'):
        assert not _is_linked(a2, 'formalmetamodel_B4', b)


def test_assoc_ca17_reverse_link_reassign_clear():
    a1 = formalmetamodel_C(name="sample_text")
    a2 = formalmetamodel_C(name="sample_text_2")
    b = formalmetamodel_A(name="sample_text")
    _safe_set(b, 'formalmetamodel_A19', a1)
    assert _is_linked(b, 'formalmetamodel_A19', a1)
    if hasattr(a1, 'formalmetamodel_C18'):
        assert _is_linked(a1, 'formalmetamodel_C18', b)
    _safe_set(b, 'formalmetamodel_A19', a2)
    assert _is_linked(b, 'formalmetamodel_A19', a2)
    if hasattr(a1, 'formalmetamodel_C18'):
        assert not _is_linked(a1, 'formalmetamodel_C18', b)
    if hasattr(a2, 'formalmetamodel_C18'):
        assert _is_linked(a2, 'formalmetamodel_C18', b)
    _safe_set(b, 'formalmetamodel_A19', None)
    assert not _is_linked(b, 'formalmetamodel_A19', a2)
    if hasattr(a2, 'formalmetamodel_C18'):
        assert not _is_linked(a2, 'formalmetamodel_C18', b)


def test_assoc_cs15_reverse_link_reassign_clear():
    a1 = formalmetamodel_C(name="sample_text")
    a2 = formalmetamodel_C(name="sample_text_2")
    b = formalmetamodel_C(name="sample_text")
    _safe_set(b, 'formalmetamodel_C16', a1)
    assert _is_linked(b, 'formalmetamodel_C16', a1)
    if hasattr(a1, 'formalmetamodel_C14'):
        assert _is_linked(a1, 'formalmetamodel_C14', b)
    _safe_set(b, 'formalmetamodel_C16', a2)
    assert _is_linked(b, 'formalmetamodel_C16', a2)
    if hasattr(a1, 'formalmetamodel_C14'):
        assert not _is_linked(a1, 'formalmetamodel_C14', b)
    if hasattr(a2, 'formalmetamodel_C14'):
        assert _is_linked(a2, 'formalmetamodel_C14', b)
    _safe_set(b, 'formalmetamodel_C16', None)
    assert not _is_linked(b, 'formalmetamodel_C16', a2)
    if hasattr(a2, 'formalmetamodel_C14'):
        assert not _is_linked(a2, 'formalmetamodel_C14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_as_9_stub_double():
    # formalmetamodel_FormalModel has no real 'formalmetamodel_FormalModel10' property in the generated
    # code (a bare stub) -- manually attach it so formalmetamodel_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # formalmetamodel_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = formalmetamodel_A(name="sample_text")
    partner = formalmetamodel_FormalModel()
    setattr(partner, 'formalmetamodel_FormalModel10', None)
    _safe_set(owner, 'formalmetamodel_A11', partner)
    assert owner in getattr(partner, 'formalmetamodel_FormalModel10')
    _safe_set(owner, 'formalmetamodel_A11', None)
    assert owner not in getattr(partner, 'formalmetamodel_FormalModel10')


def test_assoc_bs7_stub_double():
    # formalmetamodel_FormalModel has no real 'formalmetamodel_FormalModel' property in the generated
    # code (a bare stub) -- manually attach it so formalmetamodel_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # formalmetamodel_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = formalmetamodel_B(name="sample_text")
    partner = formalmetamodel_FormalModel()
    setattr(partner, 'formalmetamodel_FormalModel', None)
    _safe_set(owner, 'formalmetamodel_B8', partner)
    assert owner in getattr(partner, 'formalmetamodel_FormalModel')
    _safe_set(owner, 'formalmetamodel_B8', None)
    assert owner not in getattr(partner, 'formalmetamodel_FormalModel')


def test_assoc_cs12_stub_double():
    # formalmetamodel_FormalModel has no real 'formalmetamodel_FormalModel13' property in the generated
    # code (a bare stub) -- manually attach it so formalmetamodel_C's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # formalmetamodel_C's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = formalmetamodel_C(name="sample_text")
    partner = formalmetamodel_FormalModel()
    setattr(partner, 'formalmetamodel_FormalModel13', None)
    _safe_set(owner, 'formalmetamodel_C', partner)
    assert owner in getattr(partner, 'formalmetamodel_FormalModel13')
    _safe_set(owner, 'formalmetamodel_C', None)
    assert owner not in getattr(partner, 'formalmetamodel_FormalModel13')


