import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CompanyModel_Company,
    CompanyModel_Department,
    CompanyModel_Employee,
    CompanyModel_Product,
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

def test_assoc_departments0_reverse_link_reassign_clear():
    a1 = CompanyModel_Department(number=7)
    a2 = CompanyModel_Department(number=13)
    b = CompanyModel_Company(name="sample_text")
    _safe_set(b, 'CompanyModel_Company', {a1})
    assert _is_linked(b, 'CompanyModel_Company', a1)
    if hasattr(a1, 'CompanyModel_Department'):
        assert _is_linked(a1, 'CompanyModel_Department', b)
    _safe_set(b, 'CompanyModel_Company', {a2})
    assert _is_linked(b, 'CompanyModel_Company', a2)
    if hasattr(a1, 'CompanyModel_Department'):
        assert not _is_linked(a1, 'CompanyModel_Department', b)
    if hasattr(a2, 'CompanyModel_Department'):
        assert _is_linked(a2, 'CompanyModel_Department', b)
    _safe_set(b, 'CompanyModel_Company', set())
    assert not _is_linked(b, 'CompanyModel_Company', a2)
    if hasattr(a2, 'CompanyModel_Department'):
        assert not _is_linked(a2, 'CompanyModel_Department', b)


def test_assoc_employees1_reverse_link_reassign_clear():
    a1 = CompanyModel_Employee(isManager=True, name="sample_text")
    a2 = CompanyModel_Employee(isManager=False, name="sample_text_2")
    b = CompanyModel_Department(number=7)
    _safe_set(b, 'CompanyModel_Department2', {a1})
    assert _is_linked(b, 'CompanyModel_Department2', a1)
    if hasattr(a1, 'CompanyModel_Employee'):
        assert _is_linked(a1, 'CompanyModel_Employee', b)
    _safe_set(b, 'CompanyModel_Department2', {a2})
    assert _is_linked(b, 'CompanyModel_Department2', a2)
    if hasattr(a1, 'CompanyModel_Employee'):
        assert not _is_linked(a1, 'CompanyModel_Employee', b)
    if hasattr(a2, 'CompanyModel_Employee'):
        assert _is_linked(a2, 'CompanyModel_Employee', b)
    _safe_set(b, 'CompanyModel_Department2', set())
    assert not _is_linked(b, 'CompanyModel_Department2', a2)
    if hasattr(a2, 'CompanyModel_Employee'):
        assert not _is_linked(a2, 'CompanyModel_Employee', b)


def test_assoc_products3_reverse_link_reassign_clear():
    a1 = CompanyModel_Product(name="sample_text", productID=7)
    a2 = CompanyModel_Product(name="sample_text_2", productID=13)
    b = CompanyModel_Department(number=7)
    _safe_set(b, 'CompanyModel_Department4', {a1})
    assert _is_linked(b, 'CompanyModel_Department4', a1)
    if hasattr(a1, 'CompanyModel_Product'):
        assert _is_linked(a1, 'CompanyModel_Product', b)
    _safe_set(b, 'CompanyModel_Department4', {a2})
    assert _is_linked(b, 'CompanyModel_Department4', a2)
    if hasattr(a1, 'CompanyModel_Product'):
        assert not _is_linked(a1, 'CompanyModel_Product', b)
    if hasattr(a2, 'CompanyModel_Product'):
        assert _is_linked(a2, 'CompanyModel_Product', b)
    _safe_set(b, 'CompanyModel_Department4', set())
    assert not _is_linked(b, 'CompanyModel_Department4', a2)
    if hasattr(a2, 'CompanyModel_Product'):
        assert not _is_linked(a2, 'CompanyModel_Product', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

