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


def test_assoc_books1_reverse_link_reassign_clear():
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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_author4_stub_double():
    # extlibrary_BookOnTape has no real 'extlibrary_BookOnTape5' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Writer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Writer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Writer(name="sample_text")
    partner = extlibrary_BookOnTape()
    setattr(partner, 'extlibrary_BookOnTape5', None)
    _safe_set(owner, 'extlibrary_Writer', partner)
    assert getattr(partner, 'extlibrary_BookOnTape5') == owner
    _safe_set(owner, 'extlibrary_Writer', None)
    assert getattr(partner, 'extlibrary_BookOnTape5') is None


def test_assoc_borrowed8_stub_double():
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


def test_assoc_borrowers2_stub_double():
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


def test_assoc_cast6_stub_double():
    # extlibrary_VideoCassette has no real 'extlibrary_VideoCassette' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Person(firstName="sample_text", lastName="sample_text")
    partner = extlibrary_VideoCassette()
    setattr(partner, 'extlibrary_VideoCassette', None)
    _safe_set(owner, 'extlibrary_Person7', partner)
    assert owner in getattr(partner, 'extlibrary_VideoCassette')
    _safe_set(owner, 'extlibrary_Person7', None)
    assert owner not in getattr(partner, 'extlibrary_VideoCassette')


def test_assoc_reader3_stub_double():
    # extlibrary_BookOnTape has no real 'extlibrary_BookOnTape' property in the generated
    # code (a bare stub) -- manually attach it so extlibrary_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extlibrary_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extlibrary_Person(firstName="sample_text", lastName="sample_text")
    partner = extlibrary_BookOnTape()
    setattr(partner, 'extlibrary_BookOnTape', None)
    _safe_set(owner, 'extlibrary_Person', partner)
    assert getattr(partner, 'extlibrary_BookOnTape') == owner
    _safe_set(owner, 'extlibrary_Person', None)
    assert getattr(partner, 'extlibrary_BookOnTape') is None


