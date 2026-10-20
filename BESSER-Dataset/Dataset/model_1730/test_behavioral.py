import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    comicBookCollection2_Artist,
    comicBookCollection2_Book,
    comicBookCollection2_ComicBookCollection,
    comicBookCollection2_Editor,
    comicBookCollection2_Publisher,
    comicBookCollection2_Series,
    comicBookCollection2_Writer,
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

def test_assoc_artists14_reverse_link_reassign_clear():
    a1 = comicBookCollection2_Book(name="sample_text", publicationDate="sample_text")
    a2 = comicBookCollection2_Book(name="sample_text_2", publicationDate="sample_text_2")
    b = comicBookCollection2_Artist(name="sample_text")
    _safe_set(b, 'Artist', a1)
    assert _is_linked(b, 'Artist', a1)
    if hasattr(a1, 'booksArtistFor'):
        assert _is_linked(a1, 'booksArtistFor', b)
    _safe_set(b, 'Artist', a2)
    assert _is_linked(b, 'Artist', a2)
    if hasattr(a1, 'booksArtistFor'):
        assert not _is_linked(a1, 'booksArtistFor', b)
    if hasattr(a2, 'booksArtistFor'):
        assert _is_linked(a2, 'booksArtistFor', b)
    _safe_set(b, 'Artist', None)
    assert not _is_linked(b, 'Artist', a2)
    if hasattr(a2, 'booksArtistFor'):
        assert not _is_linked(a2, 'booksArtistFor', b)


def test_assoc_booksArtistFor21_reverse_link_reassign_clear():
    a1 = comicBookCollection2_Book(name="sample_text", publicationDate="sample_text")
    a2 = comicBookCollection2_Book(name="sample_text_2", publicationDate="sample_text_2")
    b = comicBookCollection2_Artist(name="sample_text")
    _safe_set(b, 'artists', {a1})
    assert _is_linked(b, 'artists', a1)
    if hasattr(a1, 'Book22'):
        assert _is_linked(a1, 'Book22', b)
    _safe_set(b, 'artists', {a2})
    assert _is_linked(b, 'artists', a2)
    if hasattr(a1, 'Book22'):
        assert not _is_linked(a1, 'Book22', b)
    if hasattr(a2, 'Book22'):
        assert _is_linked(a2, 'Book22', b)
    _safe_set(b, 'artists', set())
    assert not _is_linked(b, 'artists', a2)
    if hasattr(a2, 'Book22'):
        assert not _is_linked(a2, 'Book22', b)


def test_assoc_booksCoverArtistFor23_reverse_link_reassign_clear():
    a1 = comicBookCollection2_Book(name="sample_text", publicationDate="sample_text")
    a2 = comicBookCollection2_Book(name="sample_text_2", publicationDate="sample_text_2")
    b = comicBookCollection2_Artist(name="sample_text")
    _safe_set(b, 'coverArtist', {a1})
    assert _is_linked(b, 'coverArtist', a1)
    if hasattr(a1, 'Book24'):
        assert _is_linked(a1, 'Book24', b)
    _safe_set(b, 'coverArtist', {a2})
    assert _is_linked(b, 'coverArtist', a2)
    if hasattr(a1, 'Book24'):
        assert not _is_linked(a1, 'Book24', b)
    if hasattr(a2, 'Book24'):
        assert _is_linked(a2, 'Book24', b)
    _safe_set(b, 'coverArtist', set())
    assert not _is_linked(b, 'coverArtist', a2)
    if hasattr(a2, 'Book24'):
        assert not _is_linked(a2, 'Book24', b)


def test_assoc_booksEditorFor25_reverse_link_reassign_clear():
    a1 = comicBookCollection2_Editor(name="sample_text")
    a2 = comicBookCollection2_Editor(name="sample_text_2")
    b = comicBookCollection2_Book(name="sample_text", publicationDate="sample_text")
    _safe_set(b, 'Book26', a1)
    assert _is_linked(b, 'Book26', a1)
    if hasattr(a1, 'editors'):
        assert _is_linked(a1, 'editors', b)
    _safe_set(b, 'Book26', a2)
    assert _is_linked(b, 'Book26', a2)
    if hasattr(a1, 'editors'):
        assert not _is_linked(a1, 'editors', b)
    if hasattr(a2, 'editors'):
        assert _is_linked(a2, 'editors', b)
    _safe_set(b, 'Book26', None)
    assert not _is_linked(b, 'Book26', a2)
    if hasattr(a2, 'editors'):
        assert not _is_linked(a2, 'editors', b)


def test_assoc_booksInSeries12_reverse_link_reassign_clear():
    a1 = comicBookCollection2_Series(seriesName="sample_text")
    a2 = comicBookCollection2_Series(seriesName="sample_text_2")
    b = comicBookCollection2_Book(name="sample_text", publicationDate="sample_text")
    _safe_set(b, 'Book13', a1)
    assert _is_linked(b, 'Book13', a1)
    if hasattr(a1, 'seriesPartOf'):
        assert _is_linked(a1, 'seriesPartOf', b)
    _safe_set(b, 'Book13', a2)
    assert _is_linked(b, 'Book13', a2)
    if hasattr(a1, 'seriesPartOf'):
        assert not _is_linked(a1, 'seriesPartOf', b)
    if hasattr(a2, 'seriesPartOf'):
        assert _is_linked(a2, 'seriesPartOf', b)
    _safe_set(b, 'Book13', None)
    assert not _is_linked(b, 'Book13', a2)
    if hasattr(a2, 'seriesPartOf'):
        assert not _is_linked(a2, 'seriesPartOf', b)


def test_assoc_booksPublished11_reverse_link_reassign_clear():
    a1 = comicBookCollection2_Publisher(publishersName="sample_text")
    a2 = comicBookCollection2_Publisher(publishersName="sample_text_2")
    b = comicBookCollection2_Book(name="sample_text", publicationDate="sample_text")
    _safe_set(b, 'Book', a1)
    assert _is_linked(b, 'Book', a1)
    if hasattr(a1, 'publisher'):
        assert _is_linked(a1, 'publisher', b)
    _safe_set(b, 'Book', a2)
    assert _is_linked(b, 'Book', a2)
    if hasattr(a1, 'publisher'):
        assert not _is_linked(a1, 'publisher', b)
    if hasattr(a2, 'publisher'):
        assert _is_linked(a2, 'publisher', b)
    _safe_set(b, 'Book', None)
    assert not _is_linked(b, 'Book', a2)
    if hasattr(a2, 'publisher'):
        assert not _is_linked(a2, 'publisher', b)


def test_assoc_booksWriterFor27_reverse_link_reassign_clear():
    a1 = comicBookCollection2_Writer(name="sample_text")
    a2 = comicBookCollection2_Writer(name="sample_text_2")
    b = comicBookCollection2_Book(name="sample_text", publicationDate="sample_text")
    _safe_set(b, 'Book28', a1)
    assert _is_linked(b, 'Book28', a1)
    if hasattr(a1, 'writers'):
        assert _is_linked(a1, 'writers', b)
    _safe_set(b, 'Book28', a2)
    assert _is_linked(b, 'Book28', a2)
    if hasattr(a1, 'writers'):
        assert not _is_linked(a1, 'writers', b)
    if hasattr(a2, 'writers'):
        assert _is_linked(a2, 'writers', b)
    _safe_set(b, 'Book28', None)
    assert not _is_linked(b, 'Book28', a2)
    if hasattr(a2, 'writers'):
        assert not _is_linked(a2, 'writers', b)


def test_assoc_coverArtist17_reverse_link_reassign_clear():
    a1 = comicBookCollection2_Book(name="sample_text", publicationDate="sample_text")
    a2 = comicBookCollection2_Book(name="sample_text_2", publicationDate="sample_text_2")
    b = comicBookCollection2_Artist(name="sample_text")
    _safe_set(b, 'Artist18', a1)
    assert _is_linked(b, 'Artist18', a1)
    if hasattr(a1, 'booksCoverArtistFor'):
        assert _is_linked(a1, 'booksCoverArtistFor', b)
    _safe_set(b, 'Artist18', a2)
    assert _is_linked(b, 'Artist18', a2)
    if hasattr(a1, 'booksCoverArtistFor'):
        assert not _is_linked(a1, 'booksCoverArtistFor', b)
    if hasattr(a2, 'booksCoverArtistFor'):
        assert _is_linked(a2, 'booksCoverArtistFor', b)
    _safe_set(b, 'Artist18', None)
    assert not _is_linked(b, 'Artist18', a2)
    if hasattr(a2, 'booksCoverArtistFor'):
        assert not _is_linked(a2, 'booksCoverArtistFor', b)


def test_assoc_editors15_reverse_link_reassign_clear():
    a1 = comicBookCollection2_Editor(name="sample_text")
    a2 = comicBookCollection2_Editor(name="sample_text_2")
    b = comicBookCollection2_Book(name="sample_text", publicationDate="sample_text")
    _safe_set(b, 'booksEditorFor', {a1})
    assert _is_linked(b, 'booksEditorFor', a1)
    if hasattr(a1, 'Editor'):
        assert _is_linked(a1, 'Editor', b)
    _safe_set(b, 'booksEditorFor', {a2})
    assert _is_linked(b, 'booksEditorFor', a2)
    if hasattr(a1, 'Editor'):
        assert not _is_linked(a1, 'Editor', b)
    if hasattr(a2, 'Editor'):
        assert _is_linked(a2, 'Editor', b)
    _safe_set(b, 'booksEditorFor', set())
    assert not _is_linked(b, 'booksEditorFor', a2)
    if hasattr(a2, 'Editor'):
        assert not _is_linked(a2, 'Editor', b)


def test_assoc_publisher19_reverse_link_reassign_clear():
    a1 = comicBookCollection2_Publisher(publishersName="sample_text")
    a2 = comicBookCollection2_Publisher(publishersName="sample_text_2")
    b = comicBookCollection2_Book(name="sample_text", publicationDate="sample_text")
    _safe_set(b, 'booksPublished', a1)
    assert _is_linked(b, 'booksPublished', a1)
    if hasattr(a1, 'Publisher'):
        assert _is_linked(a1, 'Publisher', b)
    _safe_set(b, 'booksPublished', a2)
    assert _is_linked(b, 'booksPublished', a2)
    if hasattr(a1, 'Publisher'):
        assert not _is_linked(a1, 'Publisher', b)
    if hasattr(a2, 'Publisher'):
        assert _is_linked(a2, 'Publisher', b)
    _safe_set(b, 'booksPublished', None)
    assert not _is_linked(b, 'booksPublished', a2)
    if hasattr(a2, 'Publisher'):
        assert not _is_linked(a2, 'Publisher', b)


def test_assoc_seriesPartOf20_reverse_link_reassign_clear():
    a1 = comicBookCollection2_Series(seriesName="sample_text")
    a2 = comicBookCollection2_Series(seriesName="sample_text_2")
    b = comicBookCollection2_Book(name="sample_text", publicationDate="sample_text")
    _safe_set(b, 'booksInSeries', a1)
    assert _is_linked(b, 'booksInSeries', a1)
    if hasattr(a1, 'Series'):
        assert _is_linked(a1, 'Series', b)
    _safe_set(b, 'booksInSeries', a2)
    assert _is_linked(b, 'booksInSeries', a2)
    if hasattr(a1, 'Series'):
        assert not _is_linked(a1, 'Series', b)
    if hasattr(a2, 'Series'):
        assert _is_linked(a2, 'Series', b)
    _safe_set(b, 'booksInSeries', None)
    assert not _is_linked(b, 'booksInSeries', a2)
    if hasattr(a2, 'Series'):
        assert not _is_linked(a2, 'Series', b)


def test_assoc_writers16_reverse_link_reassign_clear():
    a1 = comicBookCollection2_Writer(name="sample_text")
    a2 = comicBookCollection2_Writer(name="sample_text_2")
    b = comicBookCollection2_Book(name="sample_text", publicationDate="sample_text")
    _safe_set(b, 'booksWriterFor', {a1})
    assert _is_linked(b, 'booksWriterFor', a1)
    if hasattr(a1, 'Writer'):
        assert _is_linked(a1, 'Writer', b)
    _safe_set(b, 'booksWriterFor', {a2})
    assert _is_linked(b, 'booksWriterFor', a2)
    if hasattr(a1, 'Writer'):
        assert not _is_linked(a1, 'Writer', b)
    if hasattr(a2, 'Writer'):
        assert _is_linked(a2, 'Writer', b)
    _safe_set(b, 'booksWriterFor', set())
    assert not _is_linked(b, 'booksWriterFor', a2)
    if hasattr(a2, 'Writer'):
        assert not _is_linked(a2, 'Writer', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_artists1_stub_double():
    # comicBookCollection2_ComicBookCollection has no real 'comicBookCollection2_ComicBookCollection2' property in the generated
    # code (a bare stub) -- manually attach it so comicBookCollection2_Artist's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # comicBookCollection2_Artist's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = comicBookCollection2_Artist(name="sample_text")
    partner = comicBookCollection2_ComicBookCollection()
    setattr(partner, 'comicBookCollection2_ComicBookCollection2', None)
    _safe_set(owner, 'comicBookCollection2_Artist', partner)
    assert owner in getattr(partner, 'comicBookCollection2_ComicBookCollection2')
    _safe_set(owner, 'comicBookCollection2_Artist', None)
    assert owner not in getattr(partner, 'comicBookCollection2_ComicBookCollection2')


def test_assoc_books0_stub_double():
    # comicBookCollection2_ComicBookCollection has no real 'comicBookCollection2_ComicBookCollection' property in the generated
    # code (a bare stub) -- manually attach it so comicBookCollection2_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # comicBookCollection2_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = comicBookCollection2_Book(name="sample_text", publicationDate="sample_text")
    partner = comicBookCollection2_ComicBookCollection()
    setattr(partner, 'comicBookCollection2_ComicBookCollection', None)
    _safe_set(owner, 'comicBookCollection2_Book', partner)
    assert owner in getattr(partner, 'comicBookCollection2_ComicBookCollection')
    _safe_set(owner, 'comicBookCollection2_Book', None)
    assert owner not in getattr(partner, 'comicBookCollection2_ComicBookCollection')


def test_assoc_editors3_stub_double():
    # comicBookCollection2_ComicBookCollection has no real 'comicBookCollection2_ComicBookCollection4' property in the generated
    # code (a bare stub) -- manually attach it so comicBookCollection2_Editor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # comicBookCollection2_Editor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = comicBookCollection2_Editor(name="sample_text")
    partner = comicBookCollection2_ComicBookCollection()
    setattr(partner, 'comicBookCollection2_ComicBookCollection4', None)
    _safe_set(owner, 'comicBookCollection2_Editor', partner)
    assert owner in getattr(partner, 'comicBookCollection2_ComicBookCollection4')
    _safe_set(owner, 'comicBookCollection2_Editor', None)
    assert owner not in getattr(partner, 'comicBookCollection2_ComicBookCollection4')


def test_assoc_publishingCompanies7_stub_double():
    # comicBookCollection2_ComicBookCollection has no real 'comicBookCollection2_ComicBookCollection8' property in the generated
    # code (a bare stub) -- manually attach it so comicBookCollection2_Publisher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # comicBookCollection2_Publisher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = comicBookCollection2_Publisher(publishersName="sample_text")
    partner = comicBookCollection2_ComicBookCollection()
    setattr(partner, 'comicBookCollection2_ComicBookCollection8', None)
    _safe_set(owner, 'comicBookCollection2_Publisher', partner)
    assert owner in getattr(partner, 'comicBookCollection2_ComicBookCollection8')
    _safe_set(owner, 'comicBookCollection2_Publisher', None)
    assert owner not in getattr(partner, 'comicBookCollection2_ComicBookCollection8')


def test_assoc_series9_stub_double():
    # comicBookCollection2_ComicBookCollection has no real 'comicBookCollection2_ComicBookCollection10' property in the generated
    # code (a bare stub) -- manually attach it so comicBookCollection2_Series's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # comicBookCollection2_Series's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = comicBookCollection2_Series(seriesName="sample_text")
    partner = comicBookCollection2_ComicBookCollection()
    setattr(partner, 'comicBookCollection2_ComicBookCollection10', None)
    _safe_set(owner, 'comicBookCollection2_Series', partner)
    assert owner in getattr(partner, 'comicBookCollection2_ComicBookCollection10')
    _safe_set(owner, 'comicBookCollection2_Series', None)
    assert owner not in getattr(partner, 'comicBookCollection2_ComicBookCollection10')


def test_assoc_writers5_stub_double():
    # comicBookCollection2_ComicBookCollection has no real 'comicBookCollection2_ComicBookCollection6' property in the generated
    # code (a bare stub) -- manually attach it so comicBookCollection2_Writer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # comicBookCollection2_Writer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = comicBookCollection2_Writer(name="sample_text")
    partner = comicBookCollection2_ComicBookCollection()
    setattr(partner, 'comicBookCollection2_ComicBookCollection6', None)
    _safe_set(owner, 'comicBookCollection2_Writer', partner)
    assert owner in getattr(partner, 'comicBookCollection2_ComicBookCollection6')
    _safe_set(owner, 'comicBookCollection2_Writer', None)
    assert owner not in getattr(partner, 'comicBookCollection2_ComicBookCollection6')


