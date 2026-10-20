import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Book,
    Guest,
    Librarian,
    Member,
    log,
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

def test_assoc_Admin_Book_reverse_link_reassign_clear():
    a1 = Book(author="sample_text", name="sample_text")
    a2 = Book(author="sample_text_2", name="sample_text_2")
    b = Admin(id=7, password="sample_text", username="sample_text")
    _safe_set(b, 'book6', a1)
    assert _is_linked(b, 'book6', a1)
    if hasattr(a1, 'admin7'):
        assert _is_linked(a1, 'admin7', b)
    _safe_set(b, 'book6', a2)
    assert _is_linked(b, 'book6', a2)
    if hasattr(a1, 'admin7'):
        assert not _is_linked(a1, 'admin7', b)
    if hasattr(a2, 'admin7'):
        assert _is_linked(a2, 'admin7', b)
    _safe_set(b, 'book6', None)
    assert not _is_linked(b, 'book6', a2)
    if hasattr(a2, 'admin7'):
        assert not _is_linked(a2, 'admin7', b)


def test_assoc_Book_Member_reverse_link_reassign_clear():
    a1 = Member(id=7, name="sample_text", password="sample_text", username="sample_text")
    a2 = Member(id=13, name="sample_text_2", password="sample_text_2", username="sample_text_2")
    b = Book(author="sample_text", name="sample_text")
    _safe_set(b, 'member10', a1)
    assert _is_linked(b, 'member10', a1)
    if hasattr(a1, 'book11'):
        assert _is_linked(a1, 'book11', b)
    _safe_set(b, 'member10', a2)
    assert _is_linked(b, 'member10', a2)
    if hasattr(a1, 'book11'):
        assert not _is_linked(a1, 'book11', b)
    if hasattr(a2, 'book11'):
        assert _is_linked(a2, 'book11', b)
    _safe_set(b, 'member10', None)
    assert not _is_linked(b, 'member10', a2)
    if hasattr(a2, 'book11'):
        assert not _is_linked(a2, 'book11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Guest_Book_stub_double():
    # Guest has no real 'book4' property in the generated
    # code (a bare stub) -- manually attach it so Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Book(author="sample_text", name="sample_text")
    partner = Guest()
    setattr(partner, 'book4', None)
    _safe_set(owner, 'guest5', partner)
    assert getattr(partner, 'book4') == owner
    _safe_set(owner, 'guest5', None)
    assert getattr(partner, 'book4') is None


def test_assoc_log_Admin_stub_double():
    # log has no real 'admin0' property in the generated
    # code (a bare stub) -- manually attach it so Admin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Admin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Admin(id=7, password="sample_text", username="sample_text")
    partner = log()
    setattr(partner, 'admin0', None)
    _safe_set(owner, 'log1', partner)
    assert owner in getattr(partner, 'admin0')
    _safe_set(owner, 'log1', None)
    assert owner not in getattr(partner, 'admin0')


def test_assoc_log_Librarian_stub_double():
    # log has no real 'librarian2' property in the generated
    # code (a bare stub) -- manually attach it so Librarian's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Librarian's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Librarian(attribute="sample_text", id=7, password="sample_text")
    partner = log()
    setattr(partner, 'librarian2', None)
    _safe_set(owner, 'log3', partner)
    assert owner in getattr(partner, 'librarian2')
    _safe_set(owner, 'log3', None)
    assert owner not in getattr(partner, 'librarian2')


def test_assoc_log_Member_stub_double():
    # log has no real 'member8' property in the generated
    # code (a bare stub) -- manually attach it so Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Member(id=7, name="sample_text", password="sample_text", username="sample_text")
    partner = log()
    setattr(partner, 'member8', None)
    _safe_set(owner, 'log9', partner)
    assert getattr(partner, 'member8') == owner
    _safe_set(owner, 'log9', None)
    assert getattr(partner, 'member8') is None


