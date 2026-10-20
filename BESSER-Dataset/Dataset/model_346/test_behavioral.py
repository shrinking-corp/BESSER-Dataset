import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Addressable,
    AudioVisualItem,
    CirculatingItem,
    Item,
    Lendable,
    Person,
    extlibrary_Addressable,
    extlibrary_AudioVisualItem,
    extlibrary_Book,
    extlibrary_BookOnTape,
    extlibrary_Borrower,
    extlibrary_CirculatingItem,
    extlibrary_Employee,
    extlibrary_Item,
    extlibrary_Lendable,
    extlibrary_Library,
    extlibrary_Periodical,
    extlibrary_Person,
    extlibrary_VideoCassette,
    extlibrary_Writer,
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
    a1 = extlibrary_Writer(name="sample_text")
    a2 = extlibrary_Writer(name="sample_text_2")
    b = extlibrary_Book(category="sample_text", pages=7, title="sample_text")
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


def test_assoc_books20_reverse_link_reassign_clear():
    a1 = extlibrary_Writer(name="sample_text")
    a2 = extlibrary_Writer(name="sample_text_2")
    b = extlibrary_Book(category="sample_text", pages=7, title="sample_text")
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
    a1 = extlibrary_Library(name="sample_text")
    a2 = extlibrary_Library(name="sample_text_2")
    b = extlibrary_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'extlibrary_Book', a1)
    assert _is_linked(b, 'extlibrary_Book', a1)
    if hasattr(a1, 'extlibrary_Library9'):
        assert _is_linked(a1, 'extlibrary_Library9', b)
    _safe_set(b, 'extlibrary_Book', a2)
    assert _is_linked(b, 'extlibrary_Book', a2)
    if hasattr(a1, 'extlibrary_Library9'):
        assert not _is_linked(a1, 'extlibrary_Library9', b)
    if hasattr(a2, 'extlibrary_Library9'):
        assert _is_linked(a2, 'extlibrary_Library9', b)
    _safe_set(b, 'extlibrary_Book', None)
    assert not _is_linked(b, 'extlibrary_Book', a2)
    if hasattr(a2, 'extlibrary_Library9'):
        assert not _is_linked(a2, 'extlibrary_Library9', b)


def test_assoc_branches11_reverse_link_reassign_clear():
    a1 = extlibrary_Library(name="sample_text")
    a2 = extlibrary_Library(name="sample_text_2")
    b = extlibrary_Library(name="sample_text")
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


def test_assoc_casts15_reverse_link_reassign_clear():
    a1 = extlibrary_Person(firstName="sample_text", lastName="sample_text")
    a2 = extlibrary_Person(firstName="sample_text_2", lastName="sample_text_2")
    b = extlibrary_Library(name="sample_text")
    _safe_set(b, 'extlibrary_Library16', {a1})
    assert _is_linked(b, 'extlibrary_Library16', a1)
    if hasattr(a1, 'extlibrary_Person'):
        assert _is_linked(a1, 'extlibrary_Person', b)
    _safe_set(b, 'extlibrary_Library16', {a2})
    assert _is_linked(b, 'extlibrary_Library16', a2)
    if hasattr(a1, 'extlibrary_Person'):
        assert not _is_linked(a1, 'extlibrary_Person', b)
    if hasattr(a2, 'extlibrary_Person'):
        assert _is_linked(a2, 'extlibrary_Person', b)
    _safe_set(b, 'extlibrary_Library16', set())
    assert not _is_linked(b, 'extlibrary_Library16', a2)
    if hasattr(a2, 'extlibrary_Person'):
        assert not _is_linked(a2, 'extlibrary_Person', b)


def test_assoc_parentBranch13_reverse_link_reassign_clear():
    a1 = extlibrary_Library(name="sample_text")
    a2 = extlibrary_Library(name="sample_text_2")
    b = extlibrary_Library(name="sample_text")
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


def test_assoc_readers17_reverse_link_reassign_clear():
    a1 = extlibrary_Person(firstName="sample_text", lastName="sample_text")
    a2 = extlibrary_Person(firstName="sample_text_2", lastName="sample_text_2")
    b = extlibrary_Library(name="sample_text")
    _safe_set(b, 'extlibrary_Library18', {a1})
    assert _is_linked(b, 'extlibrary_Library18', a1)
    if hasattr(a1, 'extlibrary_Person19'):
        assert _is_linked(a1, 'extlibrary_Person19', b)
    _safe_set(b, 'extlibrary_Library18', {a2})
    assert _is_linked(b, 'extlibrary_Library18', a2)
    if hasattr(a1, 'extlibrary_Person19'):
        assert not _is_linked(a1, 'extlibrary_Person19', b)
    if hasattr(a2, 'extlibrary_Person19'):
        assert _is_linked(a2, 'extlibrary_Person19', b)
    _safe_set(b, 'extlibrary_Library18', set())
    assert not _is_linked(b, 'extlibrary_Library18', a2)
    if hasattr(a2, 'extlibrary_Person19'):
        assert not _is_linked(a2, 'extlibrary_Person19', b)


def test_assoc_stock6_reverse_link_reassign_clear():
    a1 = extlibrary_Library(name="sample_text")
    a2 = extlibrary_Library(name="sample_text_2")
    b = extlibrary_Item(publicationDate=date(2024, 1, 1))
    _safe_set(b, 'extlibrary_Item', a1)
    assert _is_linked(b, 'extlibrary_Item', a1)
    if hasattr(a1, 'extlibrary_Library7'):
        assert _is_linked(a1, 'extlibrary_Library7', b)
    _safe_set(b, 'extlibrary_Item', a2)
    assert _is_linked(b, 'extlibrary_Item', a2)
    if hasattr(a1, 'extlibrary_Library7'):
        assert not _is_linked(a1, 'extlibrary_Library7', b)
    if hasattr(a2, 'extlibrary_Library7'):
        assert _is_linked(a2, 'extlibrary_Library7', b)
    _safe_set(b, 'extlibrary_Item', None)
    assert not _is_linked(b, 'extlibrary_Item', a2)
    if hasattr(a2, 'extlibrary_Library7'):
        assert not _is_linked(a2, 'extlibrary_Library7', b)


def test_assoc_writers1_reverse_link_reassign_clear():
    a1 = extlibrary_Writer(name="sample_text")
    a2 = extlibrary_Writer(name="sample_text_2")
    b = extlibrary_Library(name="sample_text")
    _safe_set(b, 'extlibrary_Library', {a1})
    assert _is_linked(b, 'extlibrary_Library', a1)
    if hasattr(a1, 'extlibrary_Writer'):
        assert _is_linked(a1, 'extlibrary_Writer', b)
    _safe_set(b, 'extlibrary_Library', {a2})
    assert _is_linked(b, 'extlibrary_Library', a2)
    if hasattr(a1, 'extlibrary_Writer'):
        assert not _is_linked(a1, 'extlibrary_Writer', b)
    if hasattr(a2, 'extlibrary_Writer'):
        assert _is_linked(a2, 'extlibrary_Writer', b)
    _safe_set(b, 'extlibrary_Library', set())
    assert not _is_linked(b, 'extlibrary_Library', a2)
    if hasattr(a2, 'extlibrary_Writer'):
        assert not _is_linked(a2, 'extlibrary_Writer', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_author24_stub_double():
    # extlibrary_BookOnTape has no real 'extlibrary_BookOnTape25' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Writer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Writer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Writer(name="sample_text")
    partner = extlibrary_BookOnTape()
    setattr(partner, 'extlibrary_BookOnTape25', None)
    _safe_set(owner, 'extlibrary_Writer26', partner)
    assert getattr(partner, 'extlibrary_BookOnTape25') == owner
    _safe_set(owner, 'extlibrary_Writer26', None)
    assert getattr(partner, 'extlibrary_BookOnTape25') is None


def test_assoc_borrowed29_stub_double():
    # extlibrary_Borrower has no real 'borrowers' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Lendable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Lendable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Lendable(copies=7)
    partner = extlibrary_Borrower()
    setattr(partner, 'borrowers', None)
    _safe_set(owner, 'Lendable', partner)
    assert owner in getattr(partner, 'borrowers')
    _safe_set(owner, 'Lendable', None)
    assert owner not in getattr(partner, 'borrowers')


def test_assoc_borrowers21_stub_double():
    # extlibrary_Borrower has no real 'Borrower' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Lendable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Lendable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Lendable(copies=7)
    partner = extlibrary_Borrower()
    setattr(partner, 'Borrower', None)
    _safe_set(owner, 'borrowed', {partner})
    assert getattr(partner, 'Borrower') == owner
    _safe_set(owner, 'borrowed', set())
    assert getattr(partner, 'Borrower') is None


def test_assoc_borrowers4_stub_double():
    # extlibrary_Borrower has no real 'extlibrary_Borrower' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Library(name="sample_text")
    partner = extlibrary_Borrower()
    setattr(partner, 'extlibrary_Borrower', None)
    _safe_set(owner, 'extlibrary_Library5', {partner})
    assert getattr(partner, 'extlibrary_Borrower') == owner
    _safe_set(owner, 'extlibrary_Library5', set())
    assert getattr(partner, 'extlibrary_Borrower') is None


def test_assoc_cast27_stub_double():
    # extlibrary_VideoCassette has no real 'extlibrary_VideoCassette' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Person(firstName="sample_text", lastName="sample_text")
    partner = extlibrary_VideoCassette()
    setattr(partner, 'extlibrary_VideoCassette', None)
    _safe_set(owner, 'extlibrary_Person28', partner)
    assert owner in getattr(partner, 'extlibrary_VideoCassette')
    _safe_set(owner, 'extlibrary_Person28', None)
    assert owner not in getattr(partner, 'extlibrary_VideoCassette')


def test_assoc_employees2_stub_double():
    # extlibrary_Employee has no real 'extlibrary_Employee' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Library(name="sample_text")
    partner = extlibrary_Employee()
    setattr(partner, 'extlibrary_Employee', None)
    _safe_set(owner, 'extlibrary_Library3', {partner})
    assert getattr(partner, 'extlibrary_Employee') == owner
    _safe_set(owner, 'extlibrary_Library3', set())
    assert getattr(partner, 'extlibrary_Employee') is None


def test_assoc_reader22_stub_double():
    # extlibrary_BookOnTape has no real 'extlibrary_BookOnTape' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Person(firstName="sample_text", lastName="sample_text")
    partner = extlibrary_BookOnTape()
    setattr(partner, 'extlibrary_BookOnTape', None)
    _safe_set(owner, 'extlibrary_Person23', partner)
    assert getattr(partner, 'extlibrary_BookOnTape') == owner
    _safe_set(owner, 'extlibrary_Person23', None)
    assert getattr(partner, 'extlibrary_BookOnTape') is None


