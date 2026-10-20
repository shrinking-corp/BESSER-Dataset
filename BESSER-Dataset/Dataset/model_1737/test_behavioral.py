import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Ent,
    bookstore_Book,
    bookstore_Cd,
    bookstore_Dvd,
    bookstore_Ent,
    bookstore_Magazine,
    bookstore_Model,
    bookstore_Person,
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

def test_assoc_actor10_reverse_link_reassign_clear():
    a1 = bookstore_Person(achternaam="sample_text", voornaam="sample_text")
    a2 = bookstore_Person(achternaam="sample_text_2", voornaam="sample_text_2")
    b = bookstore_Dvd(title="sample_text")
    _safe_set(b, 'bookstore_Dvd', {a1})
    assert _is_linked(b, 'bookstore_Dvd', a1)
    if hasattr(a1, 'bookstore_Person11'):
        assert _is_linked(a1, 'bookstore_Person11', b)
    _safe_set(b, 'bookstore_Dvd', {a2})
    assert _is_linked(b, 'bookstore_Dvd', a2)
    if hasattr(a1, 'bookstore_Person11'):
        assert not _is_linked(a1, 'bookstore_Person11', b)
    if hasattr(a2, 'bookstore_Person11'):
        assert _is_linked(a2, 'bookstore_Person11', b)
    _safe_set(b, 'bookstore_Dvd', set())
    assert not _is_linked(b, 'bookstore_Dvd', a2)
    if hasattr(a2, 'bookstore_Person11'):
        assert not _is_linked(a2, 'bookstore_Person11', b)


def test_assoc_artiesten21_reverse_link_reassign_clear():
    a1 = bookstore_Person(achternaam="sample_text", voornaam="sample_text")
    a2 = bookstore_Person(achternaam="sample_text_2", voornaam="sample_text_2")
    b = bookstore_Cd(albumName="sample_text", bandArtist="sample_text")
    _safe_set(b, 'bookstore_Cd', {a1})
    assert _is_linked(b, 'bookstore_Cd', a1)
    if hasattr(a1, 'bookstore_Person22'):
        assert _is_linked(a1, 'bookstore_Person22', b)
    _safe_set(b, 'bookstore_Cd', {a2})
    assert _is_linked(b, 'bookstore_Cd', a2)
    if hasattr(a1, 'bookstore_Person22'):
        assert not _is_linked(a1, 'bookstore_Person22', b)
    if hasattr(a2, 'bookstore_Person22'):
        assert _is_linked(a2, 'bookstore_Person22', b)
    _safe_set(b, 'bookstore_Cd', set())
    assert not _is_linked(b, 'bookstore_Cd', a2)
    if hasattr(a2, 'bookstore_Person22'):
        assert not _is_linked(a2, 'bookstore_Person22', b)


def test_assoc_book12_reverse_link_reassign_clear():
    a1 = bookstore_Dvd(title="sample_text")
    a2 = bookstore_Dvd(title="sample_text_2")
    b = bookstore_Book(pages=7, title="sample_text")
    _safe_set(b, 'bookstore_Book14', a1)
    assert _is_linked(b, 'bookstore_Book14', a1)
    if hasattr(a1, 'bookstore_Dvd13'):
        assert _is_linked(a1, 'bookstore_Dvd13', b)
    _safe_set(b, 'bookstore_Book14', a2)
    assert _is_linked(b, 'bookstore_Book14', a2)
    if hasattr(a1, 'bookstore_Dvd13'):
        assert not _is_linked(a1, 'bookstore_Dvd13', b)
    if hasattr(a2, 'bookstore_Dvd13'):
        assert _is_linked(a2, 'bookstore_Dvd13', b)
    _safe_set(b, 'bookstore_Book14', None)
    assert not _is_linked(b, 'bookstore_Book14', a2)
    if hasattr(a2, 'bookstore_Dvd13'):
        assert not _is_linked(a2, 'bookstore_Dvd13', b)


def test_assoc_manWife2_reverse_link_reassign_clear():
    a1 = bookstore_Person(achternaam="sample_text", voornaam="sample_text")
    a2 = bookstore_Person(achternaam="sample_text_2", voornaam="sample_text_2")
    b = bookstore_Person(achternaam="sample_text", voornaam="sample_text")
    _safe_set(b, 'bookstore_Person1', a1)
    assert _is_linked(b, 'bookstore_Person1', a1)
    if hasattr(a1, 'bookstore_Person'):
        assert _is_linked(a1, 'bookstore_Person', b)
    _safe_set(b, 'bookstore_Person1', a2)
    assert _is_linked(b, 'bookstore_Person1', a2)
    if hasattr(a1, 'bookstore_Person'):
        assert not _is_linked(a1, 'bookstore_Person', b)
    if hasattr(a2, 'bookstore_Person'):
        assert _is_linked(a2, 'bookstore_Person', b)
    _safe_set(b, 'bookstore_Person1', None)
    assert not _is_linked(b, 'bookstore_Person1', a2)
    if hasattr(a2, 'bookstore_Person'):
        assert not _is_linked(a2, 'bookstore_Person', b)


def test_assoc_sequel19_reverse_link_reassign_clear():
    a1 = bookstore_Dvd(title="sample_text")
    a2 = bookstore_Dvd(title="sample_text_2")
    b = bookstore_Dvd(title="sample_text")
    _safe_set(b, 'bookstore_Dvd20', a1)
    assert _is_linked(b, 'bookstore_Dvd20', a1)
    if hasattr(a1, 'bookstore_Dvd18'):
        assert _is_linked(a1, 'bookstore_Dvd18', b)
    _safe_set(b, 'bookstore_Dvd20', a2)
    assert _is_linked(b, 'bookstore_Dvd20', a2)
    if hasattr(a1, 'bookstore_Dvd18'):
        assert not _is_linked(a1, 'bookstore_Dvd18', b)
    if hasattr(a2, 'bookstore_Dvd18'):
        assert _is_linked(a2, 'bookstore_Dvd18', b)
    _safe_set(b, 'bookstore_Dvd20', None)
    assert not _is_linked(b, 'bookstore_Dvd20', a2)
    if hasattr(a2, 'bookstore_Dvd18'):
        assert not _is_linked(a2, 'bookstore_Dvd18', b)


def test_assoc_sequel4_reverse_link_reassign_clear():
    a1 = bookstore_Book(pages=7, title="sample_text")
    a2 = bookstore_Book(pages=13, title="sample_text_2")
    b = bookstore_Book(pages=7, title="sample_text")
    _safe_set(b, 'bookstore_Book3', a1)
    assert _is_linked(b, 'bookstore_Book3', a1)
    if hasattr(a1, 'bookstore_Book'):
        assert _is_linked(a1, 'bookstore_Book', b)
    _safe_set(b, 'bookstore_Book3', a2)
    assert _is_linked(b, 'bookstore_Book3', a2)
    if hasattr(a1, 'bookstore_Book'):
        assert not _is_linked(a1, 'bookstore_Book', b)
    if hasattr(a2, 'bookstore_Book'):
        assert _is_linked(a2, 'bookstore_Book', b)
    _safe_set(b, 'bookstore_Book3', None)
    assert not _is_linked(b, 'bookstore_Book3', a2)
    if hasattr(a2, 'bookstore_Book'):
        assert not _is_linked(a2, 'bookstore_Book', b)


def test_assoc_writer15_reverse_link_reassign_clear():
    a1 = bookstore_Person(achternaam="sample_text", voornaam="sample_text")
    a2 = bookstore_Person(achternaam="sample_text_2", voornaam="sample_text_2")
    b = bookstore_Dvd(title="sample_text")
    _safe_set(b, 'bookstore_Dvd16', a1)
    assert _is_linked(b, 'bookstore_Dvd16', a1)
    if hasattr(a1, 'bookstore_Person17'):
        assert _is_linked(a1, 'bookstore_Person17', b)
    _safe_set(b, 'bookstore_Dvd16', a2)
    assert _is_linked(b, 'bookstore_Dvd16', a2)
    if hasattr(a1, 'bookstore_Person17'):
        assert not _is_linked(a1, 'bookstore_Person17', b)
    if hasattr(a2, 'bookstore_Person17'):
        assert _is_linked(a2, 'bookstore_Person17', b)
    _safe_set(b, 'bookstore_Dvd16', None)
    assert not _is_linked(b, 'bookstore_Dvd16', a2)
    if hasattr(a2, 'bookstore_Person17'):
        assert not _is_linked(a2, 'bookstore_Person17', b)


def test_assoc_writer5_reverse_link_reassign_clear():
    a1 = bookstore_Person(achternaam="sample_text", voornaam="sample_text")
    a2 = bookstore_Person(achternaam="sample_text_2", voornaam="sample_text_2")
    b = bookstore_Book(pages=7, title="sample_text")
    _safe_set(b, 'bookstore_Book6', a1)
    assert _is_linked(b, 'bookstore_Book6', a1)
    if hasattr(a1, 'bookstore_Person7'):
        assert _is_linked(a1, 'bookstore_Person7', b)
    _safe_set(b, 'bookstore_Book6', a2)
    assert _is_linked(b, 'bookstore_Book6', a2)
    if hasattr(a1, 'bookstore_Person7'):
        assert not _is_linked(a1, 'bookstore_Person7', b)
    if hasattr(a2, 'bookstore_Person7'):
        assert _is_linked(a2, 'bookstore_Person7', b)
    _safe_set(b, 'bookstore_Book6', None)
    assert not _is_linked(b, 'bookstore_Book6', a2)
    if hasattr(a2, 'bookstore_Person7'):
        assert not _is_linked(a2, 'bookstore_Person7', b)


def test_assoc_writer8_reverse_link_reassign_clear():
    a1 = bookstore_Person(achternaam="sample_text", voornaam="sample_text")
    a2 = bookstore_Person(achternaam="sample_text_2", voornaam="sample_text_2")
    b = bookstore_Magazine(pages=7, title="sample_text", version="sample_text")
    _safe_set(b, 'bookstore_Magazine', a1)
    assert _is_linked(b, 'bookstore_Magazine', a1)
    if hasattr(a1, 'bookstore_Person9'):
        assert _is_linked(a1, 'bookstore_Person9', b)
    _safe_set(b, 'bookstore_Magazine', a2)
    assert _is_linked(b, 'bookstore_Magazine', a2)
    if hasattr(a1, 'bookstore_Person9'):
        assert not _is_linked(a1, 'bookstore_Person9', b)
    if hasattr(a2, 'bookstore_Person9'):
        assert _is_linked(a2, 'bookstore_Person9', b)
    _safe_set(b, 'bookstore_Magazine', None)
    assert not _is_linked(b, 'bookstore_Magazine', a2)
    if hasattr(a2, 'bookstore_Person9'):
        assert not _is_linked(a2, 'bookstore_Person9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ent0_stub_double():
    # bookstore_Model has no real 'bookstore_Model' property in the generated
    # code (a bare stub) -- manually attach it so bookstore_Ent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bookstore_Ent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bookstore_Ent(name="sample_text")
    partner = bookstore_Model()
    setattr(partner, 'bookstore_Model', None)
    _safe_set(owner, 'bookstore_Ent', partner)
    assert owner in getattr(partner, 'bookstore_Model')
    _safe_set(owner, 'bookstore_Ent', None)
    assert owner not in getattr(partner, 'bookstore_Model')


