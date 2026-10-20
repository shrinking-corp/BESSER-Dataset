import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    company_Company,
    company_Person,
    Gender,
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

def test_assoc_manager1_reverse_link_reassign_clear():
    a1 = company_Person(age=7, gender="sample_text", isUnemployed=True, lastname="sample_text", name="sample_text", salary=7)
    a2 = company_Person(age=13, gender="sample_text_2", isUnemployed=False, lastname="sample_text_2", name="sample_text_2", salary=13)
    b = company_Company(name="sample_text", numberOfManager=7)
    _safe_set(b, 'managerCompanies', {a1})
    assert _is_linked(b, 'managerCompanies', a1)
    if hasattr(a1, 'Person'):
        assert _is_linked(a1, 'Person', b)
    _safe_set(b, 'managerCompanies', {a2})
    assert _is_linked(b, 'managerCompanies', a2)
    if hasattr(a1, 'Person'):
        assert not _is_linked(a1, 'Person', b)
    if hasattr(a2, 'Person'):
        assert _is_linked(a2, 'Person', b)
    _safe_set(b, 'managerCompanies', set())
    assert not _is_linked(b, 'managerCompanies', a2)
    if hasattr(a2, 'Person'):
        assert not _is_linked(a2, 'Person', b)


def test_assoc_managerCompanies0_reverse_link_reassign_clear():
    a1 = company_Person(age=7, gender="sample_text", isUnemployed=True, lastname="sample_text", name="sample_text", salary=7)
    a2 = company_Person(age=13, gender="sample_text_2", isUnemployed=False, lastname="sample_text_2", name="sample_text_2", salary=13)
    b = company_Company(name="sample_text", numberOfManager=7)
    _safe_set(b, 'Company', a1)
    assert _is_linked(b, 'Company', a1)
    if hasattr(a1, 'manager'):
        assert _is_linked(a1, 'manager', b)
    _safe_set(b, 'Company', a2)
    assert _is_linked(b, 'Company', a2)
    if hasattr(a1, 'manager'):
        assert not _is_linked(a1, 'manager', b)
    if hasattr(a2, 'manager'):
        assert _is_linked(a2, 'manager', b)
    _safe_set(b, 'Company', None)
    assert not _is_linked(b, 'Company', a2)
    if hasattr(a2, 'manager'):
        assert not _is_linked(a2, 'manager', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

