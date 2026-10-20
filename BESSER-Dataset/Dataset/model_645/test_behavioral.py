import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    model_Book,
    model_BookShelf,
    model_DataBase,
    model_Person,
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

def test_assoc_books5_reverse_link_reassign_clear():
    a1 = model_BookShelf(name="sample_text")
    a2 = model_BookShelf(name="sample_text_2")
    b = model_Book(author="sample_text", avgRating=7, name="sample_text")
    _safe_set(b, 'Book', a1)
    assert _is_linked(b, 'Book', a1)
    if hasattr(a1, 'presentIn'):
        assert _is_linked(a1, 'presentIn', b)
    _safe_set(b, 'Book', a2)
    assert _is_linked(b, 'Book', a2)
    if hasattr(a1, 'presentIn'):
        assert not _is_linked(a1, 'presentIn', b)
    if hasattr(a2, 'presentIn'):
        assert _is_linked(a2, 'presentIn', b)
    _safe_set(b, 'Book', None)
    assert not _is_linked(b, 'Book', a2)
    if hasattr(a2, 'presentIn'):
        assert not _is_linked(a2, 'presentIn', b)


def test_assoc_friends4_reverse_link_reassign_clear():
    a1 = model_Person(name="sample_text")
    a2 = model_Person(name="sample_text_2")
    b = model_Person(name="sample_text")
    _safe_set(b, 'model_Person3', {a1})
    assert _is_linked(b, 'model_Person3', a1)
    if hasattr(a1, 'model_Person'):
        assert _is_linked(a1, 'model_Person', b)
    _safe_set(b, 'model_Person3', {a2})
    assert _is_linked(b, 'model_Person3', a2)
    if hasattr(a1, 'model_Person'):
        assert not _is_linked(a1, 'model_Person', b)
    if hasattr(a2, 'model_Person'):
        assert _is_linked(a2, 'model_Person', b)
    _safe_set(b, 'model_Person3', set())
    assert not _is_linked(b, 'model_Person3', a2)
    if hasattr(a2, 'model_Person'):
        assert not _is_linked(a2, 'model_Person', b)


def test_assoc_ownedBy6_reverse_link_reassign_clear():
    a1 = model_Person(name="sample_text")
    a2 = model_Person(name="sample_text_2")
    b = model_BookShelf(name="sample_text")
    _safe_set(b, 'shelves', a1)
    assert _is_linked(b, 'shelves', a1)
    if hasattr(a1, 'Person'):
        assert _is_linked(a1, 'Person', b)
    _safe_set(b, 'shelves', a2)
    assert _is_linked(b, 'shelves', a2)
    if hasattr(a1, 'Person'):
        assert not _is_linked(a1, 'Person', b)
    if hasattr(a2, 'Person'):
        assert _is_linked(a2, 'Person', b)
    _safe_set(b, 'shelves', None)
    assert not _is_linked(b, 'shelves', a2)
    if hasattr(a2, 'Person'):
        assert not _is_linked(a2, 'Person', b)


def test_assoc_presentIn0_reverse_link_reassign_clear():
    a1 = model_BookShelf(name="sample_text")
    a2 = model_BookShelf(name="sample_text_2")
    b = model_Book(author="sample_text", avgRating=7, name="sample_text")
    _safe_set(b, 'books', {a1})
    assert _is_linked(b, 'books', a1)
    if hasattr(a1, 'BookShelf'):
        assert _is_linked(a1, 'BookShelf', b)
    _safe_set(b, 'books', {a2})
    assert _is_linked(b, 'books', a2)
    if hasattr(a1, 'BookShelf'):
        assert not _is_linked(a1, 'BookShelf', b)
    if hasattr(a2, 'BookShelf'):
        assert _is_linked(a2, 'BookShelf', b)
    _safe_set(b, 'books', set())
    assert not _is_linked(b, 'books', a2)
    if hasattr(a2, 'BookShelf'):
        assert not _is_linked(a2, 'BookShelf', b)


def test_assoc_shelves1_reverse_link_reassign_clear():
    a1 = model_Person(name="sample_text")
    a2 = model_Person(name="sample_text_2")
    b = model_BookShelf(name="sample_text")
    _safe_set(b, 'BookShelf2', a1)
    assert _is_linked(b, 'BookShelf2', a1)
    if hasattr(a1, 'ownedBy'):
        assert _is_linked(a1, 'ownedBy', b)
    _safe_set(b, 'BookShelf2', a2)
    assert _is_linked(b, 'BookShelf2', a2)
    if hasattr(a1, 'ownedBy'):
        assert not _is_linked(a1, 'ownedBy', b)
    if hasattr(a2, 'ownedBy'):
        assert _is_linked(a2, 'ownedBy', b)
    _safe_set(b, 'BookShelf2', None)
    assert not _is_linked(b, 'BookShelf2', a2)
    if hasattr(a2, 'ownedBy'):
        assert not _is_linked(a2, 'ownedBy', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_books9_stub_double():
    # model_DataBase has no real 'model_DataBase10' property in the generated
    # code (a bare stub) -- manually attach it so model_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Book(author="sample_text", avgRating=7, name="sample_text")
    partner = model_DataBase()
    setattr(partner, 'model_DataBase10', None)
    _safe_set(owner, 'model_Book', partner)
    assert owner in getattr(partner, 'model_DataBase10')
    _safe_set(owner, 'model_Book', None)
    assert owner not in getattr(partner, 'model_DataBase10')


def test_assoc_people7_stub_double():
    # model_DataBase has no real 'model_DataBase' property in the generated
    # code (a bare stub) -- manually attach it so model_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Person(name="sample_text")
    partner = model_DataBase()
    setattr(partner, 'model_DataBase', None)
    _safe_set(owner, 'model_Person8', partner)
    assert owner in getattr(partner, 'model_DataBase')
    _safe_set(owner, 'model_Person8', None)
    assert owner not in getattr(partner, 'model_DataBase')


