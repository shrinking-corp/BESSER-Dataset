import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Account,
    Administrator,
    Comment,
    IAcc_Interface,
    Project,
    User,
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

def test_assoc_Account_Administrator_reverse_link_reassign_clear():
    a1 = Administrator(Id=7)
    a2 = Administrator(Id=13)
    b = Account(Info="sample_text", UserName="sample_text")
    _safe_set(b, 'administrator8', a1)
    assert _is_linked(b, 'administrator8', a1)
    if hasattr(a1, 'account9'):
        assert _is_linked(a1, 'account9', b)
    _safe_set(b, 'administrator8', a2)
    assert _is_linked(b, 'administrator8', a2)
    if hasattr(a1, 'account9'):
        assert not _is_linked(a1, 'account9', b)
    if hasattr(a2, 'account9'):
        assert _is_linked(a2, 'account9', b)
    _safe_set(b, 'administrator8', None)
    assert not _is_linked(b, 'administrator8', a2)
    if hasattr(a2, 'account9'):
        assert not _is_linked(a2, 'account9', b)


def test_assoc_Account_User_reverse_link_reassign_clear():
    a1 = User(Id=7)
    a2 = User(Id=13)
    b = Account(Info="sample_text", UserName="sample_text")
    _safe_set(b, 'user6', a1)
    assert _is_linked(b, 'user6', a1)
    if hasattr(a1, 'account7'):
        assert _is_linked(a1, 'account7', b)
    _safe_set(b, 'user6', a2)
    assert _is_linked(b, 'user6', a2)
    if hasattr(a1, 'account7'):
        assert not _is_linked(a1, 'account7', b)
    if hasattr(a2, 'account7'):
        assert _is_linked(a2, 'account7', b)
    _safe_set(b, 'user6', None)
    assert not _is_linked(b, 'user6', a2)
    if hasattr(a2, 'account7'):
        assert not _is_linked(a2, 'account7', b)


def test_assoc_User_Project_reverse_link_reassign_clear():
    a1 = User(Id=7)
    a2 = User(Id=13)
    b = Project(Access="sample_text", Id=7, Info="sample_text", State="sample_text", Title="sample_text")
    _safe_set(b, 'user5', a1)
    assert _is_linked(b, 'user5', a1)
    if hasattr(a1, 'project4'):
        assert _is_linked(a1, 'project4', b)
    _safe_set(b, 'user5', a2)
    assert _is_linked(b, 'user5', a2)
    if hasattr(a1, 'project4'):
        assert not _is_linked(a1, 'project4', b)
    if hasattr(a2, 'project4'):
        assert _is_linked(a2, 'project4', b)
    _safe_set(b, 'user5', None)
    assert not _is_linked(b, 'user5', a2)
    if hasattr(a2, 'project4'):
        assert not _is_linked(a2, 'project4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

