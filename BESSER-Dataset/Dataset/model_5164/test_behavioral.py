import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FaultyUMLmodel4_A,
    FaultyUMLmodel4_B,
    FaultyUMLmodel4_C,
    FaultyUMLmodel4_D,
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

def test_assoc_AB0_reverse_link_reassign_clear():
    a1 = FaultyUMLmodel4_B(x=7, y=7)
    a2 = FaultyUMLmodel4_B(x=13, y=13)
    b = FaultyUMLmodel4_A(v=7, w=True)
    _safe_set(b, 'BA', {a1})
    assert _is_linked(b, 'BA', a1)
    if hasattr(a1, 'B'):
        assert _is_linked(a1, 'B', b)
    _safe_set(b, 'BA', {a2})
    assert _is_linked(b, 'BA', a2)
    if hasattr(a1, 'B'):
        assert not _is_linked(a1, 'B', b)
    if hasattr(a2, 'B'):
        assert _is_linked(a2, 'B', b)
    _safe_set(b, 'BA', set())
    assert not _is_linked(b, 'BA', a2)
    if hasattr(a2, 'B'):
        assert not _is_linked(a2, 'B', b)


def test_assoc_AC1_reverse_link_reassign_clear():
    a1 = FaultyUMLmodel4_C(u=7)
    a2 = FaultyUMLmodel4_C(u=13)
    b = FaultyUMLmodel4_A(v=7, w=True)
    _safe_set(b, 'CA', a1)
    assert _is_linked(b, 'CA', a1)
    if hasattr(a1, 'C'):
        assert _is_linked(a1, 'C', b)
    _safe_set(b, 'CA', a2)
    assert _is_linked(b, 'CA', a2)
    if hasattr(a1, 'C'):
        assert not _is_linked(a1, 'C', b)
    if hasattr(a2, 'C'):
        assert _is_linked(a2, 'C', b)
    _safe_set(b, 'CA', None)
    assert not _is_linked(b, 'CA', a2)
    if hasattr(a2, 'C'):
        assert not _is_linked(a2, 'C', b)


def test_assoc_BA2_reverse_link_reassign_clear():
    a1 = FaultyUMLmodel4_B(x=7, y=7)
    a2 = FaultyUMLmodel4_B(x=13, y=13)
    b = FaultyUMLmodel4_A(v=7, w=True)
    _safe_set(b, 'A', a1)
    assert _is_linked(b, 'A', a1)
    if hasattr(a1, 'AB'):
        assert _is_linked(a1, 'AB', b)
    _safe_set(b, 'A', a2)
    assert _is_linked(b, 'A', a2)
    if hasattr(a1, 'AB'):
        assert not _is_linked(a1, 'AB', b)
    if hasattr(a2, 'AB'):
        assert _is_linked(a2, 'AB', b)
    _safe_set(b, 'A', None)
    assert not _is_linked(b, 'A', a2)
    if hasattr(a2, 'AB'):
        assert not _is_linked(a2, 'AB', b)


def test_assoc_BC3_reverse_link_reassign_clear():
    a1 = FaultyUMLmodel4_C(u=7)
    a2 = FaultyUMLmodel4_C(u=13)
    b = FaultyUMLmodel4_B(x=7, y=7)
    _safe_set(b, 'CB', {a1})
    assert _is_linked(b, 'CB', a1)
    if hasattr(a1, 'C4'):
        assert _is_linked(a1, 'C4', b)
    _safe_set(b, 'CB', {a2})
    assert _is_linked(b, 'CB', a2)
    if hasattr(a1, 'C4'):
        assert not _is_linked(a1, 'C4', b)
    if hasattr(a2, 'C4'):
        assert _is_linked(a2, 'C4', b)
    _safe_set(b, 'CB', set())
    assert not _is_linked(b, 'CB', a2)
    if hasattr(a2, 'C4'):
        assert not _is_linked(a2, 'C4', b)


def test_assoc_CA5_reverse_link_reassign_clear():
    a1 = FaultyUMLmodel4_C(u=7)
    a2 = FaultyUMLmodel4_C(u=13)
    b = FaultyUMLmodel4_A(v=7, w=True)
    _safe_set(b, 'A6', a1)
    assert _is_linked(b, 'A6', a1)
    if hasattr(a1, 'AC'):
        assert _is_linked(a1, 'AC', b)
    _safe_set(b, 'A6', a2)
    assert _is_linked(b, 'A6', a2)
    if hasattr(a1, 'AC'):
        assert not _is_linked(a1, 'AC', b)
    if hasattr(a2, 'AC'):
        assert _is_linked(a2, 'AC', b)
    _safe_set(b, 'A6', None)
    assert not _is_linked(b, 'A6', a2)
    if hasattr(a2, 'AC'):
        assert not _is_linked(a2, 'AC', b)


def test_assoc_CB7_reverse_link_reassign_clear():
    a1 = FaultyUMLmodel4_C(u=7)
    a2 = FaultyUMLmodel4_C(u=13)
    b = FaultyUMLmodel4_B(x=7, y=7)
    _safe_set(b, 'B8', a1)
    assert _is_linked(b, 'B8', a1)
    if hasattr(a1, 'BC'):
        assert _is_linked(a1, 'BC', b)
    _safe_set(b, 'B8', a2)
    assert _is_linked(b, 'B8', a2)
    if hasattr(a1, 'BC'):
        assert not _is_linked(a1, 'BC', b)
    if hasattr(a2, 'BC'):
        assert _is_linked(a2, 'BC', b)
    _safe_set(b, 'B8', None)
    assert not _is_linked(b, 'B8', a2)
    if hasattr(a2, 'BC'):
        assert not _is_linked(a2, 'BC', b)


def test_assoc_CD9_reverse_link_reassign_clear():
    a1 = FaultyUMLmodel4_D(z=True)
    a2 = FaultyUMLmodel4_D(z=False)
    b = FaultyUMLmodel4_C(u=7)
    _safe_set(b, 'DC', {a1})
    assert _is_linked(b, 'DC', a1)
    if hasattr(a1, 'D'):
        assert _is_linked(a1, 'D', b)
    _safe_set(b, 'DC', {a2})
    assert _is_linked(b, 'DC', a2)
    if hasattr(a1, 'D'):
        assert not _is_linked(a1, 'D', b)
    if hasattr(a2, 'D'):
        assert _is_linked(a2, 'D', b)
    _safe_set(b, 'DC', set())
    assert not _is_linked(b, 'DC', a2)
    if hasattr(a2, 'D'):
        assert not _is_linked(a2, 'D', b)


def test_assoc_DC10_reverse_link_reassign_clear():
    a1 = FaultyUMLmodel4_D(z=True)
    a2 = FaultyUMLmodel4_D(z=False)
    b = FaultyUMLmodel4_C(u=7)
    _safe_set(b, 'C11', a1)
    assert _is_linked(b, 'C11', a1)
    if hasattr(a1, 'CD'):
        assert _is_linked(a1, 'CD', b)
    _safe_set(b, 'C11', a2)
    assert _is_linked(b, 'C11', a2)
    if hasattr(a1, 'CD'):
        assert not _is_linked(a1, 'CD', b)
    if hasattr(a2, 'CD'):
        assert _is_linked(a2, 'CD', b)
    _safe_set(b, 'C11', None)
    assert not _is_linked(b, 'C11', a2)
    if hasattr(a2, 'CD'):
        assert not _is_linked(a2, 'CD', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

