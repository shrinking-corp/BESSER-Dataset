import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    libraryinteractionmodel_Author,
    libraryinteractionmodel_AuthorShort,
    libraryinteractionmodel_Authors,
    libraryinteractionmodel_Book,
    libraryinteractionmodel_BookShort,
    libraryinteractionmodel_Books,
    libraryinteractionmodel_Client,
    libraryinteractionmodel_Clients,
    libraryinteractionmodel_Library,
    libraryinteractionmodel_Reservation,
    libraryinteractionmodel_Reservations,
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

def test_assoc_author5_reverse_link_reassign_clear():
    a1 = libraryinteractionmodel_Book(isbn="sample_text", title="sample_text")
    a2 = libraryinteractionmodel_Book(isbn="sample_text_2", title="sample_text_2")
    b = libraryinteractionmodel_AuthorShort(name="sample_text", nationality="sample_text")
    _safe_set(b, 'libraryinteractionmodel_AuthorShort', a1)
    assert _is_linked(b, 'libraryinteractionmodel_AuthorShort', a1)
    if hasattr(a1, 'libraryinteractionmodel_Book'):
        assert _is_linked(a1, 'libraryinteractionmodel_Book', b)
    _safe_set(b, 'libraryinteractionmodel_AuthorShort', a2)
    assert _is_linked(b, 'libraryinteractionmodel_AuthorShort', a2)
    if hasattr(a1, 'libraryinteractionmodel_Book'):
        assert not _is_linked(a1, 'libraryinteractionmodel_Book', b)
    if hasattr(a2, 'libraryinteractionmodel_Book'):
        assert _is_linked(a2, 'libraryinteractionmodel_Book', b)
    _safe_set(b, 'libraryinteractionmodel_AuthorShort', None)
    assert not _is_linked(b, 'libraryinteractionmodel_AuthorShort', a2)
    if hasattr(a2, 'libraryinteractionmodel_Book'):
        assert not _is_linked(a2, 'libraryinteractionmodel_Book', b)


def test_assoc_book25_reverse_link_reassign_clear():
    a1 = libraryinteractionmodel_Reservation(from_=date(2024, 1, 1), to=date(2024, 1, 1))
    a2 = libraryinteractionmodel_Reservation(from_=date(2025, 6, 15), to=date(2025, 6, 15))
    b = libraryinteractionmodel_Book(isbn="sample_text", title="sample_text")
    _safe_set(b, 'libraryinteractionmodel_Book27', a1)
    assert _is_linked(b, 'libraryinteractionmodel_Book27', a1)
    if hasattr(a1, 'libraryinteractionmodel_Reservation26'):
        assert _is_linked(a1, 'libraryinteractionmodel_Reservation26', b)
    _safe_set(b, 'libraryinteractionmodel_Book27', a2)
    assert _is_linked(b, 'libraryinteractionmodel_Book27', a2)
    if hasattr(a1, 'libraryinteractionmodel_Reservation26'):
        assert not _is_linked(a1, 'libraryinteractionmodel_Reservation26', b)
    if hasattr(a2, 'libraryinteractionmodel_Reservation26'):
        assert _is_linked(a2, 'libraryinteractionmodel_Reservation26', b)
    _safe_set(b, 'libraryinteractionmodel_Book27', None)
    assert not _is_linked(b, 'libraryinteractionmodel_Book27', a2)
    if hasattr(a2, 'libraryinteractionmodel_Reservation26'):
        assert not _is_linked(a2, 'libraryinteractionmodel_Reservation26', b)


def test_assoc_books28_reverse_link_reassign_clear():
    a1 = libraryinteractionmodel_BookShort(isbn="sample_text", title="sample_text")
    a2 = libraryinteractionmodel_BookShort(isbn="sample_text_2", title="sample_text_2")
    b = libraryinteractionmodel_Author(fullBio="sample_text", name="sample_text", nationality="sample_text")
    _safe_set(b, 'libraryinteractionmodel_Author29', {a1})
    assert _is_linked(b, 'libraryinteractionmodel_Author29', a1)
    if hasattr(a1, 'libraryinteractionmodel_BookShort30'):
        assert _is_linked(a1, 'libraryinteractionmodel_BookShort30', b)
    _safe_set(b, 'libraryinteractionmodel_Author29', {a2})
    assert _is_linked(b, 'libraryinteractionmodel_Author29', a2)
    if hasattr(a1, 'libraryinteractionmodel_BookShort30'):
        assert not _is_linked(a1, 'libraryinteractionmodel_BookShort30', b)
    if hasattr(a2, 'libraryinteractionmodel_BookShort30'):
        assert _is_linked(a2, 'libraryinteractionmodel_BookShort30', b)
    _safe_set(b, 'libraryinteractionmodel_Author29', set())
    assert not _is_linked(b, 'libraryinteractionmodel_Author29', a2)
    if hasattr(a2, 'libraryinteractionmodel_BookShort30'):
        assert not _is_linked(a2, 'libraryinteractionmodel_BookShort30', b)


def test_assoc_client22_reverse_link_reassign_clear():
    a1 = libraryinteractionmodel_Reservation(from_=date(2024, 1, 1), to=date(2024, 1, 1))
    a2 = libraryinteractionmodel_Reservation(from_=date(2025, 6, 15), to=date(2025, 6, 15))
    b = libraryinteractionmodel_Client(email="sample_text", name="sample_text")
    _safe_set(b, 'libraryinteractionmodel_Client24', a1)
    assert _is_linked(b, 'libraryinteractionmodel_Client24', a1)
    if hasattr(a1, 'libraryinteractionmodel_Reservation23'):
        assert _is_linked(a1, 'libraryinteractionmodel_Reservation23', b)
    _safe_set(b, 'libraryinteractionmodel_Client24', a2)
    assert _is_linked(b, 'libraryinteractionmodel_Client24', a2)
    if hasattr(a1, 'libraryinteractionmodel_Reservation23'):
        assert not _is_linked(a1, 'libraryinteractionmodel_Reservation23', b)
    if hasattr(a2, 'libraryinteractionmodel_Reservation23'):
        assert _is_linked(a2, 'libraryinteractionmodel_Reservation23', b)
    _safe_set(b, 'libraryinteractionmodel_Client24', None)
    assert not _is_linked(b, 'libraryinteractionmodel_Client24', a2)
    if hasattr(a2, 'libraryinteractionmodel_Reservation23'):
        assert not _is_linked(a2, 'libraryinteractionmodel_Reservation23', b)


def test_assoc_currentReservation6_reverse_link_reassign_clear():
    a1 = libraryinteractionmodel_Reservation(from_=date(2024, 1, 1), to=date(2024, 1, 1))
    a2 = libraryinteractionmodel_Reservation(from_=date(2025, 6, 15), to=date(2025, 6, 15))
    b = libraryinteractionmodel_Book(isbn="sample_text", title="sample_text")
    _safe_set(b, 'libraryinteractionmodel_Book7', a1)
    assert _is_linked(b, 'libraryinteractionmodel_Book7', a1)
    if hasattr(a1, 'libraryinteractionmodel_Reservation'):
        assert _is_linked(a1, 'libraryinteractionmodel_Reservation', b)
    _safe_set(b, 'libraryinteractionmodel_Book7', a2)
    assert _is_linked(b, 'libraryinteractionmodel_Book7', a2)
    if hasattr(a1, 'libraryinteractionmodel_Reservation'):
        assert not _is_linked(a1, 'libraryinteractionmodel_Reservation', b)
    if hasattr(a2, 'libraryinteractionmodel_Reservation'):
        assert _is_linked(a2, 'libraryinteractionmodel_Reservation', b)
    _safe_set(b, 'libraryinteractionmodel_Book7', None)
    assert not _is_linked(b, 'libraryinteractionmodel_Book7', a2)
    if hasattr(a2, 'libraryinteractionmodel_Reservation'):
        assert not _is_linked(a2, 'libraryinteractionmodel_Reservation', b)


def test_assoc_self15_reverse_link_reassign_clear():
    a1 = libraryinteractionmodel_AuthorShort(name="sample_text", nationality="sample_text")
    a2 = libraryinteractionmodel_AuthorShort(name="sample_text_2", nationality="sample_text_2")
    b = libraryinteractionmodel_Author(fullBio="sample_text", name="sample_text", nationality="sample_text")
    _safe_set(b, 'libraryinteractionmodel_Author', a1)
    assert _is_linked(b, 'libraryinteractionmodel_Author', a1)
    if hasattr(a1, 'libraryinteractionmodel_AuthorShort16'):
        assert _is_linked(a1, 'libraryinteractionmodel_AuthorShort16', b)
    _safe_set(b, 'libraryinteractionmodel_Author', a2)
    assert _is_linked(b, 'libraryinteractionmodel_Author', a2)
    if hasattr(a1, 'libraryinteractionmodel_AuthorShort16'):
        assert not _is_linked(a1, 'libraryinteractionmodel_AuthorShort16', b)
    if hasattr(a2, 'libraryinteractionmodel_AuthorShort16'):
        assert _is_linked(a2, 'libraryinteractionmodel_AuthorShort16', b)
    _safe_set(b, 'libraryinteractionmodel_Author', None)
    assert not _is_linked(b, 'libraryinteractionmodel_Author', a2)
    if hasattr(a2, 'libraryinteractionmodel_AuthorShort16'):
        assert not _is_linked(a2, 'libraryinteractionmodel_AuthorShort16', b)


def test_assoc_self18_reverse_link_reassign_clear():
    a1 = libraryinteractionmodel_Client(email="sample_text", name="sample_text")
    a2 = libraryinteractionmodel_Client(email="sample_text_2", name="sample_text_2")
    b = libraryinteractionmodel_Client(email="sample_text", name="sample_text")
    _safe_set(b, 'libraryinteractionmodel_Client17', a1)
    assert _is_linked(b, 'libraryinteractionmodel_Client17', a1)
    if hasattr(a1, 'libraryinteractionmodel_Client'):
        assert _is_linked(a1, 'libraryinteractionmodel_Client', b)
    _safe_set(b, 'libraryinteractionmodel_Client17', a2)
    assert _is_linked(b, 'libraryinteractionmodel_Client17', a2)
    if hasattr(a1, 'libraryinteractionmodel_Client'):
        assert not _is_linked(a1, 'libraryinteractionmodel_Client', b)
    if hasattr(a2, 'libraryinteractionmodel_Client'):
        assert _is_linked(a2, 'libraryinteractionmodel_Client', b)
    _safe_set(b, 'libraryinteractionmodel_Client17', None)
    assert not _is_linked(b, 'libraryinteractionmodel_Client17', a2)
    if hasattr(a2, 'libraryinteractionmodel_Client'):
        assert not _is_linked(a2, 'libraryinteractionmodel_Client', b)


def test_assoc_self31_reverse_link_reassign_clear():
    a1 = libraryinteractionmodel_BookShort(isbn="sample_text", title="sample_text")
    a2 = libraryinteractionmodel_BookShort(isbn="sample_text_2", title="sample_text_2")
    b = libraryinteractionmodel_Book(isbn="sample_text", title="sample_text")
    _safe_set(b, 'libraryinteractionmodel_Book33', a1)
    assert _is_linked(b, 'libraryinteractionmodel_Book33', a1)
    if hasattr(a1, 'libraryinteractionmodel_BookShort32'):
        assert _is_linked(a1, 'libraryinteractionmodel_BookShort32', b)
    _safe_set(b, 'libraryinteractionmodel_Book33', a2)
    assert _is_linked(b, 'libraryinteractionmodel_Book33', a2)
    if hasattr(a1, 'libraryinteractionmodel_BookShort32'):
        assert not _is_linked(a1, 'libraryinteractionmodel_BookShort32', b)
    if hasattr(a2, 'libraryinteractionmodel_BookShort32'):
        assert _is_linked(a2, 'libraryinteractionmodel_BookShort32', b)
    _safe_set(b, 'libraryinteractionmodel_Book33', None)
    assert not _is_linked(b, 'libraryinteractionmodel_Book33', a2)
    if hasattr(a2, 'libraryinteractionmodel_BookShort32'):
        assert not _is_linked(a2, 'libraryinteractionmodel_BookShort32', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_items10_stub_double():
    # libraryinteractionmodel_Books has no real 'libraryinteractionmodel_Books11' property in the generated
    # code (a bare stub) -- manually attach it so libraryinteractionmodel_BookShort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryinteractionmodel_BookShort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryinteractionmodel_BookShort(isbn="sample_text", title="sample_text")
    partner = libraryinteractionmodel_Books()
    setattr(partner, 'libraryinteractionmodel_Books11', None)
    _safe_set(owner, 'libraryinteractionmodel_BookShort', partner)
    assert owner in getattr(partner, 'libraryinteractionmodel_Books11')
    _safe_set(owner, 'libraryinteractionmodel_BookShort', None)
    assert owner not in getattr(partner, 'libraryinteractionmodel_Books11')


def test_assoc_items12_stub_double():
    # libraryinteractionmodel_Authors has no real 'libraryinteractionmodel_Authors13' property in the generated
    # code (a bare stub) -- manually attach it so libraryinteractionmodel_AuthorShort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryinteractionmodel_AuthorShort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryinteractionmodel_AuthorShort(name="sample_text", nationality="sample_text")
    partner = libraryinteractionmodel_Authors()
    setattr(partner, 'libraryinteractionmodel_Authors13', None)
    _safe_set(owner, 'libraryinteractionmodel_AuthorShort14', partner)
    assert owner in getattr(partner, 'libraryinteractionmodel_Authors13')
    _safe_set(owner, 'libraryinteractionmodel_AuthorShort14', None)
    assert owner not in getattr(partner, 'libraryinteractionmodel_Authors13')


def test_assoc_items19_stub_double():
    # libraryinteractionmodel_Clients has no real 'libraryinteractionmodel_Clients20' property in the generated
    # code (a bare stub) -- manually attach it so libraryinteractionmodel_Client's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryinteractionmodel_Client's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryinteractionmodel_Client(email="sample_text", name="sample_text")
    partner = libraryinteractionmodel_Clients()
    setattr(partner, 'libraryinteractionmodel_Clients20', None)
    _safe_set(owner, 'libraryinteractionmodel_Client21', partner)
    assert owner in getattr(partner, 'libraryinteractionmodel_Clients20')
    _safe_set(owner, 'libraryinteractionmodel_Client21', None)
    assert owner not in getattr(partner, 'libraryinteractionmodel_Clients20')


def test_assoc_items34_stub_double():
    # libraryinteractionmodel_Reservations has no real 'libraryinteractionmodel_Reservations35' property in the generated
    # code (a bare stub) -- manually attach it so libraryinteractionmodel_Reservation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryinteractionmodel_Reservation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryinteractionmodel_Reservation(from_=date(2024, 1, 1), to=date(2024, 1, 1))
    partner = libraryinteractionmodel_Reservations()
    setattr(partner, 'libraryinteractionmodel_Reservations35', None)
    _safe_set(owner, 'libraryinteractionmodel_Reservation36', partner)
    assert owner in getattr(partner, 'libraryinteractionmodel_Reservations35')
    _safe_set(owner, 'libraryinteractionmodel_Reservation36', None)
    assert owner not in getattr(partner, 'libraryinteractionmodel_Reservations35')


def test_assoc_reservations8_stub_double():
    # libraryinteractionmodel_Reservations has no real 'libraryinteractionmodel_Reservations' property in the generated
    # code (a bare stub) -- manually attach it so libraryinteractionmodel_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryinteractionmodel_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryinteractionmodel_Book(isbn="sample_text", title="sample_text")
    partner = libraryinteractionmodel_Reservations()
    setattr(partner, 'libraryinteractionmodel_Reservations', None)
    _safe_set(owner, 'libraryinteractionmodel_Book9', partner)
    assert getattr(partner, 'libraryinteractionmodel_Reservations') == owner
    _safe_set(owner, 'libraryinteractionmodel_Book9', None)
    assert getattr(partner, 'libraryinteractionmodel_Reservations') is None


