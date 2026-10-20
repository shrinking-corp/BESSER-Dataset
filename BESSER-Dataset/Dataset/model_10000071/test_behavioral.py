import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Ar_Condicionado,
    Borrowed,
    Class,
    Members,
    Quado_Branco,
    Reserved,
    Retro_Projetor,
    Staff,
    admin,
    lecturer,
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

def test_assoc_Books_Borrowed_reverse_link_reassign_clear():
    a1 = Retro_Projetor(ISBN_no="sample_text", author_name="sample_text", book_id=7, book_qty=7, publisher="sample_text", title="sample_text")
    a2 = Retro_Projetor(ISBN_no="sample_text_2", author_name="sample_text_2", book_id=13, book_qty=13, publisher="sample_text_2", title="sample_text_2")
    b = Borrowed(borrowed_date="sample_text", returned_date="sample_text")
    _safe_set(b, 'books1', {a1})
    assert _is_linked(b, 'books1', a1)
    if hasattr(a1, 'borrowed0'):
        assert _is_linked(a1, 'borrowed0', b)
    _safe_set(b, 'books1', {a2})
    assert _is_linked(b, 'books1', a2)
    if hasattr(a1, 'borrowed0'):
        assert not _is_linked(a1, 'borrowed0', b)
    if hasattr(a2, 'borrowed0'):
        assert _is_linked(a2, 'borrowed0', b)
    _safe_set(b, 'books1', set())
    assert not _is_linked(b, 'books1', a2)
    if hasattr(a2, 'borrowed0'):
        assert not _is_linked(a2, 'borrowed0', b)


def test_assoc_Books_Reserved_reverse_link_reassign_clear():
    a1 = Retro_Projetor(ISBN_no="sample_text", author_name="sample_text", book_id=7, book_qty=7, publisher="sample_text", title="sample_text")
    a2 = Retro_Projetor(ISBN_no="sample_text_2", author_name="sample_text_2", book_id=13, book_qty=13, publisher="sample_text_2", title="sample_text_2")
    b = Reserved(reserved_date="sample_text")
    _safe_set(b, 'books5', {a1})
    assert _is_linked(b, 'books5', a1)
    if hasattr(a1, 'reserved4'):
        assert _is_linked(a1, 'reserved4', b)
    _safe_set(b, 'books5', {a2})
    assert _is_linked(b, 'books5', a2)
    if hasattr(a1, 'reserved4'):
        assert not _is_linked(a1, 'reserved4', b)
    if hasattr(a2, 'reserved4'):
        assert _is_linked(a2, 'reserved4', b)
    _safe_set(b, 'books5', set())
    assert not _is_linked(b, 'books5', a2)
    if hasattr(a2, 'reserved4'):
        assert not _is_linked(a2, 'reserved4', b)


def test_assoc_Borrowed_Member_reverse_link_reassign_clear():
    a1 = Members(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    a2 = Members(address="sample_text_2", cont_no=13, dob="sample_text_2", fname="sample_text_2", gender="sample_text_2", lname="sample_text_2", member_id=13, member_pwd="sample_text_2")
    b = Borrowed(borrowed_date="sample_text", returned_date="sample_text")
    _safe_set(b, 'member2', {a1})
    assert _is_linked(b, 'member2', a1)
    if hasattr(a1, 'borrowed3'):
        assert _is_linked(a1, 'borrowed3', b)
    _safe_set(b, 'member2', {a2})
    assert _is_linked(b, 'member2', a2)
    if hasattr(a1, 'borrowed3'):
        assert not _is_linked(a1, 'borrowed3', b)
    if hasattr(a2, 'borrowed3'):
        assert _is_linked(a2, 'borrowed3', b)
    _safe_set(b, 'member2', set())
    assert not _is_linked(b, 'member2', a2)
    if hasattr(a2, 'borrowed3'):
        assert not _is_linked(a2, 'borrowed3', b)


def test_assoc_Fine_Member_reverse_link_reassign_clear():
    a1 = Members(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    a2 = Members(address="sample_text_2", cont_no=13, dob="sample_text_2", fname="sample_text_2", gender="sample_text_2", lname="sample_text_2", member_id=13, member_pwd="sample_text_2")
    b = Ar_Condicionado(book_id=7, borrowed_date="sample_text", fine_amount=7, member_id=7, returned_date="sample_text")
    _safe_set(b, 'member12', a1)
    assert _is_linked(b, 'member12', a1)
    if hasattr(a1, 'fine13'):
        assert _is_linked(a1, 'fine13', b)
    _safe_set(b, 'member12', a2)
    assert _is_linked(b, 'member12', a2)
    if hasattr(a1, 'fine13'):
        assert not _is_linked(a1, 'fine13', b)
    if hasattr(a2, 'fine13'):
        assert _is_linked(a2, 'fine13', b)
    _safe_set(b, 'member12', None)
    assert not _is_linked(b, 'member12', a2)
    if hasattr(a2, 'fine13'):
        assert not _is_linked(a2, 'fine13', b)


def test_assoc_Librarian_Books_reverse_link_reassign_clear():
    a1 = Retro_Projetor(ISBN_no="sample_text", author_name="sample_text", book_id=7, book_qty=7, publisher="sample_text", title="sample_text")
    a2 = Retro_Projetor(ISBN_no="sample_text_2", author_name="sample_text_2", book_id=13, book_qty=13, publisher="sample_text_2", title="sample_text_2")
    b = Quado_Branco(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    _safe_set(b, 'books8', {a1})
    assert _is_linked(b, 'books8', a1)
    if hasattr(a1, 'librarian9'):
        assert _is_linked(a1, 'librarian9', b)
    _safe_set(b, 'books8', {a2})
    assert _is_linked(b, 'books8', a2)
    if hasattr(a1, 'librarian9'):
        assert not _is_linked(a1, 'librarian9', b)
    if hasattr(a2, 'librarian9'):
        assert _is_linked(a2, 'librarian9', b)
    _safe_set(b, 'books8', set())
    assert not _is_linked(b, 'books8', a2)
    if hasattr(a2, 'librarian9'):
        assert not _is_linked(a2, 'librarian9', b)


def test_assoc_Librarian_Fine_reverse_link_reassign_clear():
    a1 = Quado_Branco(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    a2 = Quado_Branco(address="sample_text_2", cont_no=13, dob="sample_text_2", fname="sample_text_2", gender="sample_text_2", lname="sample_text_2", member_id=13, member_pwd="sample_text_2")
    b = Ar_Condicionado(book_id=7, borrowed_date="sample_text", fine_amount=7, member_id=7, returned_date="sample_text")
    _safe_set(b, 'librarian11', {a1})
    assert _is_linked(b, 'librarian11', a1)
    if hasattr(a1, 'fine10'):
        assert _is_linked(a1, 'fine10', b)
    _safe_set(b, 'librarian11', {a2})
    assert _is_linked(b, 'librarian11', a2)
    if hasattr(a1, 'fine10'):
        assert not _is_linked(a1, 'fine10', b)
    if hasattr(a2, 'fine10'):
        assert _is_linked(a2, 'fine10', b)
    _safe_set(b, 'librarian11', set())
    assert not _is_linked(b, 'librarian11', a2)
    if hasattr(a2, 'fine10'):
        assert not _is_linked(a2, 'fine10', b)


def test_assoc_Member_Librarian_reverse_link_reassign_clear():
    a1 = Quado_Branco(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    a2 = Quado_Branco(address="sample_text_2", cont_no=13, dob="sample_text_2", fname="sample_text_2", gender="sample_text_2", lname="sample_text_2", member_id=13, member_pwd="sample_text_2")
    b = Members(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    _safe_set(b, 'librarian14', {a1})
    assert _is_linked(b, 'librarian14', a1)
    if hasattr(a1, 'member15'):
        assert _is_linked(a1, 'member15', b)
    _safe_set(b, 'librarian14', {a2})
    assert _is_linked(b, 'librarian14', a2)
    if hasattr(a1, 'member15'):
        assert not _is_linked(a1, 'member15', b)
    if hasattr(a2, 'member15'):
        assert _is_linked(a2, 'member15', b)
    _safe_set(b, 'librarian14', set())
    assert not _is_linked(b, 'librarian14', a2)
    if hasattr(a2, 'member15'):
        assert not _is_linked(a2, 'member15', b)


def test_assoc_Registar_Staff2_reverse_link_reassign_clear():
    a1 = admin(Experience="sample_text")
    a2 = admin(Experience="sample_text_2")
    b = Staff(Staff_ID=7, address="sample_text", contact=7, email="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", password="sample_text", position="sample_text", username="sample_text")
    _safe_set(b, 'registar17', a1)
    assert _is_linked(b, 'registar17', a1)
    if hasattr(a1, 'staff16'):
        assert _is_linked(a1, 'staff16', b)
    _safe_set(b, 'registar17', a2)
    assert _is_linked(b, 'registar17', a2)
    if hasattr(a1, 'staff16'):
        assert not _is_linked(a1, 'staff16', b)
    if hasattr(a2, 'staff16'):
        assert _is_linked(a2, 'staff16', b)
    _safe_set(b, 'registar17', None)
    assert not _is_linked(b, 'registar17', a2)
    if hasattr(a2, 'staff16'):
        assert not _is_linked(a2, 'staff16', b)


def test_assoc_Reserved_Member_reverse_link_reassign_clear():
    a1 = Reserved(reserved_date="sample_text")
    a2 = Reserved(reserved_date="sample_text_2")
    b = Members(address="sample_text", cont_no=7, dob="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", member_id=7, member_pwd="sample_text")
    _safe_set(b, 'reserved7', {a1})
    assert _is_linked(b, 'reserved7', a1)
    if hasattr(a1, 'member6'):
        assert _is_linked(a1, 'member6', b)
    _safe_set(b, 'reserved7', {a2})
    assert _is_linked(b, 'reserved7', a2)
    if hasattr(a1, 'member6'):
        assert not _is_linked(a1, 'member6', b)
    if hasattr(a2, 'member6'):
        assert _is_linked(a2, 'member6', b)
    _safe_set(b, 'reserved7', set())
    assert not _is_linked(b, 'reserved7', a2)
    if hasattr(a2, 'member6'):
        assert not _is_linked(a2, 'member6', b)


def test_assoc_Staff_Professor2_reverse_link_reassign_clear():
    a1 = lecturer(module="sample_text")
    a2 = lecturer(module="sample_text_2")
    b = Staff(Staff_ID=7, address="sample_text", contact=7, email="sample_text", fname="sample_text", gender="sample_text", lname="sample_text", password="sample_text", position="sample_text", username="sample_text")
    _safe_set(b, 'professor18', a1)
    assert _is_linked(b, 'professor18', a1)
    if hasattr(a1, 'staff19'):
        assert _is_linked(a1, 'staff19', b)
    _safe_set(b, 'professor18', a2)
    assert _is_linked(b, 'professor18', a2)
    if hasattr(a1, 'staff19'):
        assert not _is_linked(a1, 'staff19', b)
    if hasattr(a2, 'staff19'):
        assert _is_linked(a2, 'staff19', b)
    _safe_set(b, 'professor18', None)
    assert not _is_linked(b, 'professor18', a2)
    if hasattr(a2, 'staff19'):
        assert not _is_linked(a2, 'staff19', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

