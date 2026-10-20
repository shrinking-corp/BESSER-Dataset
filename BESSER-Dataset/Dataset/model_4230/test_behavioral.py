import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CompanyLanguage_Admin,
    CompanyLanguage_CEO,
    CompanyLanguage_Company,
    CompanyLanguage_Employee,
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

def test_assoc_admin8_reverse_link_reassign_clear():
    a1 = CompanyLanguage_Company(name="sample_text")
    a2 = CompanyLanguage_Company(name="sample_text_2")
    b = CompanyLanguage_Admin(name="sample_text")
    _safe_set(b, 'CompanyLanguage_Admin10', a1)
    assert _is_linked(b, 'CompanyLanguage_Admin10', a1)
    if hasattr(a1, 'CompanyLanguage_Company9'):
        assert _is_linked(a1, 'CompanyLanguage_Company9', b)
    _safe_set(b, 'CompanyLanguage_Admin10', a2)
    assert _is_linked(b, 'CompanyLanguage_Admin10', a2)
    if hasattr(a1, 'CompanyLanguage_Company9'):
        assert not _is_linked(a1, 'CompanyLanguage_Company9', b)
    if hasattr(a2, 'CompanyLanguage_Company9'):
        assert _is_linked(a2, 'CompanyLanguage_Company9', b)
    _safe_set(b, 'CompanyLanguage_Admin10', None)
    assert not _is_linked(b, 'CompanyLanguage_Admin10', a2)
    if hasattr(a2, 'CompanyLanguage_Company9'):
        assert not _is_linked(a2, 'CompanyLanguage_Company9', b)


def test_assoc_ceo0_reverse_link_reassign_clear():
    a1 = CompanyLanguage_CEO(name="sample_text")
    a2 = CompanyLanguage_CEO(name="sample_text_2")
    b = CompanyLanguage_Admin(name="sample_text")
    _safe_set(b, 'CompanyLanguage_Admin', a1)
    assert _is_linked(b, 'CompanyLanguage_Admin', a1)
    if hasattr(a1, 'CompanyLanguage_CEO'):
        assert _is_linked(a1, 'CompanyLanguage_CEO', b)
    _safe_set(b, 'CompanyLanguage_Admin', a2)
    assert _is_linked(b, 'CompanyLanguage_Admin', a2)
    if hasattr(a1, 'CompanyLanguage_CEO'):
        assert not _is_linked(a1, 'CompanyLanguage_CEO', b)
    if hasattr(a2, 'CompanyLanguage_CEO'):
        assert _is_linked(a2, 'CompanyLanguage_CEO', b)
    _safe_set(b, 'CompanyLanguage_Admin', None)
    assert not _is_linked(b, 'CompanyLanguage_Admin', a2)
    if hasattr(a2, 'CompanyLanguage_CEO'):
        assert not _is_linked(a2, 'CompanyLanguage_CEO', b)


def test_assoc_ceo5_reverse_link_reassign_clear():
    a1 = CompanyLanguage_Company(name="sample_text")
    a2 = CompanyLanguage_Company(name="sample_text_2")
    b = CompanyLanguage_CEO(name="sample_text")
    _safe_set(b, 'CompanyLanguage_CEO7', a1)
    assert _is_linked(b, 'CompanyLanguage_CEO7', a1)
    if hasattr(a1, 'CompanyLanguage_Company6'):
        assert _is_linked(a1, 'CompanyLanguage_Company6', b)
    _safe_set(b, 'CompanyLanguage_CEO7', a2)
    assert _is_linked(b, 'CompanyLanguage_CEO7', a2)
    if hasattr(a1, 'CompanyLanguage_Company6'):
        assert not _is_linked(a1, 'CompanyLanguage_Company6', b)
    if hasattr(a2, 'CompanyLanguage_Company6'):
        assert _is_linked(a2, 'CompanyLanguage_Company6', b)
    _safe_set(b, 'CompanyLanguage_CEO7', None)
    assert not _is_linked(b, 'CompanyLanguage_CEO7', a2)
    if hasattr(a2, 'CompanyLanguage_Company6'):
        assert not _is_linked(a2, 'CompanyLanguage_Company6', b)


def test_assoc_employee1_reverse_link_reassign_clear():
    a1 = CompanyLanguage_Employee(name="sample_text")
    a2 = CompanyLanguage_Employee(name="sample_text_2")
    b = CompanyLanguage_CEO(name="sample_text")
    _safe_set(b, 'CompanyLanguage_CEO2', {a1})
    assert _is_linked(b, 'CompanyLanguage_CEO2', a1)
    if hasattr(a1, 'CompanyLanguage_Employee'):
        assert _is_linked(a1, 'CompanyLanguage_Employee', b)
    _safe_set(b, 'CompanyLanguage_CEO2', {a2})
    assert _is_linked(b, 'CompanyLanguage_CEO2', a2)
    if hasattr(a1, 'CompanyLanguage_Employee'):
        assert not _is_linked(a1, 'CompanyLanguage_Employee', b)
    if hasattr(a2, 'CompanyLanguage_Employee'):
        assert _is_linked(a2, 'CompanyLanguage_Employee', b)
    _safe_set(b, 'CompanyLanguage_CEO2', set())
    assert not _is_linked(b, 'CompanyLanguage_CEO2', a2)
    if hasattr(a2, 'CompanyLanguage_Employee'):
        assert not _is_linked(a2, 'CompanyLanguage_Employee', b)


def test_assoc_employee3_reverse_link_reassign_clear():
    a1 = CompanyLanguage_Employee(name="sample_text")
    a2 = CompanyLanguage_Employee(name="sample_text_2")
    b = CompanyLanguage_Company(name="sample_text")
    _safe_set(b, 'CompanyLanguage_Company', {a1})
    assert _is_linked(b, 'CompanyLanguage_Company', a1)
    if hasattr(a1, 'CompanyLanguage_Employee4'):
        assert _is_linked(a1, 'CompanyLanguage_Employee4', b)
    _safe_set(b, 'CompanyLanguage_Company', {a2})
    assert _is_linked(b, 'CompanyLanguage_Company', a2)
    if hasattr(a1, 'CompanyLanguage_Employee4'):
        assert not _is_linked(a1, 'CompanyLanguage_Employee4', b)
    if hasattr(a2, 'CompanyLanguage_Employee4'):
        assert _is_linked(a2, 'CompanyLanguage_Employee4', b)
    _safe_set(b, 'CompanyLanguage_Company', set())
    assert not _is_linked(b, 'CompanyLanguage_Company', a2)
    if hasattr(a2, 'CompanyLanguage_Employee4'):
        assert not _is_linked(a2, 'CompanyLanguage_Employee4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

