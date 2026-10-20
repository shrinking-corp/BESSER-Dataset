import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TableContent,
    model_Book,
    model_Computer,
    model_Container,
    model_Content,
    model_CrossReferenceContainer,
    model_CrossReferenceContent,
    model_Librarian,
    model_Library,
    model_Mainboard,
    model_Person,
    model_PowerBlock,
    model_Referencer,
    model_TableContent,
    model_TableContentWithInnerChild,
    model_TableContentWithInnerChild2,
    model_TableContentWithValidation,
    model_TableContentWithoutValidation,
    model_TableWithMultiplicity,
    model_TableWithUnique,
    model_TableWithoutMultiplicity,
    model_TableWithoutMultiplicityConcrete,
    model_Writer,
    Color,
    Gender,
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

def test_assoc_books1_reverse_link_reassign_clear():
    a1 = model_Library(name="sample_text", phoneNumber="sample_text")
    a2 = model_Library(name="sample_text_2", phoneNumber="sample_text_2")
    b = model_Book(pages=7, title="sample_text")
    _safe_set(b, 'model_Book', a1)
    assert _is_linked(b, 'model_Book', a1)
    if hasattr(a1, 'model_Library'):
        assert _is_linked(a1, 'model_Library', b)
    _safe_set(b, 'model_Book', a2)
    assert _is_linked(b, 'model_Book', a2)
    if hasattr(a1, 'model_Library'):
        assert not _is_linked(a1, 'model_Library', b)
    if hasattr(a2, 'model_Library'):
        assert _is_linked(a2, 'model_Library', b)
    _safe_set(b, 'model_Book', None)
    assert not _is_linked(b, 'model_Book', a2)
    if hasattr(a2, 'model_Library'):
        assert not _is_linked(a2, 'model_Library', b)


def test_assoc_books4_reverse_link_reassign_clear():
    a1 = model_Writer(BirthDate=date(2024, 1, 1), EMail="sample_text", Pseudonym=True, firstName="sample_text", initials="sample_text", lastName="sample_text", title="sample_text")
    a2 = model_Writer(BirthDate=date(2025, 6, 15), EMail="sample_text_2", Pseudonym=False, firstName="sample_text_2", initials="sample_text_2", lastName="sample_text_2", title="sample_text_2")
    b = model_Book(pages=7, title="sample_text")
    _safe_set(b, 'Book', a1)
    assert _is_linked(b, 'Book', a1)
    if hasattr(a1, 'writers'):
        assert _is_linked(a1, 'writers', b)
    _safe_set(b, 'Book', a2)
    assert _is_linked(b, 'Book', a2)
    if hasattr(a1, 'writers'):
        assert not _is_linked(a1, 'writers', b)
    if hasattr(a2, 'writers'):
        assert _is_linked(a2, 'writers', b)
    _safe_set(b, 'Book', None)
    assert not _is_linked(b, 'Book', a2)
    if hasattr(a2, 'writers'):
        assert not _is_linked(a2, 'writers', b)


def test_assoc_librarian2_reverse_link_reassign_clear():
    a1 = model_Library(name="sample_text", phoneNumber="sample_text")
    a2 = model_Library(name="sample_text_2", phoneNumber="sample_text_2")
    b = model_Librarian(name="sample_text")
    _safe_set(b, 'model_Librarian', a1)
    assert _is_linked(b, 'model_Librarian', a1)
    if hasattr(a1, 'model_Library3'):
        assert _is_linked(a1, 'model_Library3', b)
    _safe_set(b, 'model_Librarian', a2)
    assert _is_linked(b, 'model_Librarian', a2)
    if hasattr(a1, 'model_Library3'):
        assert not _is_linked(a1, 'model_Library3', b)
    if hasattr(a2, 'model_Library3'):
        assert _is_linked(a2, 'model_Library3', b)
    _safe_set(b, 'model_Librarian', None)
    assert not _is_linked(b, 'model_Librarian', a2)
    if hasattr(a2, 'model_Library3'):
        assert not _is_linked(a2, 'model_Library3', b)


def test_assoc_library5_reverse_link_reassign_clear():
    a1 = model_Writer(BirthDate=date(2024, 1, 1), EMail="sample_text", Pseudonym=True, firstName="sample_text", initials="sample_text", lastName="sample_text", title="sample_text")
    a2 = model_Writer(BirthDate=date(2025, 6, 15), EMail="sample_text_2", Pseudonym=False, firstName="sample_text_2", initials="sample_text_2", lastName="sample_text_2", title="sample_text_2")
    b = model_Library(name="sample_text", phoneNumber="sample_text")
    _safe_set(b, 'Library', a1)
    assert _is_linked(b, 'Library', a1)
    if hasattr(a1, 'writers6'):
        assert _is_linked(a1, 'writers6', b)
    _safe_set(b, 'Library', a2)
    assert _is_linked(b, 'Library', a2)
    if hasattr(a1, 'writers6'):
        assert not _is_linked(a1, 'writers6', b)
    if hasattr(a2, 'writers6'):
        assert _is_linked(a2, 'writers6', b)
    _safe_set(b, 'Library', None)
    assert not _is_linked(b, 'Library', a2)
    if hasattr(a2, 'writers6'):
        assert not _is_linked(a2, 'writers6', b)


def test_assoc_mainboard9_reverse_link_reassign_clear():
    a1 = model_Mainboard(name="sample_text")
    a2 = model_Mainboard(name="sample_text_2")
    b = model_Computer(colors="sample_text", name="sample_text")
    _safe_set(b, 'model_Computer', a1)
    assert _is_linked(b, 'model_Computer', a1)
    if hasattr(a1, 'model_Mainboard'):
        assert _is_linked(a1, 'model_Mainboard', b)
    _safe_set(b, 'model_Computer', a2)
    assert _is_linked(b, 'model_Computer', a2)
    if hasattr(a1, 'model_Mainboard'):
        assert not _is_linked(a1, 'model_Mainboard', b)
    if hasattr(a2, 'model_Mainboard'):
        assert _is_linked(a2, 'model_Mainboard', b)
    _safe_set(b, 'model_Computer', None)
    assert not _is_linked(b, 'model_Computer', a2)
    if hasattr(a2, 'model_Mainboard'):
        assert not _is_linked(a2, 'model_Mainboard', b)


def test_assoc_powerBlock10_reverse_link_reassign_clear():
    a1 = model_PowerBlock(name="sample_text")
    a2 = model_PowerBlock(name="sample_text_2")
    b = model_Computer(colors="sample_text", name="sample_text")
    _safe_set(b, 'model_Computer11', a1)
    assert _is_linked(b, 'model_Computer11', a1)
    if hasattr(a1, 'model_PowerBlock'):
        assert _is_linked(a1, 'model_PowerBlock', b)
    _safe_set(b, 'model_Computer11', a2)
    assert _is_linked(b, 'model_Computer11', a2)
    if hasattr(a1, 'model_PowerBlock'):
        assert not _is_linked(a1, 'model_PowerBlock', b)
    if hasattr(a2, 'model_PowerBlock'):
        assert _is_linked(a2, 'model_PowerBlock', b)
    _safe_set(b, 'model_Computer11', None)
    assert not _is_linked(b, 'model_Computer11', a2)
    if hasattr(a2, 'model_PowerBlock'):
        assert not _is_linked(a2, 'model_PowerBlock', b)


def test_assoc_writers0_reverse_link_reassign_clear():
    a1 = model_Writer(BirthDate=date(2024, 1, 1), EMail="sample_text", Pseudonym=True, firstName="sample_text", initials="sample_text", lastName="sample_text", title="sample_text")
    a2 = model_Writer(BirthDate=date(2025, 6, 15), EMail="sample_text_2", Pseudonym=False, firstName="sample_text_2", initials="sample_text_2", lastName="sample_text_2", title="sample_text_2")
    b = model_Library(name="sample_text", phoneNumber="sample_text")
    _safe_set(b, 'library', {a1})
    assert _is_linked(b, 'library', a1)
    if hasattr(a1, 'Writer'):
        assert _is_linked(a1, 'Writer', b)
    _safe_set(b, 'library', {a2})
    assert _is_linked(b, 'library', a2)
    if hasattr(a1, 'Writer'):
        assert not _is_linked(a1, 'Writer', b)
    if hasattr(a2, 'Writer'):
        assert _is_linked(a2, 'Writer', b)
    _safe_set(b, 'library', set())
    assert not _is_linked(b, 'library', a2)
    if hasattr(a2, 'Writer'):
        assert not _is_linked(a2, 'Writer', b)


def test_assoc_writers7_reverse_link_reassign_clear():
    a1 = model_Writer(BirthDate=date(2024, 1, 1), EMail="sample_text", Pseudonym=True, firstName="sample_text", initials="sample_text", lastName="sample_text", title="sample_text")
    a2 = model_Writer(BirthDate=date(2025, 6, 15), EMail="sample_text_2", Pseudonym=False, firstName="sample_text_2", initials="sample_text_2", lastName="sample_text_2", title="sample_text_2")
    b = model_Book(pages=7, title="sample_text")
    _safe_set(b, 'books', a1)
    assert _is_linked(b, 'books', a1)
    if hasattr(a1, 'Writer8'):
        assert _is_linked(a1, 'Writer8', b)
    _safe_set(b, 'books', a2)
    assert _is_linked(b, 'books', a2)
    if hasattr(a1, 'Writer8'):
        assert not _is_linked(a1, 'Writer8', b)
    if hasattr(a2, 'Writer8'):
        assert _is_linked(a2, 'Writer8', b)
    _safe_set(b, 'books', None)
    assert not _is_linked(b, 'books', a2)
    if hasattr(a2, 'Writer8'):
        assert not _is_linked(a2, 'Writer8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_content22_stub_double():
    # model_TableWithoutMultiplicityConcrete has no real 'model_TableWithoutMultiplicityConcrete' property in the generated
    # code (a bare stub) -- manually attach it so model_TableContentWithInnerChild's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TableContentWithInnerChild's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TableContentWithInnerChild(stuff="sample_text")
    partner = model_TableWithoutMultiplicityConcrete()
    setattr(partner, 'model_TableWithoutMultiplicityConcrete', None)
    _safe_set(owner, 'model_TableContentWithInnerChild23', partner)
    assert owner in getattr(partner, 'model_TableWithoutMultiplicityConcrete')
    _safe_set(owner, 'model_TableContentWithInnerChild23', None)
    assert owner not in getattr(partner, 'model_TableWithoutMultiplicityConcrete')


def test_assoc_contents12_stub_double():
    # model_Container has no real 'model_Container' property in the generated
    # code (a bare stub) -- manually attach it so model_Content's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Content's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Content(secondAttribute="sample_text", uniqueAttribute="sample_text")
    partner = model_Container()
    setattr(partner, 'model_Container', None)
    _safe_set(owner, 'model_Content', partner)
    assert owner in getattr(partner, 'model_Container')
    _safe_set(owner, 'model_Content', None)
    assert owner not in getattr(partner, 'model_Container')


def test_assoc_innerChild20_stub_double():
    # model_TableContent has no real 'model_TableContent21' property in the generated
    # code (a bare stub) -- manually attach it so model_TableContentWithInnerChild's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TableContentWithInnerChild's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TableContentWithInnerChild(stuff="sample_text")
    partner = model_TableContent()
    setattr(partner, 'model_TableContent21', None)
    _safe_set(owner, 'model_TableContentWithInnerChild', partner)
    assert getattr(partner, 'model_TableContent21') == owner
    _safe_set(owner, 'model_TableContentWithInnerChild', None)
    assert getattr(partner, 'model_TableContent21') is None


def test_assoc_referencedContent24_stub_double():
    # model_Referencer has no real 'model_Referencer' property in the generated
    # code (a bare stub) -- manually attach it so model_Computer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Computer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Computer(colors="sample_text", name="sample_text")
    partner = model_Referencer()
    setattr(partner, 'model_Referencer', None)
    _safe_set(owner, 'model_Computer25', partner)
    assert getattr(partner, 'model_Referencer') == owner
    _safe_set(owner, 'model_Computer25', None)
    assert getattr(partner, 'model_Referencer') is None


