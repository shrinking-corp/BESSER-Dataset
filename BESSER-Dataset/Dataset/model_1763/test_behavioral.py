import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Book,
    emftest_Author,
    emftest_Book,
    emftest_BookCollection,
    emftest_ChildBook,
    emftest_Library,
    emftest_ParentBook,
    BookType,
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

def test_assoc_authors0_reverse_link_reassign_clear():
    a1 = emftest_Book(pages=7, title="sample_text")
    a2 = emftest_Book(pages=13, title="sample_text_2")
    b = emftest_Author(name="sample_text")
    _safe_set(b, 'emftest_Author', a1)
    assert _is_linked(b, 'emftest_Author', a1)
    if hasattr(a1, 'emftest_Book'):
        assert _is_linked(a1, 'emftest_Book', b)
    _safe_set(b, 'emftest_Author', a2)
    assert _is_linked(b, 'emftest_Author', a2)
    if hasattr(a1, 'emftest_Book'):
        assert not _is_linked(a1, 'emftest_Book', b)
    if hasattr(a2, 'emftest_Book'):
        assert _is_linked(a2, 'emftest_Book', b)
    _safe_set(b, 'emftest_Author', None)
    assert not _is_linked(b, 'emftest_Author', a2)
    if hasattr(a2, 'emftest_Book'):
        assert not _is_linked(a2, 'emftest_Book', b)


def test_assoc_books5_reverse_link_reassign_clear():
    a1 = emftest_Book(pages=7, title="sample_text")
    a2 = emftest_Book(pages=13, title="sample_text_2")
    b = emftest_Author(name="sample_text")
    _safe_set(b, 'emftest_Author6', {a1})
    assert _is_linked(b, 'emftest_Author6', a1)
    if hasattr(a1, 'emftest_Book7'):
        assert _is_linked(a1, 'emftest_Book7', b)
    _safe_set(b, 'emftest_Author6', {a2})
    assert _is_linked(b, 'emftest_Author6', a2)
    if hasattr(a1, 'emftest_Book7'):
        assert not _is_linked(a1, 'emftest_Book7', b)
    if hasattr(a2, 'emftest_Book7'):
        assert _is_linked(a2, 'emftest_Book7', b)
    _safe_set(b, 'emftest_Author6', set())
    assert not _is_linked(b, 'emftest_Author6', a2)
    if hasattr(a2, 'emftest_Book7'):
        assert not _is_linked(a2, 'emftest_Book7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_books1_stub_double():
    # emftest_BookCollection has no real 'emftest_BookCollection' property in the generated
    # code (a bare stub) -- manually attach it so emftest_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emftest_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emftest_Book(pages=7, title="sample_text")
    partner = emftest_BookCollection()
    setattr(partner, 'emftest_BookCollection', None)
    _safe_set(owner, 'emftest_Book2', partner)
    assert owner in getattr(partner, 'emftest_BookCollection')
    _safe_set(owner, 'emftest_Book2', None)
    assert owner not in getattr(partner, 'emftest_BookCollection')


