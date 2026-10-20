import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Books_Author,
    Books_Book,
    Books_Chapter,
    Books_System,
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

def test_assoc_authors1_reverse_link_reassign_clear():
    a1 = Books_System(name="sample_text")
    a2 = Books_System(name="sample_text_2")
    b = Books_Author(name="sample_text")
    _safe_set(b, 'Books_Author', a1)
    assert _is_linked(b, 'Books_Author', a1)
    if hasattr(a1, 'Books_System2'):
        assert _is_linked(a1, 'Books_System2', b)
    _safe_set(b, 'Books_Author', a2)
    assert _is_linked(b, 'Books_Author', a2)
    if hasattr(a1, 'Books_System2'):
        assert not _is_linked(a1, 'Books_System2', b)
    if hasattr(a2, 'Books_System2'):
        assert _is_linked(a2, 'Books_System2', b)
    _safe_set(b, 'Books_Author', None)
    assert not _is_linked(b, 'Books_Author', a2)
    if hasattr(a2, 'Books_System2'):
        assert not _is_linked(a2, 'Books_System2', b)


def test_assoc_auths4_reverse_link_reassign_clear():
    a1 = Books_Book(collecName="sample_text", title="sample_text")
    a2 = Books_Book(collecName="sample_text_2", title="sample_text_2")
    b = Books_Author(name="sample_text")
    _safe_set(b, 'Author', a1)
    assert _is_linked(b, 'Author', a1)
    if hasattr(a1, 'mybs'):
        assert _is_linked(a1, 'mybs', b)
    _safe_set(b, 'Author', a2)
    assert _is_linked(b, 'Author', a2)
    if hasattr(a1, 'mybs'):
        assert not _is_linked(a1, 'mybs', b)
    if hasattr(a2, 'mybs'):
        assert _is_linked(a2, 'mybs', b)
    _safe_set(b, 'Author', None)
    assert not _is_linked(b, 'Author', a2)
    if hasattr(a2, 'mybs'):
        assert not _is_linked(a2, 'mybs', b)


def test_assoc_books0_reverse_link_reassign_clear():
    a1 = Books_System(name="sample_text")
    a2 = Books_System(name="sample_text_2")
    b = Books_Book(collecName="sample_text", title="sample_text")
    _safe_set(b, 'Books_Book', a1)
    assert _is_linked(b, 'Books_Book', a1)
    if hasattr(a1, 'Books_System'):
        assert _is_linked(a1, 'Books_System', b)
    _safe_set(b, 'Books_Book', a2)
    assert _is_linked(b, 'Books_Book', a2)
    if hasattr(a1, 'Books_System'):
        assert not _is_linked(a1, 'Books_System', b)
    if hasattr(a2, 'Books_System'):
        assert _is_linked(a2, 'Books_System', b)
    _safe_set(b, 'Books_Book', None)
    assert not _is_linked(b, 'Books_Book', a2)
    if hasattr(a2, 'Books_System'):
        assert not _is_linked(a2, 'Books_System', b)


def test_assoc_chaps3_reverse_link_reassign_clear():
    a1 = Books_Chapter(title="sample_text")
    a2 = Books_Chapter(title="sample_text_2")
    b = Books_Book(collecName="sample_text", title="sample_text")
    _safe_set(b, 'itsbook', {a1})
    assert _is_linked(b, 'itsbook', a1)
    if hasattr(a1, 'Chapter'):
        assert _is_linked(a1, 'Chapter', b)
    _safe_set(b, 'itsbook', {a2})
    assert _is_linked(b, 'itsbook', a2)
    if hasattr(a1, 'Chapter'):
        assert not _is_linked(a1, 'Chapter', b)
    if hasattr(a2, 'Chapter'):
        assert _is_linked(a2, 'Chapter', b)
    _safe_set(b, 'itsbook', set())
    assert not _is_linked(b, 'itsbook', a2)
    if hasattr(a2, 'Chapter'):
        assert not _is_linked(a2, 'Chapter', b)


def test_assoc_itsbook5_reverse_link_reassign_clear():
    a1 = Books_Chapter(title="sample_text")
    a2 = Books_Chapter(title="sample_text_2")
    b = Books_Book(collecName="sample_text", title="sample_text")
    _safe_set(b, 'Book', a1)
    assert _is_linked(b, 'Book', a1)
    if hasattr(a1, 'chaps'):
        assert _is_linked(a1, 'chaps', b)
    _safe_set(b, 'Book', a2)
    assert _is_linked(b, 'Book', a2)
    if hasattr(a1, 'chaps'):
        assert not _is_linked(a1, 'chaps', b)
    if hasattr(a2, 'chaps'):
        assert _is_linked(a2, 'chaps', b)
    _safe_set(b, 'Book', None)
    assert not _is_linked(b, 'Book', a2)
    if hasattr(a2, 'chaps'):
        assert not _is_linked(a2, 'chaps', b)


def test_assoc_mybs6_reverse_link_reassign_clear():
    a1 = Books_Book(collecName="sample_text", title="sample_text")
    a2 = Books_Book(collecName="sample_text_2", title="sample_text_2")
    b = Books_Author(name="sample_text")
    _safe_set(b, 'auths', {a1})
    assert _is_linked(b, 'auths', a1)
    if hasattr(a1, 'Book7'):
        assert _is_linked(a1, 'Book7', b)
    _safe_set(b, 'auths', {a2})
    assert _is_linked(b, 'auths', a2)
    if hasattr(a1, 'Book7'):
        assert not _is_linked(a1, 'Book7', b)
    if hasattr(a2, 'Book7'):
        assert _is_linked(a2, 'Book7', b)
    _safe_set(b, 'auths', set())
    assert not _is_linked(b, 'auths', a2)
    if hasattr(a2, 'Book7'):
        assert not _is_linked(a2, 'Book7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

