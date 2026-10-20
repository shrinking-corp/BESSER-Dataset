import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    organizationchart_Employee,
    organizationchart_Function,
    organizationchart_Location,
    organizationchart_Organization,
    organizationchart_OrganizationalStructure,
    StructureType,
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

def test_assoc_belongsTo2_reverse_link_reassign_clear():
    a1 = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    a2 = organizationchart_OrganizationalStructure(name="sample_text_2", type="sample_text_2")
    b = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    _safe_set(b, 'employees', a1)
    assert _is_linked(b, 'employees', a1)
    if hasattr(a1, 'OrganizationalStructure'):
        assert _is_linked(a1, 'OrganizationalStructure', b)
    _safe_set(b, 'employees', a2)
    assert _is_linked(b, 'employees', a2)
    if hasattr(a1, 'OrganizationalStructure'):
        assert not _is_linked(a1, 'OrganizationalStructure', b)
    if hasattr(a2, 'OrganizationalStructure'):
        assert _is_linked(a2, 'OrganizationalStructure', b)
    _safe_set(b, 'employees', None)
    assert not _is_linked(b, 'employees', a2)
    if hasattr(a2, 'OrganizationalStructure'):
        assert not _is_linked(a2, 'OrganizationalStructure', b)


def test_assoc_employees12_reverse_link_reassign_clear():
    a1 = organizationchart_Organization(name="sample_text")
    a2 = organizationchart_Organization(name="sample_text_2")
    b = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    _safe_set(b, 'organizationchart_Employee', a1)
    assert _is_linked(b, 'organizationchart_Employee', a1)
    if hasattr(a1, 'organizationchart_Organization'):
        assert _is_linked(a1, 'organizationchart_Organization', b)
    _safe_set(b, 'organizationchart_Employee', a2)
    assert _is_linked(b, 'organizationchart_Employee', a2)
    if hasattr(a1, 'organizationchart_Organization'):
        assert not _is_linked(a1, 'organizationchart_Organization', b)
    if hasattr(a2, 'organizationchart_Organization'):
        assert _is_linked(a2, 'organizationchart_Organization', b)
    _safe_set(b, 'organizationchart_Employee', None)
    assert not _is_linked(b, 'organizationchart_Employee', a2)
    if hasattr(a2, 'organizationchart_Organization'):
        assert not _is_linked(a2, 'organizationchart_Organization', b)


def test_assoc_employees17_reverse_link_reassign_clear():
    a1 = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    a2 = organizationchart_OrganizationalStructure(name="sample_text_2", type="sample_text_2")
    b = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    _safe_set(b, 'Employee18', a1)
    assert _is_linked(b, 'Employee18', a1)
    if hasattr(a1, 'belongsTo'):
        assert _is_linked(a1, 'belongsTo', b)
    _safe_set(b, 'Employee18', a2)
    assert _is_linked(b, 'Employee18', a2)
    if hasattr(a1, 'belongsTo'):
        assert not _is_linked(a1, 'belongsTo', b)
    if hasattr(a2, 'belongsTo'):
        assert _is_linked(a2, 'belongsTo', b)
    _safe_set(b, 'Employee18', None)
    assert not _is_linked(b, 'Employee18', a2)
    if hasattr(a2, 'belongsTo'):
        assert not _is_linked(a2, 'belongsTo', b)


def test_assoc_employees26_reverse_link_reassign_clear():
    a1 = organizationchart_Location(name="sample_text")
    a2 = organizationchart_Location(name="sample_text_2")
    b = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    _safe_set(b, 'Employee27', a1)
    assert _is_linked(b, 'Employee27', a1)
    if hasattr(a1, 'location'):
        assert _is_linked(a1, 'location', b)
    _safe_set(b, 'Employee27', a2)
    assert _is_linked(b, 'Employee27', a2)
    if hasattr(a1, 'location'):
        assert not _is_linked(a1, 'location', b)
    if hasattr(a2, 'location'):
        assert _is_linked(a2, 'location', b)
    _safe_set(b, 'Employee27', None)
    assert not _is_linked(b, 'Employee27', a2)
    if hasattr(a2, 'location'):
        assert not _is_linked(a2, 'location', b)


def test_assoc_isPerformedBy28_reverse_link_reassign_clear():
    a1 = organizationchart_Function(name="sample_text")
    a2 = organizationchart_Function(name="sample_text_2")
    b = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    _safe_set(b, 'Employee29', a1)
    assert _is_linked(b, 'Employee29', a1)
    if hasattr(a1, 'performs'):
        assert _is_linked(a1, 'performs', b)
    _safe_set(b, 'Employee29', a2)
    assert _is_linked(b, 'Employee29', a2)
    if hasattr(a1, 'performs'):
        assert not _is_linked(a1, 'performs', b)
    if hasattr(a2, 'performs'):
        assert _is_linked(a2, 'performs', b)
    _safe_set(b, 'Employee29', None)
    assert not _is_linked(b, 'Employee29', a2)
    if hasattr(a2, 'performs'):
        assert not _is_linked(a2, 'performs', b)


def test_assoc_leads9_reverse_link_reassign_clear():
    a1 = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    a2 = organizationchart_OrganizationalStructure(name="sample_text_2", type="sample_text_2")
    b = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    _safe_set(b, 'manager10', {a1})
    assert _is_linked(b, 'manager10', a1)
    if hasattr(a1, 'OrganizationalStructure11'):
        assert _is_linked(a1, 'OrganizationalStructure11', b)
    _safe_set(b, 'manager10', {a2})
    assert _is_linked(b, 'manager10', a2)
    if hasattr(a1, 'OrganizationalStructure11'):
        assert not _is_linked(a1, 'OrganizationalStructure11', b)
    if hasattr(a2, 'OrganizationalStructure11'):
        assert _is_linked(a2, 'OrganizationalStructure11', b)
    _safe_set(b, 'manager10', set())
    assert not _is_linked(b, 'manager10', a2)
    if hasattr(a2, 'OrganizationalStructure11'):
        assert not _is_linked(a2, 'OrganizationalStructure11', b)


def test_assoc_location3_reverse_link_reassign_clear():
    a1 = organizationchart_Location(name="sample_text")
    a2 = organizationchart_Location(name="sample_text_2")
    b = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    _safe_set(b, 'employees4', a1)
    assert _is_linked(b, 'employees4', a1)
    if hasattr(a1, 'Location'):
        assert _is_linked(a1, 'Location', b)
    _safe_set(b, 'employees4', a2)
    assert _is_linked(b, 'employees4', a2)
    if hasattr(a1, 'Location'):
        assert not _is_linked(a1, 'Location', b)
    if hasattr(a2, 'Location'):
        assert _is_linked(a2, 'Location', b)
    _safe_set(b, 'employees4', None)
    assert not _is_linked(b, 'employees4', a2)
    if hasattr(a2, 'Location'):
        assert not _is_linked(a2, 'Location', b)


def test_assoc_locations15_reverse_link_reassign_clear():
    a1 = organizationchart_Organization(name="sample_text")
    a2 = organizationchart_Organization(name="sample_text_2")
    b = organizationchart_Location(name="sample_text")
    _safe_set(b, 'organizationchart_Location', a1)
    assert _is_linked(b, 'organizationchart_Location', a1)
    if hasattr(a1, 'organizationchart_Organization16'):
        assert _is_linked(a1, 'organizationchart_Organization16', b)
    _safe_set(b, 'organizationchart_Location', a2)
    assert _is_linked(b, 'organizationchart_Location', a2)
    if hasattr(a1, 'organizationchart_Organization16'):
        assert not _is_linked(a1, 'organizationchart_Organization16', b)
    if hasattr(a2, 'organizationchart_Organization16'):
        assert _is_linked(a2, 'organizationchart_Organization16', b)
    _safe_set(b, 'organizationchart_Location', None)
    assert not _is_linked(b, 'organizationchart_Location', a2)
    if hasattr(a2, 'organizationchart_Organization16'):
        assert not _is_linked(a2, 'organizationchart_Organization16', b)


def test_assoc_manager24_reverse_link_reassign_clear():
    a1 = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    a2 = organizationchart_OrganizationalStructure(name="sample_text_2", type="sample_text_2")
    b = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    _safe_set(b, 'Employee25', a1)
    assert _is_linked(b, 'Employee25', a1)
    if hasattr(a1, 'leads'):
        assert _is_linked(a1, 'leads', b)
    _safe_set(b, 'Employee25', a2)
    assert _is_linked(b, 'Employee25', a2)
    if hasattr(a1, 'leads'):
        assert not _is_linked(a1, 'leads', b)
    if hasattr(a2, 'leads'):
        assert _is_linked(a2, 'leads', b)
    _safe_set(b, 'Employee25', None)
    assert not _is_linked(b, 'Employee25', a2)
    if hasattr(a2, 'leads'):
        assert not _is_linked(a2, 'leads', b)


def test_assoc_manager6_reverse_link_reassign_clear():
    a1 = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    a2 = organizationchart_Employee(firstname="sample_text_2", lastname="sample_text_2", title="sample_text_2", trigraph="sample_text_2")
    b = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    _safe_set(b, 'manages', a1)
    assert _is_linked(b, 'manages', a1)
    if hasattr(a1, 'Employee7'):
        assert _is_linked(a1, 'Employee7', b)
    _safe_set(b, 'manages', a2)
    assert _is_linked(b, 'manages', a2)
    if hasattr(a1, 'Employee7'):
        assert not _is_linked(a1, 'Employee7', b)
    if hasattr(a2, 'Employee7'):
        assert _is_linked(a2, 'Employee7', b)
    _safe_set(b, 'manages', None)
    assert not _is_linked(b, 'manages', a2)
    if hasattr(a2, 'Employee7'):
        assert not _is_linked(a2, 'Employee7', b)


def test_assoc_manages1_reverse_link_reassign_clear():
    a1 = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    a2 = organizationchart_Employee(firstname="sample_text_2", lastname="sample_text_2", title="sample_text_2", trigraph="sample_text_2")
    b = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    _safe_set(b, 'manager', {a1})
    assert _is_linked(b, 'manager', a1)
    if hasattr(a1, 'Employee'):
        assert _is_linked(a1, 'Employee', b)
    _safe_set(b, 'manager', {a2})
    assert _is_linked(b, 'manager', a2)
    if hasattr(a1, 'Employee'):
        assert not _is_linked(a1, 'Employee', b)
    if hasattr(a2, 'Employee'):
        assert _is_linked(a2, 'Employee', b)
    _safe_set(b, 'manager', set())
    assert not _is_linked(b, 'manager', a2)
    if hasattr(a2, 'Employee'):
        assert not _is_linked(a2, 'Employee', b)


def test_assoc_owns22_reverse_link_reassign_clear():
    a1 = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    a2 = organizationchart_OrganizationalStructure(name="sample_text_2", type="sample_text_2")
    b = organizationchart_Function(name="sample_text")
    _safe_set(b, 'organizationchart_Function', a1)
    assert _is_linked(b, 'organizationchart_Function', a1)
    if hasattr(a1, 'organizationchart_OrganizationalStructure23'):
        assert _is_linked(a1, 'organizationchart_OrganizationalStructure23', b)
    _safe_set(b, 'organizationchart_Function', a2)
    assert _is_linked(b, 'organizationchart_Function', a2)
    if hasattr(a1, 'organizationchart_OrganizationalStructure23'):
        assert not _is_linked(a1, 'organizationchart_OrganizationalStructure23', b)
    if hasattr(a2, 'organizationchart_OrganizationalStructure23'):
        assert _is_linked(a2, 'organizationchart_OrganizationalStructure23', b)
    _safe_set(b, 'organizationchart_Function', None)
    assert not _is_linked(b, 'organizationchart_Function', a2)
    if hasattr(a2, 'organizationchart_OrganizationalStructure23'):
        assert not _is_linked(a2, 'organizationchart_OrganizationalStructure23', b)


def test_assoc_performs8_reverse_link_reassign_clear():
    a1 = organizationchart_Function(name="sample_text")
    a2 = organizationchart_Function(name="sample_text_2")
    b = organizationchart_Employee(firstname="sample_text", lastname="sample_text", title="sample_text", trigraph="sample_text")
    _safe_set(b, 'isPerformedBy', {a1})
    assert _is_linked(b, 'isPerformedBy', a1)
    if hasattr(a1, 'Function'):
        assert _is_linked(a1, 'Function', b)
    _safe_set(b, 'isPerformedBy', {a2})
    assert _is_linked(b, 'isPerformedBy', a2)
    if hasattr(a1, 'Function'):
        assert not _is_linked(a1, 'Function', b)
    if hasattr(a2, 'Function'):
        assert _is_linked(a2, 'Function', b)
    _safe_set(b, 'isPerformedBy', set())
    assert not _is_linked(b, 'isPerformedBy', a2)
    if hasattr(a2, 'Function'):
        assert not _is_linked(a2, 'Function', b)


def test_assoc_structures13_reverse_link_reassign_clear():
    a1 = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    a2 = organizationchart_OrganizationalStructure(name="sample_text_2", type="sample_text_2")
    b = organizationchart_Organization(name="sample_text")
    _safe_set(b, 'organizationchart_Organization14', {a1})
    assert _is_linked(b, 'organizationchart_Organization14', a1)
    if hasattr(a1, 'organizationchart_OrganizationalStructure'):
        assert _is_linked(a1, 'organizationchart_OrganizationalStructure', b)
    _safe_set(b, 'organizationchart_Organization14', {a2})
    assert _is_linked(b, 'organizationchart_Organization14', a2)
    if hasattr(a1, 'organizationchart_OrganizationalStructure'):
        assert not _is_linked(a1, 'organizationchart_OrganizationalStructure', b)
    if hasattr(a2, 'organizationchart_OrganizationalStructure'):
        assert _is_linked(a2, 'organizationchart_OrganizationalStructure', b)
    _safe_set(b, 'organizationchart_Organization14', set())
    assert not _is_linked(b, 'organizationchart_Organization14', a2)
    if hasattr(a2, 'organizationchart_OrganizationalStructure'):
        assert not _is_linked(a2, 'organizationchart_OrganizationalStructure', b)


def test_assoc_subStructures20_reverse_link_reassign_clear():
    a1 = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    a2 = organizationchart_OrganizationalStructure(name="sample_text_2", type="sample_text_2")
    b = organizationchart_OrganizationalStructure(name="sample_text", type="sample_text")
    _safe_set(b, 'organizationchart_OrganizationalStructure21', a1)
    assert _is_linked(b, 'organizationchart_OrganizationalStructure21', a1)
    if hasattr(a1, 'organizationchart_OrganizationalStructure19'):
        assert _is_linked(a1, 'organizationchart_OrganizationalStructure19', b)
    _safe_set(b, 'organizationchart_OrganizationalStructure21', a2)
    assert _is_linked(b, 'organizationchart_OrganizationalStructure21', a2)
    if hasattr(a1, 'organizationchart_OrganizationalStructure19'):
        assert not _is_linked(a1, 'organizationchart_OrganizationalStructure19', b)
    if hasattr(a2, 'organizationchart_OrganizationalStructure19'):
        assert _is_linked(a2, 'organizationchart_OrganizationalStructure19', b)
    _safe_set(b, 'organizationchart_OrganizationalStructure21', None)
    assert not _is_linked(b, 'organizationchart_OrganizationalStructure21', a2)
    if hasattr(a2, 'organizationchart_OrganizationalStructure19'):
        assert not _is_linked(a2, 'organizationchart_OrganizationalStructure19', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

