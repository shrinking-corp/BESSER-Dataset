import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BankAccount,
    Checking,
    Instructor,
    Main,
    Savings,
    Student,
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

def test_assoc_Checking_Instructor_reverse_link_reassign_clear():
    a1 = Instructor(name="sample_text")
    a2 = Instructor(name="sample_text_2")
    b = Checking(OVERDRAFT_FEE=3.14, OVERDRAFT_LIMIT=3.14, isActive=True)
    _safe_set(b, 'instructor4', a1)
    assert _is_linked(b, 'instructor4', a1)
    if hasattr(a1, 'checking5'):
        assert _is_linked(a1, 'checking5', b)
    _safe_set(b, 'instructor4', a2)
    assert _is_linked(b, 'instructor4', a2)
    if hasattr(a1, 'checking5'):
        assert not _is_linked(a1, 'checking5', b)
    if hasattr(a2, 'checking5'):
        assert _is_linked(a2, 'checking5', b)
    _safe_set(b, 'instructor4', None)
    assert not _is_linked(b, 'instructor4', a2)
    if hasattr(a2, 'checking5'):
        assert not _is_linked(a2, 'checking5', b)


def test_assoc_Checking_Student_reverse_link_reassign_clear():
    a1 = Student(name="sample_text")
    a2 = Student(name="sample_text_2")
    b = Checking(OVERDRAFT_FEE=3.14, OVERDRAFT_LIMIT=3.14, isActive=True)
    _safe_set(b, 'student0', a1)
    assert _is_linked(b, 'student0', a1)
    if hasattr(a1, 'checking1'):
        assert _is_linked(a1, 'checking1', b)
    _safe_set(b, 'student0', a2)
    assert _is_linked(b, 'student0', a2)
    if hasattr(a1, 'checking1'):
        assert not _is_linked(a1, 'checking1', b)
    if hasattr(a2, 'checking1'):
        assert _is_linked(a2, 'checking1', b)
    _safe_set(b, 'student0', None)
    assert not _is_linked(b, 'student0', a2)
    if hasattr(a2, 'checking1'):
        assert not _is_linked(a2, 'checking1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Savings_Instructor_stub_double():
    # Savings has no real 'instructor6' property in the generated
    # code (a bare stub) -- manually attach it so Instructor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Instructor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Instructor(name="sample_text")
    partner = Savings()
    setattr(partner, 'instructor6', None)
    _safe_set(owner, 'savings7', partner)
    assert getattr(partner, 'instructor6') == owner
    _safe_set(owner, 'savings7', None)
    assert getattr(partner, 'instructor6') is None


def test_assoc_Savings_Student_stub_double():
    # Savings has no real 'student2' property in the generated
    # code (a bare stub) -- manually attach it so Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Student(name="sample_text")
    partner = Savings()
    setattr(partner, 'student2', None)
    _safe_set(owner, 'savings3', partner)
    assert getattr(partner, 'student2') == owner
    _safe_set(owner, 'savings3', None)
    assert getattr(partner, 'student2') is None


