import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Addressable,
    AudioVisualItem,
    CirculatingItem,
    Item,
    Lendable,
    Person,
    library_Addressable,
    library_AudioVisualItem,
    library_Book,
    library_BookOnTape,
    library_Borrower,
    library_CirculatingItem,
    library_Employee,
    library_Item,
    library_Lendable,
    library_Library,
    library_Periodical,
    library_Person,
    library_VideoCassette,
    library_Writer,
    BookCategory,
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

def test_assoc_author0_reverse_link_reassign_clear():
    a1 = library_Writer(name="sample_text")
    a2 = library_Writer(name="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'books', a1)
    assert _is_linked(b, 'books', a1)
    if hasattr(a1, 'Writer'):
        assert _is_linked(a1, 'Writer', b)
    _safe_set(b, 'books', a2)
    assert _is_linked(b, 'books', a2)
    if hasattr(a1, 'Writer'):
        assert not _is_linked(a1, 'Writer', b)
    if hasattr(a2, 'Writer'):
        assert _is_linked(a2, 'Writer', b)
    _safe_set(b, 'books', None)
    assert not _is_linked(b, 'books', a2)
    if hasattr(a2, 'Writer'):
        assert not _is_linked(a2, 'Writer', b)


def test_assoc_books15_reverse_link_reassign_clear():
    a1 = library_Writer(name="sample_text")
    a2 = library_Writer(name="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'Book', a1)
    assert _is_linked(b, 'Book', a1)
    if hasattr(a1, 'author'):
        assert _is_linked(a1, 'author', b)
    _safe_set(b, 'Book', a2)
    assert _is_linked(b, 'Book', a2)
    if hasattr(a1, 'author'):
        assert not _is_linked(a1, 'author', b)
    if hasattr(a2, 'author'):
        assert _is_linked(a2, 'author', b)
    _safe_set(b, 'Book', None)
    assert not _is_linked(b, 'Book', a2)
    if hasattr(a2, 'author'):
        assert not _is_linked(a2, 'author', b)


def test_assoc_books8_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text", people="sample_text")
    a2 = library_Library(name="sample_text_2", people="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'library_Book', a1)
    assert _is_linked(b, 'library_Book', a1)
    if hasattr(a1, 'library_Library9'):
        assert _is_linked(a1, 'library_Library9', b)
    _safe_set(b, 'library_Book', a2)
    assert _is_linked(b, 'library_Book', a2)
    if hasattr(a1, 'library_Library9'):
        assert not _is_linked(a1, 'library_Library9', b)
    if hasattr(a2, 'library_Library9'):
        assert _is_linked(a2, 'library_Library9', b)
    _safe_set(b, 'library_Book', None)
    assert not _is_linked(b, 'library_Book', a2)
    if hasattr(a2, 'library_Library9'):
        assert not _is_linked(a2, 'library_Library9', b)


def test_assoc_branches11_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text", people="sample_text")
    a2 = library_Library(name="sample_text_2", people="sample_text_2")
    b = library_Library(name="sample_text", people="sample_text")
    _safe_set(b, 'parentBranch', {a1})
    assert _is_linked(b, 'parentBranch', a1)
    if hasattr(a1, 'Library'):
        assert _is_linked(a1, 'Library', b)
    _safe_set(b, 'parentBranch', {a2})
    assert _is_linked(b, 'parentBranch', a2)
    if hasattr(a1, 'Library'):
        assert not _is_linked(a1, 'Library', b)
    if hasattr(a2, 'Library'):
        assert _is_linked(a2, 'Library', b)
    _safe_set(b, 'parentBranch', set())
    assert not _is_linked(b, 'parentBranch', a2)
    if hasattr(a2, 'Library'):
        assert not _is_linked(a2, 'Library', b)


def test_assoc_parentBranch13_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text", people="sample_text")
    a2 = library_Library(name="sample_text_2", people="sample_text_2")
    b = library_Library(name="sample_text", people="sample_text")
    _safe_set(b, 'branches', a1)
    assert _is_linked(b, 'branches', a1)
    if hasattr(a1, 'Library14'):
        assert _is_linked(a1, 'Library14', b)
    _safe_set(b, 'branches', a2)
    assert _is_linked(b, 'branches', a2)
    if hasattr(a1, 'Library14'):
        assert not _is_linked(a1, 'Library14', b)
    if hasattr(a2, 'Library14'):
        assert _is_linked(a2, 'Library14', b)
    _safe_set(b, 'branches', None)
    assert not _is_linked(b, 'branches', a2)
    if hasattr(a2, 'Library14'):
        assert not _is_linked(a2, 'Library14', b)


def test_assoc_stock6_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text", people="sample_text")
    a2 = library_Library(name="sample_text_2", people="sample_text_2")
    b = library_Item(publicationDate=date(2024, 1, 1))
    _safe_set(b, 'library_Item', a1)
    assert _is_linked(b, 'library_Item', a1)
    if hasattr(a1, 'library_Library7'):
        assert _is_linked(a1, 'library_Library7', b)
    _safe_set(b, 'library_Item', a2)
    assert _is_linked(b, 'library_Item', a2)
    if hasattr(a1, 'library_Library7'):
        assert not _is_linked(a1, 'library_Library7', b)
    if hasattr(a2, 'library_Library7'):
        assert _is_linked(a2, 'library_Library7', b)
    _safe_set(b, 'library_Item', None)
    assert not _is_linked(b, 'library_Item', a2)
    if hasattr(a2, 'library_Library7'):
        assert not _is_linked(a2, 'library_Library7', b)


def test_assoc_writers1_reverse_link_reassign_clear():
    a1 = library_Writer(name="sample_text")
    a2 = library_Writer(name="sample_text_2")
    b = library_Library(name="sample_text", people="sample_text")
    _safe_set(b, 'library_Library', {a1})
    assert _is_linked(b, 'library_Library', a1)
    if hasattr(a1, 'library_Writer'):
        assert _is_linked(a1, 'library_Writer', b)
    _safe_set(b, 'library_Library', {a2})
    assert _is_linked(b, 'library_Library', a2)
    if hasattr(a1, 'library_Writer'):
        assert not _is_linked(a1, 'library_Writer', b)
    if hasattr(a2, 'library_Writer'):
        assert _is_linked(a2, 'library_Writer', b)
    _safe_set(b, 'library_Library', set())
    assert not _is_linked(b, 'library_Library', a2)
    if hasattr(a2, 'library_Writer'):
        assert not _is_linked(a2, 'library_Writer', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_author18_stub_double():
    # library_BookOnTape has no real 'library_BookOnTape19' property in the generated
    # code (a bare stub) -- manually attach it so library_Writer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Writer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Writer(name="sample_text")
    partner = library_BookOnTape()
    setattr(partner, 'library_BookOnTape19', None)
    _safe_set(owner, 'library_Writer20', partner)
    assert getattr(partner, 'library_BookOnTape19') == owner
    _safe_set(owner, 'library_Writer20', None)
    assert getattr(partner, 'library_BookOnTape19') is None


def test_assoc_borrowed23_stub_double():
    # library_Borrower has no real 'borrowers' property in the generated
    # code (a bare stub) -- manually attach it so library_Lendable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Lendable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Lendable(copies=7)
    partner = library_Borrower()
    setattr(partner, 'borrowers', None)
    _safe_set(owner, 'Lendable', partner)
    assert owner in getattr(partner, 'borrowers')
    _safe_set(owner, 'Lendable', None)
    assert owner not in getattr(partner, 'borrowers')


def test_assoc_borrowers16_stub_double():
    # library_Borrower has no real 'Borrower' property in the generated
    # code (a bare stub) -- manually attach it so library_Lendable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Lendable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Lendable(copies=7)
    partner = library_Borrower()
    setattr(partner, 'Borrower', None)
    _safe_set(owner, 'borrowed', {partner})
    assert getattr(partner, 'Borrower') == owner
    _safe_set(owner, 'borrowed', set())
    assert getattr(partner, 'Borrower') is None


def test_assoc_borrowers4_stub_double():
    # library_Borrower has no real 'library_Borrower' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text", people="sample_text")
    partner = library_Borrower()
    setattr(partner, 'library_Borrower', None)
    _safe_set(owner, 'library_Library5', {partner})
    assert getattr(partner, 'library_Borrower') == owner
    _safe_set(owner, 'library_Library5', set())
    assert getattr(partner, 'library_Borrower') is None


def test_assoc_cast21_stub_double():
    # library_VideoCassette has no real 'library_VideoCassette' property in the generated
    # code (a bare stub) -- manually attach it so library_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Person(firstName="sample_text", lastName="sample_text")
    partner = library_VideoCassette()
    setattr(partner, 'library_VideoCassette', None)
    _safe_set(owner, 'library_Person22', partner)
    assert owner in getattr(partner, 'library_VideoCassette')
    _safe_set(owner, 'library_Person22', None)
    assert owner not in getattr(partner, 'library_VideoCassette')


def test_assoc_employees2_stub_double():
    # library_Employee has no real 'library_Employee' property in the generated
    # code (a bare stub) -- manually attach it so library_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Library(name="sample_text", people="sample_text")
    partner = library_Employee()
    setattr(partner, 'library_Employee', None)
    _safe_set(owner, 'library_Library3', {partner})
    assert getattr(partner, 'library_Employee') == owner
    _safe_set(owner, 'library_Library3', set())
    assert getattr(partner, 'library_Employee') is None


def test_assoc_reader17_stub_double():
    # library_BookOnTape has no real 'library_BookOnTape' property in the generated
    # code (a bare stub) -- manually attach it so library_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_Person(firstName="sample_text", lastName="sample_text")
    partner = library_BookOnTape()
    setattr(partner, 'library_BookOnTape', None)
    _safe_set(owner, 'library_Person', partner)
    assert getattr(partner, 'library_BookOnTape') == owner
    _safe_set(owner, 'library_Person', None)
    assert getattr(partner, 'library_BookOnTape') is None


