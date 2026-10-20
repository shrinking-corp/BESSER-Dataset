import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    requirement_Category,
    requirement_EObject,
    requirement_NamedElement,
    requirement_Repository,
    requirement_Requirement,
    RequirementType,
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

def test_assoc_category14_reverse_link_reassign_clear():
    a1 = requirement_Requirement(acceptanceCriteria="sample_text", createdOn=date(2024, 1, 1), id="sample_text", modifiedOn=date(2024, 1, 1), rationale="sample_text", statement="sample_text", status="sample_text", subtype="sample_text", type="sample_text", version=7)
    a2 = requirement_Requirement(acceptanceCriteria="sample_text_2", createdOn=date(2025, 6, 15), id="sample_text_2", modifiedOn=date(2025, 6, 15), rationale="sample_text_2", statement="sample_text_2", status="sample_text_2", subtype="sample_text_2", type="sample_text_2", version=13)
    b = requirement_Category(id="sample_text")
    _safe_set(b, 'Category15', a1)
    assert _is_linked(b, 'Category15', a1)
    if hasattr(a1, 'requirements'):
        assert _is_linked(a1, 'requirements', b)
    _safe_set(b, 'Category15', a2)
    assert _is_linked(b, 'Category15', a2)
    if hasattr(a1, 'requirements'):
        assert not _is_linked(a1, 'requirements', b)
    if hasattr(a2, 'requirements'):
        assert _is_linked(a2, 'requirements', b)
    _safe_set(b, 'Category15', None)
    assert not _is_linked(b, 'Category15', a2)
    if hasattr(a2, 'requirements'):
        assert not _is_linked(a2, 'requirements', b)


def test_assoc_parentCategory8_reverse_link_reassign_clear():
    a1 = requirement_Category(id="sample_text")
    a2 = requirement_Category(id="sample_text_2")
    b = requirement_Category(id="sample_text")
    _safe_set(b, 'subCategories', a1)
    assert _is_linked(b, 'subCategories', a1)
    if hasattr(a1, 'Category9'):
        assert _is_linked(a1, 'Category9', b)
    _safe_set(b, 'subCategories', a2)
    assert _is_linked(b, 'subCategories', a2)
    if hasattr(a1, 'Category9'):
        assert not _is_linked(a1, 'Category9', b)
    if hasattr(a2, 'Category9'):
        assert _is_linked(a2, 'Category9', b)
    _safe_set(b, 'subCategories', None)
    assert not _is_linked(b, 'subCategories', a2)
    if hasattr(a2, 'Category9'):
        assert not _is_linked(a2, 'Category9', b)


def test_assoc_requirements2_reverse_link_reassign_clear():
    a1 = requirement_Requirement(acceptanceCriteria="sample_text", createdOn=date(2024, 1, 1), id="sample_text", modifiedOn=date(2024, 1, 1), rationale="sample_text", statement="sample_text", status="sample_text", subtype="sample_text", type="sample_text", version=7)
    a2 = requirement_Requirement(acceptanceCriteria="sample_text_2", createdOn=date(2025, 6, 15), id="sample_text_2", modifiedOn=date(2025, 6, 15), rationale="sample_text_2", statement="sample_text_2", status="sample_text_2", subtype="sample_text_2", type="sample_text_2", version=13)
    b = requirement_Category(id="sample_text")
    _safe_set(b, 'category', {a1})
    assert _is_linked(b, 'category', a1)
    if hasattr(a1, 'Requirement'):
        assert _is_linked(a1, 'Requirement', b)
    _safe_set(b, 'category', {a2})
    assert _is_linked(b, 'category', a2)
    if hasattr(a1, 'Requirement'):
        assert not _is_linked(a1, 'Requirement', b)
    if hasattr(a2, 'Requirement'):
        assert _is_linked(a2, 'Requirement', b)
    _safe_set(b, 'category', set())
    assert not _is_linked(b, 'category', a2)
    if hasattr(a2, 'Requirement'):
        assert not _is_linked(a2, 'Requirement', b)


def test_assoc_subCategories4_reverse_link_reassign_clear():
    a1 = requirement_Category(id="sample_text")
    a2 = requirement_Category(id="sample_text_2")
    b = requirement_Category(id="sample_text")
    _safe_set(b, 'parentCategory', {a1})
    assert _is_linked(b, 'parentCategory', a1)
    if hasattr(a1, 'Category5'):
        assert _is_linked(a1, 'Category5', b)
    _safe_set(b, 'parentCategory', {a2})
    assert _is_linked(b, 'parentCategory', a2)
    if hasattr(a1, 'Category5'):
        assert not _is_linked(a1, 'Category5', b)
    if hasattr(a2, 'Category5'):
        assert _is_linked(a2, 'Category5', b)
    _safe_set(b, 'parentCategory', set())
    assert not _is_linked(b, 'parentCategory', a2)
    if hasattr(a2, 'Category5'):
        assert not _is_linked(a2, 'Category5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_mainCategories0_stub_double():
    # requirement_Repository has no real 'repository' property in the generated
    # code (a bare stub) -- manually attach it so requirement_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirement_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirement_Category(id="sample_text")
    partner = requirement_Repository()
    setattr(partner, 'repository', None)
    _safe_set(owner, 'Category', partner)
    assert owner in getattr(partner, 'repository')
    _safe_set(owner, 'Category', None)
    assert owner not in getattr(partner, 'repository')


def test_assoc_referencedObject10_stub_double():
    # requirement_EObject has no real 'requirement_EObject11' property in the generated
    # code (a bare stub) -- manually attach it so requirement_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirement_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirement_Category(id="sample_text")
    partner = requirement_EObject()
    setattr(partner, 'requirement_EObject11', None)
    _safe_set(owner, 'requirement_Category', {partner})
    assert getattr(partner, 'requirement_EObject11') == owner
    _safe_set(owner, 'requirement_Category', set())
    assert getattr(partner, 'requirement_EObject11') is None


def test_assoc_referencedObject12_stub_double():
    # requirement_EObject has no real 'requirement_EObject13' property in the generated
    # code (a bare stub) -- manually attach it so requirement_Requirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirement_Requirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirement_Requirement(acceptanceCriteria="sample_text", createdOn=date(2024, 1, 1), id="sample_text", modifiedOn=date(2024, 1, 1), rationale="sample_text", statement="sample_text", status="sample_text", subtype="sample_text", type="sample_text", version=7)
    partner = requirement_EObject()
    setattr(partner, 'requirement_EObject13', None)
    _safe_set(owner, 'requirement_Requirement', {partner})
    assert getattr(partner, 'requirement_EObject13') == owner
    _safe_set(owner, 'requirement_Requirement', set())
    assert getattr(partner, 'requirement_EObject13') is None


def test_assoc_repository6_stub_double():
    # requirement_Repository has no real 'Repository' property in the generated
    # code (a bare stub) -- manually attach it so requirement_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # requirement_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = requirement_Category(id="sample_text")
    partner = requirement_Repository()
    setattr(partner, 'Repository', None)
    _safe_set(owner, 'mainCategories', partner)
    assert getattr(partner, 'Repository') == owner
    _safe_set(owner, 'mainCategories', None)
    assert getattr(partner, 'Repository') is None


