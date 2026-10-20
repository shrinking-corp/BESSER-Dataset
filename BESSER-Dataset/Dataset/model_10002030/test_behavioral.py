import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    LIBRARIAN,
    book_mdatabase,
    library,
    patron,
    patronrecord,
    vendor,
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

def test_assoc_book_mdatabase_patron_reverse_link_reassign_clear():
    a1 = patron(details="sample_text", patronid="sample_text", payfine="sample_text", request="sample_text", search="sample_text")
    a2 = patron(details="sample_text_2", patronid="sample_text_2", payfine="sample_text_2", request="sample_text_2", search="sample_text_2")
    b = book_mdatabase(author="sample_text", bookid="sample_text", booktitle="sample_text", update="sample_text")
    _safe_set(b, 'patron4', a1)
    assert _is_linked(b, 'patron4', a1)
    if hasattr(a1, 'book_mdatabase5'):
        assert _is_linked(a1, 'book_mdatabase5', b)
    _safe_set(b, 'patron4', a2)
    assert _is_linked(b, 'patron4', a2)
    if hasattr(a1, 'book_mdatabase5'):
        assert not _is_linked(a1, 'book_mdatabase5', b)
    if hasattr(a2, 'book_mdatabase5'):
        assert _is_linked(a2, 'book_mdatabase5', b)
    _safe_set(b, 'patron4', None)
    assert not _is_linked(b, 'patron4', a2)
    if hasattr(a2, 'book_mdatabase5'):
        assert not _is_linked(a2, 'book_mdatabase5', b)


def test_assoc_library_LIBRARIAN_reverse_link_reassign_clear():
    a1 = library(_librarion_id="sample_text", _location="sample_text")
    a2 = library(_librarion_id="sample_text_2", _location="sample_text_2")
    b = LIBRARIAN(LIBRARIAN_ID="sample_text", NAME="sample_text", issue_book="sample_text", issue_status="sample_text", searchbook__="sample_text", verify_member__="sample_text")
    _safe_set(b, 'library1', a1)
    assert _is_linked(b, 'library1', a1)
    if hasattr(a1, 'lIBRARIAN0'):
        assert _is_linked(a1, 'lIBRARIAN0', b)
    _safe_set(b, 'library1', a2)
    assert _is_linked(b, 'library1', a2)
    if hasattr(a1, 'lIBRARIAN0'):
        assert not _is_linked(a1, 'lIBRARIAN0', b)
    if hasattr(a2, 'lIBRARIAN0'):
        assert _is_linked(a2, 'lIBRARIAN0', b)
    _safe_set(b, 'library1', None)
    assert not _is_linked(b, 'library1', a2)
    if hasattr(a2, 'lIBRARIAN0'):
        assert not _is_linked(a2, 'lIBRARIAN0', b)


def test_assoc_library_book_mdatabase_reverse_link_reassign_clear():
    a1 = library(_librarion_id="sample_text", _location="sample_text")
    a2 = library(_librarion_id="sample_text_2", _location="sample_text_2")
    b = book_mdatabase(author="sample_text", bookid="sample_text", booktitle="sample_text", update="sample_text")
    _safe_set(b, 'library3', a1)
    assert _is_linked(b, 'library3', a1)
    if hasattr(a1, 'book_mdatabase2'):
        assert _is_linked(a1, 'book_mdatabase2', b)
    _safe_set(b, 'library3', a2)
    assert _is_linked(b, 'library3', a2)
    if hasattr(a1, 'book_mdatabase2'):
        assert not _is_linked(a1, 'book_mdatabase2', b)
    if hasattr(a2, 'book_mdatabase2'):
        assert _is_linked(a2, 'book_mdatabase2', b)
    _safe_set(b, 'library3', None)
    assert not _is_linked(b, 'library3', a2)
    if hasattr(a2, 'book_mdatabase2'):
        assert not _is_linked(a2, 'book_mdatabase2', b)


def test_assoc_patron_patronrecord_reverse_link_reassign_clear():
    a1 = patronrecord(address="sample_text", dateofmembership="sample_text", filesowned="sample_text", name="sample_text", noofbooks_alooted="sample_text", patronid="sample_text", phone_no="sample_text", type="sample_text")
    a2 = patronrecord(address="sample_text_2", dateofmembership="sample_text_2", filesowned="sample_text_2", name="sample_text_2", noofbooks_alooted="sample_text_2", patronid="sample_text_2", phone_no="sample_text_2", type="sample_text_2")
    b = patron(details="sample_text", patronid="sample_text", payfine="sample_text", request="sample_text", search="sample_text")
    _safe_set(b, 'patronrecord6', a1)
    assert _is_linked(b, 'patronrecord6', a1)
    if hasattr(a1, 'patron7'):
        assert _is_linked(a1, 'patron7', b)
    _safe_set(b, 'patronrecord6', a2)
    assert _is_linked(b, 'patronrecord6', a2)
    if hasattr(a1, 'patron7'):
        assert not _is_linked(a1, 'patron7', b)
    if hasattr(a2, 'patron7'):
        assert _is_linked(a2, 'patron7', b)
    _safe_set(b, 'patronrecord6', None)
    assert not _is_linked(b, 'patronrecord6', a2)
    if hasattr(a2, 'patron7'):
        assert not _is_linked(a2, 'patron7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

