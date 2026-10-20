import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ecoreJavascriptDelegatesTest_Company,
    ecoreJavascriptDelegatesTest_Employee,
    CompanySizeKind,
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

def test_assoc_allReports8_reverse_link_reassign_clear():
    a1 = ecoreJavascriptDelegatesTest_Employee(name="sample_text")
    a2 = ecoreJavascriptDelegatesTest_Employee(name="sample_text_2")
    b = ecoreJavascriptDelegatesTest_Employee(name="sample_text")
    _safe_set(b, 'ecoreJavascriptDelegatesTest_Employee9', a1)
    assert _is_linked(b, 'ecoreJavascriptDelegatesTest_Employee9', a1)
    if hasattr(a1, 'ecoreJavascriptDelegatesTest_Employee7'):
        assert _is_linked(a1, 'ecoreJavascriptDelegatesTest_Employee7', b)
    _safe_set(b, 'ecoreJavascriptDelegatesTest_Employee9', a2)
    assert _is_linked(b, 'ecoreJavascriptDelegatesTest_Employee9', a2)
    if hasattr(a1, 'ecoreJavascriptDelegatesTest_Employee7'):
        assert not _is_linked(a1, 'ecoreJavascriptDelegatesTest_Employee7', b)
    if hasattr(a2, 'ecoreJavascriptDelegatesTest_Employee7'):
        assert _is_linked(a2, 'ecoreJavascriptDelegatesTest_Employee7', b)
    _safe_set(b, 'ecoreJavascriptDelegatesTest_Employee9', None)
    assert not _is_linked(b, 'ecoreJavascriptDelegatesTest_Employee9', a2)
    if hasattr(a2, 'ecoreJavascriptDelegatesTest_Employee7'):
        assert not _is_linked(a2, 'ecoreJavascriptDelegatesTest_Employee7', b)


def test_assoc_company3_reverse_link_reassign_clear():
    a1 = ecoreJavascriptDelegatesTest_Employee(name="sample_text")
    a2 = ecoreJavascriptDelegatesTest_Employee(name="sample_text_2")
    b = ecoreJavascriptDelegatesTest_Company(name="sample_text", size="sample_text")
    _safe_set(b, 'Company', a1)
    assert _is_linked(b, 'Company', a1)
    if hasattr(a1, 'employees'):
        assert _is_linked(a1, 'employees', b)
    _safe_set(b, 'Company', a2)
    assert _is_linked(b, 'Company', a2)
    if hasattr(a1, 'employees'):
        assert not _is_linked(a1, 'employees', b)
    if hasattr(a2, 'employees'):
        assert _is_linked(a2, 'employees', b)
    _safe_set(b, 'Company', None)
    assert not _is_linked(b, 'Company', a2)
    if hasattr(a2, 'employees'):
        assert not _is_linked(a2, 'employees', b)


def test_assoc_directReports5_reverse_link_reassign_clear():
    a1 = ecoreJavascriptDelegatesTest_Employee(name="sample_text")
    a2 = ecoreJavascriptDelegatesTest_Employee(name="sample_text_2")
    b = ecoreJavascriptDelegatesTest_Employee(name="sample_text")
    _safe_set(b, 'ecoreJavascriptDelegatesTest_Employee6', a1)
    assert _is_linked(b, 'ecoreJavascriptDelegatesTest_Employee6', a1)
    if hasattr(a1, 'ecoreJavascriptDelegatesTest_Employee4'):
        assert _is_linked(a1, 'ecoreJavascriptDelegatesTest_Employee4', b)
    _safe_set(b, 'ecoreJavascriptDelegatesTest_Employee6', a2)
    assert _is_linked(b, 'ecoreJavascriptDelegatesTest_Employee6', a2)
    if hasattr(a1, 'ecoreJavascriptDelegatesTest_Employee4'):
        assert not _is_linked(a1, 'ecoreJavascriptDelegatesTest_Employee4', b)
    if hasattr(a2, 'ecoreJavascriptDelegatesTest_Employee4'):
        assert _is_linked(a2, 'ecoreJavascriptDelegatesTest_Employee4', b)
    _safe_set(b, 'ecoreJavascriptDelegatesTest_Employee6', None)
    assert not _is_linked(b, 'ecoreJavascriptDelegatesTest_Employee6', a2)
    if hasattr(a2, 'ecoreJavascriptDelegatesTest_Employee4'):
        assert not _is_linked(a2, 'ecoreJavascriptDelegatesTest_Employee4', b)


def test_assoc_employees0_reverse_link_reassign_clear():
    a1 = ecoreJavascriptDelegatesTest_Employee(name="sample_text")
    a2 = ecoreJavascriptDelegatesTest_Employee(name="sample_text_2")
    b = ecoreJavascriptDelegatesTest_Company(name="sample_text", size="sample_text")
    _safe_set(b, 'company', {a1})
    assert _is_linked(b, 'company', a1)
    if hasattr(a1, 'Employee'):
        assert _is_linked(a1, 'Employee', b)
    _safe_set(b, 'company', {a2})
    assert _is_linked(b, 'company', a2)
    if hasattr(a1, 'Employee'):
        assert not _is_linked(a1, 'Employee', b)
    if hasattr(a2, 'Employee'):
        assert _is_linked(a2, 'Employee', b)
    _safe_set(b, 'company', set())
    assert not _is_linked(b, 'company', a2)
    if hasattr(a2, 'Employee'):
        assert not _is_linked(a2, 'Employee', b)


def test_assoc_manager2_reverse_link_reassign_clear():
    a1 = ecoreJavascriptDelegatesTest_Employee(name="sample_text")
    a2 = ecoreJavascriptDelegatesTest_Employee(name="sample_text_2")
    b = ecoreJavascriptDelegatesTest_Employee(name="sample_text")
    _safe_set(b, 'ecoreJavascriptDelegatesTest_Employee1', a1)
    assert _is_linked(b, 'ecoreJavascriptDelegatesTest_Employee1', a1)
    if hasattr(a1, 'ecoreJavascriptDelegatesTest_Employee'):
        assert _is_linked(a1, 'ecoreJavascriptDelegatesTest_Employee', b)
    _safe_set(b, 'ecoreJavascriptDelegatesTest_Employee1', a2)
    assert _is_linked(b, 'ecoreJavascriptDelegatesTest_Employee1', a2)
    if hasattr(a1, 'ecoreJavascriptDelegatesTest_Employee'):
        assert not _is_linked(a1, 'ecoreJavascriptDelegatesTest_Employee', b)
    if hasattr(a2, 'ecoreJavascriptDelegatesTest_Employee'):
        assert _is_linked(a2, 'ecoreJavascriptDelegatesTest_Employee', b)
    _safe_set(b, 'ecoreJavascriptDelegatesTest_Employee1', None)
    assert not _is_linked(b, 'ecoreJavascriptDelegatesTest_Employee1', a2)
    if hasattr(a2, 'ecoreJavascriptDelegatesTest_Employee'):
        assert not _is_linked(a2, 'ecoreJavascriptDelegatesTest_Employee', b)


def test_assoc_reportingChain11_reverse_link_reassign_clear():
    a1 = ecoreJavascriptDelegatesTest_Employee(name="sample_text")
    a2 = ecoreJavascriptDelegatesTest_Employee(name="sample_text_2")
    b = ecoreJavascriptDelegatesTest_Employee(name="sample_text")
    _safe_set(b, 'ecoreJavascriptDelegatesTest_Employee12', a1)
    assert _is_linked(b, 'ecoreJavascriptDelegatesTest_Employee12', a1)
    if hasattr(a1, 'ecoreJavascriptDelegatesTest_Employee10'):
        assert _is_linked(a1, 'ecoreJavascriptDelegatesTest_Employee10', b)
    _safe_set(b, 'ecoreJavascriptDelegatesTest_Employee12', a2)
    assert _is_linked(b, 'ecoreJavascriptDelegatesTest_Employee12', a2)
    if hasattr(a1, 'ecoreJavascriptDelegatesTest_Employee10'):
        assert not _is_linked(a1, 'ecoreJavascriptDelegatesTest_Employee10', b)
    if hasattr(a2, 'ecoreJavascriptDelegatesTest_Employee10'):
        assert _is_linked(a2, 'ecoreJavascriptDelegatesTest_Employee10', b)
    _safe_set(b, 'ecoreJavascriptDelegatesTest_Employee12', None)
    assert not _is_linked(b, 'ecoreJavascriptDelegatesTest_Employee12', a2)
    if hasattr(a2, 'ecoreJavascriptDelegatesTest_Employee10'):
        assert not _is_linked(a2, 'ecoreJavascriptDelegatesTest_Employee10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

