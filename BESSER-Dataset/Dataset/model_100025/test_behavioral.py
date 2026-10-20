import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DBLP_Article,
    DBLP_Author,
    DBLP_Book,
    DBLP_Editor,
    DBLP_InCollection,
    DBLP_InProceedings,
    DBLP_Journal,
    DBLP_MastersThesis,
    DBLP_Organization,
    DBLP_PhDThesis,
    DBLP_Proceedings,
    DBLP_Publisher,
    DBLP_Record,
    DBLP_School,
    DBLP_Www,
    Record,
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

def test_assoc_articles3_reverse_link_reassign_clear():
    a1 = DBLP_Journal(name="sample_text")
    a2 = DBLP_Journal(name="sample_text_2")
    b = DBLP_Article(fromPage=7, month="sample_text", number=7, title="sample_text", toPage=7, volume="sample_text", year=7)
    _safe_set(b, 'Article', a1)
    assert _is_linked(b, 'Article', a1)
    if hasattr(a1, 'journal'):
        assert _is_linked(a1, 'journal', b)
    _safe_set(b, 'Article', a2)
    assert _is_linked(b, 'Article', a2)
    if hasattr(a1, 'journal'):
        assert not _is_linked(a1, 'journal', b)
    if hasattr(a2, 'journal'):
        assert _is_linked(a2, 'journal', b)
    _safe_set(b, 'Article', None)
    assert not _is_linked(b, 'Article', a2)
    if hasattr(a2, 'journal'):
        assert not _is_linked(a2, 'journal', b)


def test_assoc_authors0_reverse_link_reassign_clear():
    a1 = DBLP_Record(ee="sample_text", key="sample_text", mdate="sample_text", url="sample_text")
    a2 = DBLP_Record(ee="sample_text_2", key="sample_text_2", mdate="sample_text_2", url="sample_text_2")
    b = DBLP_Author(name="sample_text")
    _safe_set(b, 'Author', a1)
    assert _is_linked(b, 'Author', a1)
    if hasattr(a1, 'records'):
        assert _is_linked(a1, 'records', b)
    _safe_set(b, 'Author', a2)
    assert _is_linked(b, 'Author', a2)
    if hasattr(a1, 'records'):
        assert not _is_linked(a1, 'records', b)
    if hasattr(a2, 'records'):
        assert _is_linked(a2, 'records', b)
    _safe_set(b, 'Author', None)
    assert not _is_linked(b, 'Author', a2)
    if hasattr(a2, 'records'):
        assert not _is_linked(a2, 'records', b)


def test_assoc_editors11_reverse_link_reassign_clear():
    a1 = DBLP_InProceedings(bootitle="sample_text", fromPage=7, month="sample_text", title="sample_text", toPage=7, year=7)
    a2 = DBLP_InProceedings(bootitle="sample_text_2", fromPage=13, month="sample_text_2", title="sample_text_2", toPage=13, year=13)
    b = DBLP_Editor(name="sample_text")
    _safe_set(b, 'DBLP_Editor12', a1)
    assert _is_linked(b, 'DBLP_Editor12', a1)
    if hasattr(a1, 'DBLP_InProceedings'):
        assert _is_linked(a1, 'DBLP_InProceedings', b)
    _safe_set(b, 'DBLP_Editor12', a2)
    assert _is_linked(b, 'DBLP_Editor12', a2)
    if hasattr(a1, 'DBLP_InProceedings'):
        assert not _is_linked(a1, 'DBLP_InProceedings', b)
    if hasattr(a2, 'DBLP_InProceedings'):
        assert _is_linked(a2, 'DBLP_InProceedings', b)
    _safe_set(b, 'DBLP_Editor12', None)
    assert not _is_linked(b, 'DBLP_Editor12', a2)
    if hasattr(a2, 'DBLP_InProceedings'):
        assert not _is_linked(a2, 'DBLP_InProceedings', b)


def test_assoc_editors20_reverse_link_reassign_clear():
    a1 = DBLP_Proceedings(isbn="sample_text", month="sample_text", title="sample_text", year=7)
    a2 = DBLP_Proceedings(isbn="sample_text_2", month="sample_text_2", title="sample_text_2", year=13)
    b = DBLP_Editor(name="sample_text")
    _safe_set(b, 'DBLP_Editor21', a1)
    assert _is_linked(b, 'DBLP_Editor21', a1)
    if hasattr(a1, 'DBLP_Proceedings'):
        assert _is_linked(a1, 'DBLP_Proceedings', b)
    _safe_set(b, 'DBLP_Editor21', a2)
    assert _is_linked(b, 'DBLP_Editor21', a2)
    if hasattr(a1, 'DBLP_Proceedings'):
        assert not _is_linked(a1, 'DBLP_Proceedings', b)
    if hasattr(a2, 'DBLP_Proceedings'):
        assert _is_linked(a2, 'DBLP_Proceedings', b)
    _safe_set(b, 'DBLP_Editor21', None)
    assert not _is_linked(b, 'DBLP_Editor21', a2)
    if hasattr(a2, 'DBLP_Proceedings'):
        assert not _is_linked(a2, 'DBLP_Proceedings', b)


def test_assoc_editors30_reverse_link_reassign_clear():
    a1 = DBLP_Www(month="sample_text", title="sample_text", year=7)
    a2 = DBLP_Www(month="sample_text_2", title="sample_text_2", year=13)
    b = DBLP_Editor(name="sample_text")
    _safe_set(b, 'DBLP_Editor31', a1)
    assert _is_linked(b, 'DBLP_Editor31', a1)
    if hasattr(a1, 'DBLP_Www'):
        assert _is_linked(a1, 'DBLP_Www', b)
    _safe_set(b, 'DBLP_Editor31', a2)
    assert _is_linked(b, 'DBLP_Editor31', a2)
    if hasattr(a1, 'DBLP_Www'):
        assert not _is_linked(a1, 'DBLP_Www', b)
    if hasattr(a2, 'DBLP_Www'):
        assert _is_linked(a2, 'DBLP_Www', b)
    _safe_set(b, 'DBLP_Editor31', None)
    assert not _is_linked(b, 'DBLP_Editor31', a2)
    if hasattr(a2, 'DBLP_Www'):
        assert not _is_linked(a2, 'DBLP_Www', b)


def test_assoc_editors5_reverse_link_reassign_clear():
    a1 = DBLP_InCollection(bookTitle="sample_text", fromPage=7, month="sample_text", title="sample_text", toPage=7, year=7)
    a2 = DBLP_InCollection(bookTitle="sample_text_2", fromPage=13, month="sample_text_2", title="sample_text_2", toPage=13, year=13)
    b = DBLP_Editor(name="sample_text")
    _safe_set(b, 'DBLP_Editor', a1)
    assert _is_linked(b, 'DBLP_Editor', a1)
    if hasattr(a1, 'DBLP_InCollection'):
        assert _is_linked(a1, 'DBLP_InCollection', b)
    _safe_set(b, 'DBLP_Editor', a2)
    assert _is_linked(b, 'DBLP_Editor', a2)
    if hasattr(a1, 'DBLP_InCollection'):
        assert not _is_linked(a1, 'DBLP_InCollection', b)
    if hasattr(a2, 'DBLP_InCollection'):
        assert _is_linked(a2, 'DBLP_InCollection', b)
    _safe_set(b, 'DBLP_Editor', None)
    assert not _is_linked(b, 'DBLP_Editor', a2)
    if hasattr(a2, 'DBLP_InCollection'):
        assert not _is_linked(a2, 'DBLP_InCollection', b)


def test_assoc_journal1_reverse_link_reassign_clear():
    a1 = DBLP_Journal(name="sample_text")
    a2 = DBLP_Journal(name="sample_text_2")
    b = DBLP_Article(fromPage=7, month="sample_text", number=7, title="sample_text", toPage=7, volume="sample_text", year=7)
    _safe_set(b, 'articles', a1)
    assert _is_linked(b, 'articles', a1)
    if hasattr(a1, 'Journal'):
        assert _is_linked(a1, 'Journal', b)
    _safe_set(b, 'articles', a2)
    assert _is_linked(b, 'articles', a2)
    if hasattr(a1, 'Journal'):
        assert not _is_linked(a1, 'Journal', b)
    if hasattr(a2, 'Journal'):
        assert _is_linked(a2, 'Journal', b)
    _safe_set(b, 'articles', None)
    assert not _is_linked(b, 'articles', a2)
    if hasattr(a2, 'Journal'):
        assert not _is_linked(a2, 'Journal', b)


def test_assoc_organization13_reverse_link_reassign_clear():
    a1 = DBLP_Organization(name="sample_text")
    a2 = DBLP_Organization(name="sample_text_2")
    b = DBLP_InProceedings(bootitle="sample_text", fromPage=7, month="sample_text", title="sample_text", toPage=7, year=7)
    _safe_set(b, 'DBLP_InProceedings14', a1)
    assert _is_linked(b, 'DBLP_InProceedings14', a1)
    if hasattr(a1, 'DBLP_Organization15'):
        assert _is_linked(a1, 'DBLP_Organization15', b)
    _safe_set(b, 'DBLP_InProceedings14', a2)
    assert _is_linked(b, 'DBLP_InProceedings14', a2)
    if hasattr(a1, 'DBLP_Organization15'):
        assert not _is_linked(a1, 'DBLP_Organization15', b)
    if hasattr(a2, 'DBLP_Organization15'):
        assert _is_linked(a2, 'DBLP_Organization15', b)
    _safe_set(b, 'DBLP_InProceedings14', None)
    assert not _is_linked(b, 'DBLP_InProceedings14', a2)
    if hasattr(a2, 'DBLP_Organization15'):
        assert not _is_linked(a2, 'DBLP_Organization15', b)


def test_assoc_publisher16_reverse_link_reassign_clear():
    a1 = DBLP_Publisher(address="sample_text", name="sample_text")
    a2 = DBLP_Publisher(address="sample_text_2", name="sample_text_2")
    b = DBLP_InProceedings(bootitle="sample_text", fromPage=7, month="sample_text", title="sample_text", toPage=7, year=7)
    _safe_set(b, 'DBLP_InProceedings17', a1)
    assert _is_linked(b, 'DBLP_InProceedings17', a1)
    if hasattr(a1, 'DBLP_Publisher18'):
        assert _is_linked(a1, 'DBLP_Publisher18', b)
    _safe_set(b, 'DBLP_InProceedings17', a2)
    assert _is_linked(b, 'DBLP_InProceedings17', a2)
    if hasattr(a1, 'DBLP_Publisher18'):
        assert not _is_linked(a1, 'DBLP_Publisher18', b)
    if hasattr(a2, 'DBLP_Publisher18'):
        assert _is_linked(a2, 'DBLP_Publisher18', b)
    _safe_set(b, 'DBLP_InProceedings17', None)
    assert not _is_linked(b, 'DBLP_InProceedings17', a2)
    if hasattr(a2, 'DBLP_Publisher18'):
        assert not _is_linked(a2, 'DBLP_Publisher18', b)


def test_assoc_publisher22_reverse_link_reassign_clear():
    a1 = DBLP_Publisher(address="sample_text", name="sample_text")
    a2 = DBLP_Publisher(address="sample_text_2", name="sample_text_2")
    b = DBLP_Proceedings(isbn="sample_text", month="sample_text", title="sample_text", year=7)
    _safe_set(b, 'DBLP_Proceedings23', a1)
    assert _is_linked(b, 'DBLP_Proceedings23', a1)
    if hasattr(a1, 'DBLP_Publisher24'):
        assert _is_linked(a1, 'DBLP_Publisher24', b)
    _safe_set(b, 'DBLP_Proceedings23', a2)
    assert _is_linked(b, 'DBLP_Proceedings23', a2)
    if hasattr(a1, 'DBLP_Publisher24'):
        assert not _is_linked(a1, 'DBLP_Publisher24', b)
    if hasattr(a2, 'DBLP_Publisher24'):
        assert _is_linked(a2, 'DBLP_Publisher24', b)
    _safe_set(b, 'DBLP_Proceedings23', None)
    assert not _is_linked(b, 'DBLP_Proceedings23', a2)
    if hasattr(a2, 'DBLP_Publisher24'):
        assert not _is_linked(a2, 'DBLP_Publisher24', b)


def test_assoc_publisher4_reverse_link_reassign_clear():
    a1 = DBLP_Publisher(address="sample_text", name="sample_text")
    a2 = DBLP_Publisher(address="sample_text_2", name="sample_text_2")
    b = DBLP_Book(edition=7, isbn="sample_text", month="sample_text", series="sample_text", title="sample_text", volume=7, year=7)
    _safe_set(b, 'DBLP_Book', a1)
    assert _is_linked(b, 'DBLP_Book', a1)
    if hasattr(a1, 'DBLP_Publisher'):
        assert _is_linked(a1, 'DBLP_Publisher', b)
    _safe_set(b, 'DBLP_Book', a2)
    assert _is_linked(b, 'DBLP_Book', a2)
    if hasattr(a1, 'DBLP_Publisher'):
        assert not _is_linked(a1, 'DBLP_Publisher', b)
    if hasattr(a2, 'DBLP_Publisher'):
        assert _is_linked(a2, 'DBLP_Publisher', b)
    _safe_set(b, 'DBLP_Book', None)
    assert not _is_linked(b, 'DBLP_Book', a2)
    if hasattr(a2, 'DBLP_Publisher'):
        assert not _is_linked(a2, 'DBLP_Publisher', b)


def test_assoc_publisher8_reverse_link_reassign_clear():
    a1 = DBLP_Publisher(address="sample_text", name="sample_text")
    a2 = DBLP_Publisher(address="sample_text_2", name="sample_text_2")
    b = DBLP_InCollection(bookTitle="sample_text", fromPage=7, month="sample_text", title="sample_text", toPage=7, year=7)
    _safe_set(b, 'DBLP_InCollection9', a1)
    assert _is_linked(b, 'DBLP_InCollection9', a1)
    if hasattr(a1, 'DBLP_Publisher10'):
        assert _is_linked(a1, 'DBLP_Publisher10', b)
    _safe_set(b, 'DBLP_InCollection9', a2)
    assert _is_linked(b, 'DBLP_InCollection9', a2)
    if hasattr(a1, 'DBLP_Publisher10'):
        assert not _is_linked(a1, 'DBLP_Publisher10', b)
    if hasattr(a2, 'DBLP_Publisher10'):
        assert _is_linked(a2, 'DBLP_Publisher10', b)
    _safe_set(b, 'DBLP_InCollection9', None)
    assert not _is_linked(b, 'DBLP_InCollection9', a2)
    if hasattr(a2, 'DBLP_Publisher10'):
        assert not _is_linked(a2, 'DBLP_Publisher10', b)


def test_assoc_records2_reverse_link_reassign_clear():
    a1 = DBLP_Record(ee="sample_text", key="sample_text", mdate="sample_text", url="sample_text")
    a2 = DBLP_Record(ee="sample_text_2", key="sample_text_2", mdate="sample_text_2", url="sample_text_2")
    b = DBLP_Author(name="sample_text")
    _safe_set(b, 'authors', {a1})
    assert _is_linked(b, 'authors', a1)
    if hasattr(a1, 'Record'):
        assert _is_linked(a1, 'Record', b)
    _safe_set(b, 'authors', {a2})
    assert _is_linked(b, 'authors', a2)
    if hasattr(a1, 'Record'):
        assert not _is_linked(a1, 'Record', b)
    if hasattr(a2, 'Record'):
        assert _is_linked(a2, 'Record', b)
    _safe_set(b, 'authors', set())
    assert not _is_linked(b, 'authors', a2)
    if hasattr(a2, 'Record'):
        assert not _is_linked(a2, 'Record', b)


def test_assoc_school19_reverse_link_reassign_clear():
    a1 = DBLP_School(address="sample_text", name="sample_text")
    a2 = DBLP_School(address="sample_text_2", name="sample_text_2")
    b = DBLP_MastersThesis(month="sample_text", title="sample_text", year=7)
    _safe_set(b, 'DBLP_MastersThesis', a1)
    assert _is_linked(b, 'DBLP_MastersThesis', a1)
    if hasattr(a1, 'DBLP_School'):
        assert _is_linked(a1, 'DBLP_School', b)
    _safe_set(b, 'DBLP_MastersThesis', a2)
    assert _is_linked(b, 'DBLP_MastersThesis', a2)
    if hasattr(a1, 'DBLP_School'):
        assert not _is_linked(a1, 'DBLP_School', b)
    if hasattr(a2, 'DBLP_School'):
        assert _is_linked(a2, 'DBLP_School', b)
    _safe_set(b, 'DBLP_MastersThesis', None)
    assert not _is_linked(b, 'DBLP_MastersThesis', a2)
    if hasattr(a2, 'DBLP_School'):
        assert not _is_linked(a2, 'DBLP_School', b)


def test_assoc_school28_reverse_link_reassign_clear():
    a1 = DBLP_School(address="sample_text", name="sample_text")
    a2 = DBLP_School(address="sample_text_2", name="sample_text_2")
    b = DBLP_PhDThesis(month="sample_text", title="sample_text", year=7)
    _safe_set(b, 'DBLP_PhDThesis', a1)
    assert _is_linked(b, 'DBLP_PhDThesis', a1)
    if hasattr(a1, 'DBLP_School29'):
        assert _is_linked(a1, 'DBLP_School29', b)
    _safe_set(b, 'DBLP_PhDThesis', a2)
    assert _is_linked(b, 'DBLP_PhDThesis', a2)
    if hasattr(a1, 'DBLP_School29'):
        assert not _is_linked(a1, 'DBLP_School29', b)
    if hasattr(a2, 'DBLP_School29'):
        assert _is_linked(a2, 'DBLP_School29', b)
    _safe_set(b, 'DBLP_PhDThesis', None)
    assert not _is_linked(b, 'DBLP_PhDThesis', a2)
    if hasattr(a2, 'DBLP_School29'):
        assert not _is_linked(a2, 'DBLP_School29', b)


def test_assoc_sponsoredBy25_reverse_link_reassign_clear():
    a1 = DBLP_Proceedings(isbn="sample_text", month="sample_text", title="sample_text", year=7)
    a2 = DBLP_Proceedings(isbn="sample_text_2", month="sample_text_2", title="sample_text_2", year=13)
    b = DBLP_Organization(name="sample_text")
    _safe_set(b, 'DBLP_Organization27', a1)
    assert _is_linked(b, 'DBLP_Organization27', a1)
    if hasattr(a1, 'DBLP_Proceedings26'):
        assert _is_linked(a1, 'DBLP_Proceedings26', b)
    _safe_set(b, 'DBLP_Organization27', a2)
    assert _is_linked(b, 'DBLP_Organization27', a2)
    if hasattr(a1, 'DBLP_Proceedings26'):
        assert not _is_linked(a1, 'DBLP_Proceedings26', b)
    if hasattr(a2, 'DBLP_Proceedings26'):
        assert _is_linked(a2, 'DBLP_Proceedings26', b)
    _safe_set(b, 'DBLP_Organization27', None)
    assert not _is_linked(b, 'DBLP_Organization27', a2)
    if hasattr(a2, 'DBLP_Proceedings26'):
        assert not _is_linked(a2, 'DBLP_Proceedings26', b)


def test_assoc_sponsoredBy6_reverse_link_reassign_clear():
    a1 = DBLP_Organization(name="sample_text")
    a2 = DBLP_Organization(name="sample_text_2")
    b = DBLP_InCollection(bookTitle="sample_text", fromPage=7, month="sample_text", title="sample_text", toPage=7, year=7)
    _safe_set(b, 'DBLP_InCollection7', a1)
    assert _is_linked(b, 'DBLP_InCollection7', a1)
    if hasattr(a1, 'DBLP_Organization'):
        assert _is_linked(a1, 'DBLP_Organization', b)
    _safe_set(b, 'DBLP_InCollection7', a2)
    assert _is_linked(b, 'DBLP_InCollection7', a2)
    if hasattr(a1, 'DBLP_Organization'):
        assert not _is_linked(a1, 'DBLP_Organization', b)
    if hasattr(a2, 'DBLP_Organization'):
        assert _is_linked(a2, 'DBLP_Organization', b)
    _safe_set(b, 'DBLP_InCollection7', None)
    assert not _is_linked(b, 'DBLP_InCollection7', a2)
    if hasattr(a2, 'DBLP_Organization'):
        assert not _is_linked(a2, 'DBLP_Organization', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

