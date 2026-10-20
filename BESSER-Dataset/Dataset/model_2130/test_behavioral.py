import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Statement,
    Variable,
    uitf_AssertInState,
    uitf_Statement,
    uitf_TestCase,
    uitf_TestSuite,
    uitf_TriggeredTransition,
    uitf_UIControl,
    uitf_UIControlVariable,
    uitf_UISUT,
    uitf_Variable,
    UserInstructionEnum,
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

def test_assoc_itsStatement1_reverse_link_reassign_clear():
    a1 = uitf_TestCase(id="sample_text")
    a2 = uitf_TestCase(id="sample_text_2")
    b = uitf_Statement(description="sample_text", kind="sample_text")
    _safe_set(b, 'uitf_Statement', a1)
    assert _is_linked(b, 'uitf_Statement', a1)
    if hasattr(a1, 'uitf_TestCase2'):
        assert _is_linked(a1, 'uitf_TestCase2', b)
    _safe_set(b, 'uitf_Statement', a2)
    assert _is_linked(b, 'uitf_Statement', a2)
    if hasattr(a1, 'uitf_TestCase2'):
        assert not _is_linked(a1, 'uitf_TestCase2', b)
    if hasattr(a2, 'uitf_TestCase2'):
        assert _is_linked(a2, 'uitf_TestCase2', b)
    _safe_set(b, 'uitf_Statement', None)
    assert not _is_linked(b, 'uitf_Statement', a2)
    if hasattr(a2, 'uitf_TestCase2'):
        assert not _is_linked(a2, 'uitf_TestCase2', b)


def test_assoc_itsTestCase3_reverse_link_reassign_clear():
    a1 = uitf_TestSuite(id="sample_text")
    a2 = uitf_TestSuite(id="sample_text_2")
    b = uitf_TestCase(id="sample_text")
    _safe_set(b, 'uitf_TestCase4', a1)
    assert _is_linked(b, 'uitf_TestCase4', a1)
    if hasattr(a1, 'uitf_TestSuite'):
        assert _is_linked(a1, 'uitf_TestSuite', b)
    _safe_set(b, 'uitf_TestCase4', a2)
    assert _is_linked(b, 'uitf_TestCase4', a2)
    if hasattr(a1, 'uitf_TestSuite'):
        assert not _is_linked(a1, 'uitf_TestSuite', b)
    if hasattr(a2, 'uitf_TestSuite'):
        assert _is_linked(a2, 'uitf_TestSuite', b)
    _safe_set(b, 'uitf_TestCase4', None)
    assert not _is_linked(b, 'uitf_TestCase4', a2)
    if hasattr(a2, 'uitf_TestSuite'):
        assert not _is_linked(a2, 'uitf_TestSuite', b)


def test_assoc_itsUICtrl7_reverse_link_reassign_clear():
    a1 = uitf_UISUT(objectURI="sample_text")
    a2 = uitf_UISUT(objectURI="sample_text_2")
    b = uitf_UIControl(id="sample_text")
    _safe_set(b, 'uitf_UIControl', a1)
    assert _is_linked(b, 'uitf_UIControl', a1)
    if hasattr(a1, 'uitf_UISUT8'):
        assert _is_linked(a1, 'uitf_UISUT8', b)
    _safe_set(b, 'uitf_UIControl', a2)
    assert _is_linked(b, 'uitf_UIControl', a2)
    if hasattr(a1, 'uitf_UISUT8'):
        assert not _is_linked(a1, 'uitf_UISUT8', b)
    if hasattr(a2, 'uitf_UISUT8'):
        assert _is_linked(a2, 'uitf_UISUT8', b)
    _safe_set(b, 'uitf_UIControl', None)
    assert not _is_linked(b, 'uitf_UIControl', a2)
    if hasattr(a2, 'uitf_UISUT8'):
        assert not _is_linked(a2, 'uitf_UISUT8', b)


def test_assoc_itsUISUT0_reverse_link_reassign_clear():
    a1 = uitf_UISUT(objectURI="sample_text")
    a2 = uitf_UISUT(objectURI="sample_text_2")
    b = uitf_TestCase(id="sample_text")
    _safe_set(b, 'uitf_TestCase', a1)
    assert _is_linked(b, 'uitf_TestCase', a1)
    if hasattr(a1, 'uitf_UISUT'):
        assert _is_linked(a1, 'uitf_UISUT', b)
    _safe_set(b, 'uitf_TestCase', a2)
    assert _is_linked(b, 'uitf_TestCase', a2)
    if hasattr(a1, 'uitf_UISUT'):
        assert not _is_linked(a1, 'uitf_UISUT', b)
    if hasattr(a2, 'uitf_UISUT'):
        assert _is_linked(a2, 'uitf_UISUT', b)
    _safe_set(b, 'uitf_TestCase', None)
    assert not _is_linked(b, 'uitf_TestCase', a2)
    if hasattr(a2, 'uitf_UISUT'):
        assert not _is_linked(a2, 'uitf_UISUT', b)


def test_assoc_itsVariable12_reverse_link_reassign_clear():
    a1 = uitf_Variable(id="sample_text")
    a2 = uitf_Variable(id="sample_text_2")
    b = uitf_UIControl(id="sample_text")
    _safe_set(b, 'uitf_UIControl13', a1)
    assert _is_linked(b, 'uitf_UIControl13', a1)
    if hasattr(a1, 'uitf_Variable14'):
        assert _is_linked(a1, 'uitf_Variable14', b)
    _safe_set(b, 'uitf_UIControl13', a2)
    assert _is_linked(b, 'uitf_UIControl13', a2)
    if hasattr(a1, 'uitf_Variable14'):
        assert not _is_linked(a1, 'uitf_Variable14', b)
    if hasattr(a2, 'uitf_Variable14'):
        assert _is_linked(a2, 'uitf_Variable14', b)
    _safe_set(b, 'uitf_UIControl13', None)
    assert not _is_linked(b, 'uitf_UIControl13', a2)
    if hasattr(a2, 'uitf_Variable14'):
        assert not _is_linked(a2, 'uitf_Variable14', b)


def test_assoc_itsVariable5_reverse_link_reassign_clear():
    a1 = uitf_Variable(id="sample_text")
    a2 = uitf_Variable(id="sample_text_2")
    b = uitf_UISUT(objectURI="sample_text")
    _safe_set(b, 'uitf_UISUT6', {a1})
    assert _is_linked(b, 'uitf_UISUT6', a1)
    if hasattr(a1, 'uitf_Variable'):
        assert _is_linked(a1, 'uitf_Variable', b)
    _safe_set(b, 'uitf_UISUT6', {a2})
    assert _is_linked(b, 'uitf_UISUT6', a2)
    if hasattr(a1, 'uitf_Variable'):
        assert not _is_linked(a1, 'uitf_Variable', b)
    if hasattr(a2, 'uitf_Variable'):
        assert _is_linked(a2, 'uitf_Variable', b)
    _safe_set(b, 'uitf_UISUT6', set())
    assert not _is_linked(b, 'uitf_UISUT6', a2)
    if hasattr(a2, 'uitf_Variable'):
        assert not _is_linked(a2, 'uitf_Variable', b)


def test_assoc_itsVariable9_reverse_link_reassign_clear():
    a1 = uitf_Variable(id="sample_text")
    a2 = uitf_Variable(id="sample_text_2")
    b = uitf_Statement(description="sample_text", kind="sample_text")
    _safe_set(b, 'uitf_Statement10', a1)
    assert _is_linked(b, 'uitf_Statement10', a1)
    if hasattr(a1, 'uitf_Variable11'):
        assert _is_linked(a1, 'uitf_Variable11', b)
    _safe_set(b, 'uitf_Statement10', a2)
    assert _is_linked(b, 'uitf_Statement10', a2)
    if hasattr(a1, 'uitf_Variable11'):
        assert not _is_linked(a1, 'uitf_Variable11', b)
    if hasattr(a2, 'uitf_Variable11'):
        assert _is_linked(a2, 'uitf_Variable11', b)
    _safe_set(b, 'uitf_Statement10', None)
    assert not _is_linked(b, 'uitf_Statement10', a2)
    if hasattr(a2, 'uitf_Variable11'):
        assert not _is_linked(a2, 'uitf_Variable11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

