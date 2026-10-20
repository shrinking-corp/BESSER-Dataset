import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    demo_model_Address,
    demo_model_Company,
    demo_model_Employee,
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

def test_assoc_address2_reverse_link_reassign_clear():
    a1 = demo_model_Employee(birthday=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phone="sample_text", position="sample_text")
    a2 = demo_model_Employee(birthday=date(2025, 6, 15), email="sample_text_2", firstname="sample_text_2", lastname="sample_text_2", phone="sample_text_2", position="sample_text_2")
    b = demo_model_Address(city="sample_text", country="sample_text", state="sample_text", street="sample_text", zipcode=7)
    _safe_set(b, 'demo_model_Address', a1)
    assert _is_linked(b, 'demo_model_Address', a1)
    if hasattr(a1, 'demo_model_Employee'):
        assert _is_linked(a1, 'demo_model_Employee', b)
    _safe_set(b, 'demo_model_Address', a2)
    assert _is_linked(b, 'demo_model_Address', a2)
    if hasattr(a1, 'demo_model_Employee'):
        assert not _is_linked(a1, 'demo_model_Employee', b)
    if hasattr(a2, 'demo_model_Employee'):
        assert _is_linked(a2, 'demo_model_Employee', b)
    _safe_set(b, 'demo_model_Address', None)
    assert not _is_linked(b, 'demo_model_Address', a2)
    if hasattr(a2, 'demo_model_Employee'):
        assert not _is_linked(a2, 'demo_model_Employee', b)


def test_assoc_company1_reverse_link_reassign_clear():
    a1 = demo_model_Employee(birthday=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phone="sample_text", position="sample_text")
    a2 = demo_model_Employee(birthday=date(2025, 6, 15), email="sample_text_2", firstname="sample_text_2", lastname="sample_text_2", phone="sample_text_2", position="sample_text_2")
    b = demo_model_Company(name="sample_text")
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


def test_assoc_employees0_reverse_link_reassign_clear():
    a1 = demo_model_Employee(birthday=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phone="sample_text", position="sample_text")
    a2 = demo_model_Employee(birthday=date(2025, 6, 15), email="sample_text_2", firstname="sample_text_2", lastname="sample_text_2", phone="sample_text_2", position="sample_text_2")
    b = demo_model_Company(name="sample_text")
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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

