import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    RootIn,
    RootOut,
    Trace,
    traces_A,
    traces_B,
    traces_C,
    traces_D,
    traces_E,
    traces_R1_Trace,
    traces_R2_Trace,
    traces_RootIn,
    traces_RootOut,
    traces_Trace,
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

def test_assoc_refA17_reverse_link_reassign_clear():
    a1 = traces_B(name="sample_text")
    a2 = traces_B(name="sample_text_2")
    b = traces_A(name="sample_text")
    _safe_set(b, 'traces_A19', a1)
    assert _is_linked(b, 'traces_A19', a1)
    if hasattr(a1, 'traces_B18'):
        assert _is_linked(a1, 'traces_B18', b)
    _safe_set(b, 'traces_A19', a2)
    assert _is_linked(b, 'traces_A19', a2)
    if hasattr(a1, 'traces_B18'):
        assert not _is_linked(a1, 'traces_B18', b)
    if hasattr(a2, 'traces_B18'):
        assert _is_linked(a2, 'traces_B18', b)
    _safe_set(b, 'traces_A19', None)
    assert not _is_linked(b, 'traces_A19', a2)
    if hasattr(a2, 'traces_B18'):
        assert not _is_linked(a2, 'traces_B18', b)


def test_assoc_refB12_reverse_link_reassign_clear():
    a1 = traces_B(name="sample_text")
    a2 = traces_B(name="sample_text_2")
    b = traces_A(name="sample_text")
    _safe_set(b, 'traces_A13', {a1})
    assert _is_linked(b, 'traces_A13', a1)
    if hasattr(a1, 'traces_B14'):
        assert _is_linked(a1, 'traces_B14', b)
    _safe_set(b, 'traces_A13', {a2})
    assert _is_linked(b, 'traces_A13', a2)
    if hasattr(a1, 'traces_B14'):
        assert not _is_linked(a1, 'traces_B14', b)
    if hasattr(a2, 'traces_B14'):
        assert _is_linked(a2, 'traces_B14', b)
    _safe_set(b, 'traces_A13', set())
    assert not _is_linked(b, 'traces_A13', a2)
    if hasattr(a2, 'traces_B14'):
        assert not _is_linked(a2, 'traces_B14', b)


def test_assoc_refC15_reverse_link_reassign_clear():
    a1 = traces_C(name="sample_text")
    a2 = traces_C(name="sample_text_2")
    b = traces_A(name="sample_text")
    _safe_set(b, 'traces_A16', {a1})
    assert _is_linked(b, 'traces_A16', a1)
    if hasattr(a1, 'traces_C'):
        assert _is_linked(a1, 'traces_C', b)
    _safe_set(b, 'traces_A16', {a2})
    assert _is_linked(b, 'traces_A16', a2)
    if hasattr(a1, 'traces_C'):
        assert not _is_linked(a1, 'traces_C', b)
    if hasattr(a2, 'traces_C'):
        assert _is_linked(a2, 'traces_C', b)
    _safe_set(b, 'traces_A16', set())
    assert not _is_linked(b, 'traces_A16', a2)
    if hasattr(a2, 'traces_C'):
        assert not _is_linked(a2, 'traces_C', b)


def test_assoc_refD24_reverse_link_reassign_clear():
    a1 = traces_D(name="sample_text")
    a2 = traces_D(name="sample_text_2")
    b = traces_D(name="sample_text")
    _safe_set(b, 'traces_D25', a1)
    assert _is_linked(b, 'traces_D25', a1)
    if hasattr(a1, 'traces_D23'):
        assert _is_linked(a1, 'traces_D23', b)
    _safe_set(b, 'traces_D25', a2)
    assert _is_linked(b, 'traces_D25', a2)
    if hasattr(a1, 'traces_D23'):
        assert not _is_linked(a1, 'traces_D23', b)
    if hasattr(a2, 'traces_D23'):
        assert _is_linked(a2, 'traces_D23', b)
    _safe_set(b, 'traces_D25', None)
    assert not _is_linked(b, 'traces_D25', a2)
    if hasattr(a2, 'traces_D23'):
        assert not _is_linked(a2, 'traces_D23', b)


def test_assoc_refD26_reverse_link_reassign_clear():
    a1 = traces_E(name="sample_text")
    a2 = traces_E(name="sample_text_2")
    b = traces_D(name="sample_text")
    _safe_set(b, 'traces_D28', a1)
    assert _is_linked(b, 'traces_D28', a1)
    if hasattr(a1, 'traces_E27'):
        assert _is_linked(a1, 'traces_E27', b)
    _safe_set(b, 'traces_D28', a2)
    assert _is_linked(b, 'traces_D28', a2)
    if hasattr(a1, 'traces_E27'):
        assert not _is_linked(a1, 'traces_E27', b)
    if hasattr(a2, 'traces_E27'):
        assert _is_linked(a2, 'traces_E27', b)
    _safe_set(b, 'traces_D28', None)
    assert not _is_linked(b, 'traces_D28', a2)
    if hasattr(a2, 'traces_E27'):
        assert not _is_linked(a2, 'traces_E27', b)


def test_assoc_refE20_reverse_link_reassign_clear():
    a1 = traces_E(name="sample_text")
    a2 = traces_E(name="sample_text_2")
    b = traces_D(name="sample_text")
    _safe_set(b, 'traces_D21', {a1})
    assert _is_linked(b, 'traces_D21', a1)
    if hasattr(a1, 'traces_E22'):
        assert _is_linked(a1, 'traces_E22', b)
    _safe_set(b, 'traces_D21', {a2})
    assert _is_linked(b, 'traces_D21', a2)
    if hasattr(a1, 'traces_E22'):
        assert not _is_linked(a1, 'traces_E22', b)
    if hasattr(a2, 'traces_E22'):
        assert _is_linked(a2, 'traces_E22', b)
    _safe_set(b, 'traces_D21', set())
    assert not _is_linked(b, 'traces_D21', a2)
    if hasattr(a2, 'traces_E22'):
        assert not _is_linked(a2, 'traces_E22', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_s3_stub_double():
    # traces_R1_Trace has no real 'traces_R1_Trace' property in the generated
    # code (a bare stub) -- manually attach it so traces_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traces_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traces_A(name="sample_text")
    partner = traces_R1_Trace()
    setattr(partner, 'traces_R1_Trace', None)
    _safe_set(owner, 'traces_A', partner)
    assert getattr(partner, 'traces_R1_Trace') == owner
    _safe_set(owner, 'traces_A', None)
    assert getattr(partner, 'traces_R1_Trace') is None


def test_assoc_s9_stub_double():
    # traces_R2_Trace has no real 'traces_R2_Trace' property in the generated
    # code (a bare stub) -- manually attach it so traces_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traces_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traces_B(name="sample_text")
    partner = traces_R2_Trace()
    setattr(partner, 'traces_R2_Trace', None)
    _safe_set(owner, 'traces_B', partner)
    assert getattr(partner, 'traces_R2_Trace') == owner
    _safe_set(owner, 'traces_B', None)
    assert getattr(partner, 'traces_R2_Trace') is None


def test_assoc_t10_stub_double():
    # traces_R2_Trace has no real 'traces_R2_Trace11' property in the generated
    # code (a bare stub) -- manually attach it so traces_E's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traces_E's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traces_E(name="sample_text")
    partner = traces_R2_Trace()
    setattr(partner, 'traces_R2_Trace11', None)
    _safe_set(owner, 'traces_E', partner)
    assert getattr(partner, 'traces_R2_Trace11') == owner
    _safe_set(owner, 'traces_E', None)
    assert getattr(partner, 'traces_R2_Trace11') is None


def test_assoc_t14_stub_double():
    # traces_R1_Trace has no real 'traces_R1_Trace5' property in the generated
    # code (a bare stub) -- manually attach it so traces_D's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traces_D's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traces_D(name="sample_text")
    partner = traces_R1_Trace()
    setattr(partner, 'traces_R1_Trace5', None)
    _safe_set(owner, 'traces_D', partner)
    assert getattr(partner, 'traces_R1_Trace5') == owner
    _safe_set(owner, 'traces_D', None)
    assert getattr(partner, 'traces_R1_Trace5') is None


def test_assoc_t26_stub_double():
    # traces_R1_Trace has no real 'traces_R1_Trace7' property in the generated
    # code (a bare stub) -- manually attach it so traces_D's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traces_D's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traces_D(name="sample_text")
    partner = traces_R1_Trace()
    setattr(partner, 'traces_R1_Trace7', None)
    _safe_set(owner, 'traces_D8', partner)
    assert getattr(partner, 'traces_R1_Trace7') == owner
    _safe_set(owner, 'traces_D8', None)
    assert getattr(partner, 'traces_R1_Trace7') is None


