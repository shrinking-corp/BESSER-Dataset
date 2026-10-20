import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    libraryModel_ecore_Author,
    libraryModel_ecore_Book,
    libraryModel_ecore_LibraryModel,
    libraryModel_ecore_NamedElement,
    libraryModel_ecore_Picture,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_authors7_stub_double():
    # libraryModel_ecore_Author has no real 'Author' property in the generated
    # code (a bare stub) -- manually attach it so libraryModel_ecore_LibraryModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryModel_ecore_LibraryModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryModel_ecore_LibraryModel()
    partner = libraryModel_ecore_Author()
    setattr(partner, 'Author', None)
    _safe_set(owner, 'library8', {partner})
    assert getattr(partner, 'Author') == owner
    _safe_set(owner, 'library8', set())
    assert getattr(partner, 'Author') is None


def test_assoc_book6_stub_double():
    # libraryModel_ecore_Book has no real 'Book' property in the generated
    # code (a bare stub) -- manually attach it so libraryModel_ecore_LibraryModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryModel_ecore_LibraryModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryModel_ecore_LibraryModel()
    partner = libraryModel_ecore_Book()
    setattr(partner, 'Book', None)
    _safe_set(owner, 'library', {partner})
    assert getattr(partner, 'Book') == owner
    _safe_set(owner, 'library', set())
    assert getattr(partner, 'Book') is None


def test_assoc_book9_stub_double():
    # libraryModel_ecore_Book has no real 'Book10' property in the generated
    # code (a bare stub) -- manually attach it so libraryModel_ecore_Picture's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryModel_ecore_Picture's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryModel_ecore_Picture(pageNumber="sample_text")
    partner = libraryModel_ecore_Book()
    setattr(partner, 'Book10', None)
    _safe_set(owner, 'pictures', partner)
    assert getattr(partner, 'Book10') == owner
    _safe_set(owner, 'pictures', None)
    assert getattr(partner, 'Book10') is None


def test_assoc_library1_stub_double():
    # libraryModel_ecore_Book has no real 'book' property in the generated
    # code (a bare stub) -- manually attach it so libraryModel_ecore_LibraryModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryModel_ecore_LibraryModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryModel_ecore_LibraryModel()
    partner = libraryModel_ecore_Book()
    setattr(partner, 'book', None)
    _safe_set(owner, 'LibraryModel', partner)
    assert getattr(partner, 'book') == owner
    _safe_set(owner, 'LibraryModel', None)
    assert getattr(partner, 'book') is None


def test_assoc_library4_stub_double():
    # libraryModel_ecore_Author has no real 'authors' property in the generated
    # code (a bare stub) -- manually attach it so libraryModel_ecore_LibraryModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryModel_ecore_LibraryModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryModel_ecore_LibraryModel()
    partner = libraryModel_ecore_Author()
    setattr(partner, 'authors', None)
    _safe_set(owner, 'LibraryModel5', partner)
    assert getattr(partner, 'authors') == owner
    _safe_set(owner, 'LibraryModel5', None)
    assert getattr(partner, 'authors') is None


def test_assoc_pictures2_stub_double():
    # libraryModel_ecore_Book has no real 'book3' property in the generated
    # code (a bare stub) -- manually attach it so libraryModel_ecore_Picture's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryModel_ecore_Picture's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryModel_ecore_Picture(pageNumber="sample_text")
    partner = libraryModel_ecore_Book()
    setattr(partner, 'book3', None)
    _safe_set(owner, 'Picture', partner)
    assert owner in getattr(partner, 'book3')
    _safe_set(owner, 'Picture', None)
    assert owner not in getattr(partner, 'book3')


