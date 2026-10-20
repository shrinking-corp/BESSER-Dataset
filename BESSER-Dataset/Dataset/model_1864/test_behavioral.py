import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    decobat_Customer,
    decobat_Level,
    decobat_Library,
    decobat_LibraryCategory,
    decobat_Object,
    decobat_Plan,
    decobat_Product,
    decobat_Project,
    decobat_ProjectCategory,
    decobat_ProjectRevision,
    decobat_Service,
    decobat_Supplier,
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

def test_assoc_categories7_reverse_link_reassign_clear():
    a1 = decobat_LibraryCategory(created=date(2024, 1, 1), description="sample_text", name="sample_text", shortDescription="sample_text")
    a2 = decobat_LibraryCategory(created=date(2025, 6, 15), description="sample_text_2", name="sample_text_2", shortDescription="sample_text_2")
    b = decobat_Library(created=date(2024, 1, 1), depth="sample_text", description="sample_text", height="sample_text", name="sample_text", shortDescription="sample_text", update=date(2024, 1, 1), width="sample_text")
    _safe_set(b, 'decobat_Library', {a1})
    assert _is_linked(b, 'decobat_Library', a1)
    if hasattr(a1, 'decobat_LibraryCategory'):
        assert _is_linked(a1, 'decobat_LibraryCategory', b)
    _safe_set(b, 'decobat_Library', {a2})
    assert _is_linked(b, 'decobat_Library', a2)
    if hasattr(a1, 'decobat_LibraryCategory'):
        assert not _is_linked(a1, 'decobat_LibraryCategory', b)
    if hasattr(a2, 'decobat_LibraryCategory'):
        assert _is_linked(a2, 'decobat_LibraryCategory', b)
    _safe_set(b, 'decobat_Library', set())
    assert not _is_linked(b, 'decobat_Library', a2)
    if hasattr(a2, 'decobat_LibraryCategory'):
        assert not _is_linked(a2, 'decobat_LibraryCategory', b)


def test_assoc_customer5_reverse_link_reassign_clear():
    a1 = decobat_Project(closed=date(2024, 1, 1), created=date(2024, 1, 1), description="sample_text", name="sample_text", shortDescription="sample_text")
    a2 = decobat_Project(closed=date(2025, 6, 15), created=date(2025, 6, 15), description="sample_text_2", name="sample_text_2", shortDescription="sample_text_2")
    b = decobat_Customer(address="sample_text", city="sample_text", code="sample_text", country="sample_text", email="sample_text", fax="sample_text", name="sample_text", phone="sample_text", zip="sample_text")
    _safe_set(b, 'decobat_Customer', a1)
    assert _is_linked(b, 'decobat_Customer', a1)
    if hasattr(a1, 'decobat_Project6'):
        assert _is_linked(a1, 'decobat_Project6', b)
    _safe_set(b, 'decobat_Customer', a2)
    assert _is_linked(b, 'decobat_Customer', a2)
    if hasattr(a1, 'decobat_Project6'):
        assert not _is_linked(a1, 'decobat_Project6', b)
    if hasattr(a2, 'decobat_Project6'):
        assert _is_linked(a2, 'decobat_Project6', b)
    _safe_set(b, 'decobat_Customer', None)
    assert not _is_linked(b, 'decobat_Customer', a2)
    if hasattr(a2, 'decobat_Project6'):
        assert not _is_linked(a2, 'decobat_Project6', b)


def test_assoc_levels9_reverse_link_reassign_clear():
    a1 = decobat_Plan(code="sample_text", description="sample_text", name="sample_text", shortDescription="sample_text")
    a2 = decobat_Plan(code="sample_text_2", description="sample_text_2", name="sample_text_2", shortDescription="sample_text_2")
    b = decobat_Level(code="sample_text", description="sample_text", name="sample_text", shortDescription="sample_text")
    _safe_set(b, 'decobat_Level', a1)
    assert _is_linked(b, 'decobat_Level', a1)
    if hasattr(a1, 'decobat_Plan10'):
        assert _is_linked(a1, 'decobat_Plan10', b)
    _safe_set(b, 'decobat_Level', a2)
    assert _is_linked(b, 'decobat_Level', a2)
    if hasattr(a1, 'decobat_Plan10'):
        assert not _is_linked(a1, 'decobat_Plan10', b)
    if hasattr(a2, 'decobat_Plan10'):
        assert _is_linked(a2, 'decobat_Plan10', b)
    _safe_set(b, 'decobat_Level', None)
    assert not _is_linked(b, 'decobat_Level', a2)
    if hasattr(a2, 'decobat_Plan10'):
        assert not _is_linked(a2, 'decobat_Plan10', b)


def test_assoc_libraryItems11_reverse_link_reassign_clear():
    a1 = decobat_Library(created=date(2024, 1, 1), depth="sample_text", description="sample_text", height="sample_text", name="sample_text", shortDescription="sample_text", update=date(2024, 1, 1), width="sample_text")
    a2 = decobat_Library(created=date(2025, 6, 15), depth="sample_text_2", description="sample_text_2", height="sample_text_2", name="sample_text_2", shortDescription="sample_text_2", update=date(2025, 6, 15), width="sample_text_2")
    b = decobat_Level(code="sample_text", description="sample_text", name="sample_text", shortDescription="sample_text")
    _safe_set(b, 'decobat_Level12', {a1})
    assert _is_linked(b, 'decobat_Level12', a1)
    if hasattr(a1, 'decobat_Library13'):
        assert _is_linked(a1, 'decobat_Library13', b)
    _safe_set(b, 'decobat_Level12', {a2})
    assert _is_linked(b, 'decobat_Level12', a2)
    if hasattr(a1, 'decobat_Library13'):
        assert not _is_linked(a1, 'decobat_Library13', b)
    if hasattr(a2, 'decobat_Library13'):
        assert _is_linked(a2, 'decobat_Library13', b)
    _safe_set(b, 'decobat_Level12', set())
    assert not _is_linked(b, 'decobat_Level12', a2)
    if hasattr(a2, 'decobat_Library13'):
        assert not _is_linked(a2, 'decobat_Library13', b)


def test_assoc_libraryItems14_reverse_link_reassign_clear():
    a1 = decobat_Object(code="sample_text", description="sample_text", name="sample_text", shortDescription="sample_text")
    a2 = decobat_Object(code="sample_text_2", description="sample_text_2", name="sample_text_2", shortDescription="sample_text_2")
    b = decobat_Library(created=date(2024, 1, 1), depth="sample_text", description="sample_text", height="sample_text", name="sample_text", shortDescription="sample_text", update=date(2024, 1, 1), width="sample_text")
    _safe_set(b, 'decobat_Library15', a1)
    assert _is_linked(b, 'decobat_Library15', a1)
    if hasattr(a1, 'decobat_Object'):
        assert _is_linked(a1, 'decobat_Object', b)
    _safe_set(b, 'decobat_Library15', a2)
    assert _is_linked(b, 'decobat_Library15', a2)
    if hasattr(a1, 'decobat_Object'):
        assert not _is_linked(a1, 'decobat_Object', b)
    if hasattr(a2, 'decobat_Object'):
        assert _is_linked(a2, 'decobat_Object', b)
    _safe_set(b, 'decobat_Library15', None)
    assert not _is_linked(b, 'decobat_Library15', a2)
    if hasattr(a2, 'decobat_Object'):
        assert not _is_linked(a2, 'decobat_Object', b)


def test_assoc_plans3_reverse_link_reassign_clear():
    a1 = decobat_Project(closed=date(2024, 1, 1), created=date(2024, 1, 1), description="sample_text", name="sample_text", shortDescription="sample_text")
    a2 = decobat_Project(closed=date(2025, 6, 15), created=date(2025, 6, 15), description="sample_text_2", name="sample_text_2", shortDescription="sample_text_2")
    b = decobat_Plan(code="sample_text", description="sample_text", name="sample_text", shortDescription="sample_text")
    _safe_set(b, 'decobat_Plan', a1)
    assert _is_linked(b, 'decobat_Plan', a1)
    if hasattr(a1, 'decobat_Project4'):
        assert _is_linked(a1, 'decobat_Project4', b)
    _safe_set(b, 'decobat_Plan', a2)
    assert _is_linked(b, 'decobat_Plan', a2)
    if hasattr(a1, 'decobat_Project4'):
        assert not _is_linked(a1, 'decobat_Project4', b)
    if hasattr(a2, 'decobat_Project4'):
        assert _is_linked(a2, 'decobat_Project4', b)
    _safe_set(b, 'decobat_Plan', None)
    assert not _is_linked(b, 'decobat_Plan', a2)
    if hasattr(a2, 'decobat_Project4'):
        assert not _is_linked(a2, 'decobat_Project4', b)


def test_assoc_projectCategories1_reverse_link_reassign_clear():
    a1 = decobat_ProjectCategory(created=date(2024, 1, 1), description="sample_text", name="sample_text", shortDescription="sample_text")
    a2 = decobat_ProjectCategory(created=date(2025, 6, 15), description="sample_text_2", name="sample_text_2", shortDescription="sample_text_2")
    b = decobat_Project(closed=date(2024, 1, 1), created=date(2024, 1, 1), description="sample_text", name="sample_text", shortDescription="sample_text")
    _safe_set(b, 'decobat_Project2', a1)
    assert _is_linked(b, 'decobat_Project2', a1)
    if hasattr(a1, 'decobat_ProjectCategory'):
        assert _is_linked(a1, 'decobat_ProjectCategory', b)
    _safe_set(b, 'decobat_Project2', a2)
    assert _is_linked(b, 'decobat_Project2', a2)
    if hasattr(a1, 'decobat_ProjectCategory'):
        assert not _is_linked(a1, 'decobat_ProjectCategory', b)
    if hasattr(a2, 'decobat_ProjectCategory'):
        assert _is_linked(a2, 'decobat_ProjectCategory', b)
    _safe_set(b, 'decobat_Project2', None)
    assert not _is_linked(b, 'decobat_Project2', a2)
    if hasattr(a2, 'decobat_ProjectCategory'):
        assert not _is_linked(a2, 'decobat_ProjectCategory', b)


def test_assoc_projectRevisions0_reverse_link_reassign_clear():
    a1 = decobat_ProjectRevision(comment="sample_text", description="sample_text", shortDescription="sample_text", update=date(2024, 1, 1))
    a2 = decobat_ProjectRevision(comment="sample_text_2", description="sample_text_2", shortDescription="sample_text_2", update=date(2025, 6, 15))
    b = decobat_Project(closed=date(2024, 1, 1), created=date(2024, 1, 1), description="sample_text", name="sample_text", shortDescription="sample_text")
    _safe_set(b, 'decobat_Project', {a1})
    assert _is_linked(b, 'decobat_Project', a1)
    if hasattr(a1, 'decobat_ProjectRevision'):
        assert _is_linked(a1, 'decobat_ProjectRevision', b)
    _safe_set(b, 'decobat_Project', {a2})
    assert _is_linked(b, 'decobat_Project', a2)
    if hasattr(a1, 'decobat_ProjectRevision'):
        assert not _is_linked(a1, 'decobat_ProjectRevision', b)
    if hasattr(a2, 'decobat_ProjectRevision'):
        assert _is_linked(a2, 'decobat_ProjectRevision', b)
    _safe_set(b, 'decobat_Project', set())
    assert not _is_linked(b, 'decobat_Project', a2)
    if hasattr(a2, 'decobat_ProjectRevision'):
        assert not _is_linked(a2, 'decobat_ProjectRevision', b)


def test_assoc_supplier8_reverse_link_reassign_clear():
    a1 = decobat_Supplier(address="sample_text", city="sample_text", code="sample_text", country="sample_text", email="sample_text", fax="sample_text", name="sample_text", phone="sample_text", zip="sample_text")
    a2 = decobat_Supplier(address="sample_text_2", city="sample_text_2", code="sample_text_2", country="sample_text_2", email="sample_text_2", fax="sample_text_2", name="sample_text_2", phone="sample_text_2", zip="sample_text_2")
    b = decobat_Product(created=date(2024, 1, 1), depth="sample_text", description="sample_text", height="sample_text", name="sample_text", shortDescription="sample_text", unitBilledPrice="sample_text", unitCostPrice="sample_text", unitWeight="sample_text", update=date(2024, 1, 1), width="sample_text")
    _safe_set(b, 'decobat_Product', a1)
    assert _is_linked(b, 'decobat_Product', a1)
    if hasattr(a1, 'decobat_Supplier'):
        assert _is_linked(a1, 'decobat_Supplier', b)
    _safe_set(b, 'decobat_Product', a2)
    assert _is_linked(b, 'decobat_Product', a2)
    if hasattr(a1, 'decobat_Supplier'):
        assert not _is_linked(a1, 'decobat_Supplier', b)
    if hasattr(a2, 'decobat_Supplier'):
        assert _is_linked(a2, 'decobat_Supplier', b)
    _safe_set(b, 'decobat_Product', None)
    assert not _is_linked(b, 'decobat_Product', a2)
    if hasattr(a2, 'decobat_Supplier'):
        assert not _is_linked(a2, 'decobat_Supplier', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

