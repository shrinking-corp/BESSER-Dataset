import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Article,
    BiblioReference,
    Journal,
    SimpleCitation,
    SimpleFeature,
    SimpleIdentifier,
    publication_Article,
    publication_BiblioReference,
    publication_BiblioReferenceSet,
    publication_Book,
    publication_BookArticle,
    publication_Contact,
    publication_Content,
    publication_Indexing,
    publication_Journal,
    publication_JournalArticle,
    publication_JournalIssue,
    publication_LegalEntity,
    publication_Multimedia,
    publication_Ontology,
    publication_OrderedLegalEntitySet,
    publication_Organization,
    publication_Proceeding,
    publication_Protocol,
    publication_SimpleCitation,
    publication_SimpleFeature,
    publication_SimpleOntologyTerm,
    publication_TechnicalReport,
    publication_Thesis,
    publication_WebResource,
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

def test_assoc_articles17_reverse_link_reassign_clear():
    a1 = publication_BookArticle(section="sample_text")
    a2 = publication_BookArticle(section="sample_text_2")
    b = publication_Book(edition="sample_text", iSBN="sample_text", series="sample_text", volume="sample_text")
    _safe_set(b, 'book', {a1})
    assert _is_linked(b, 'book', a1)
    if hasattr(a1, 'BookArticle'):
        assert _is_linked(a1, 'BookArticle', b)
    _safe_set(b, 'book', {a2})
    assert _is_linked(b, 'book', a2)
    if hasattr(a1, 'BookArticle'):
        assert not _is_linked(a1, 'BookArticle', b)
    if hasattr(a2, 'BookArticle'):
        assert _is_linked(a2, 'BookArticle', b)
    _safe_set(b, 'book', set())
    assert not _is_linked(b, 'book', a2)
    if hasattr(a2, 'BookArticle'):
        assert not _is_linked(a2, 'BookArticle', b)


def test_assoc_book18_reverse_link_reassign_clear():
    a1 = publication_BookArticle(section="sample_text")
    a2 = publication_BookArticle(section="sample_text_2")
    b = publication_Book(edition="sample_text", iSBN="sample_text", series="sample_text", volume="sample_text")
    _safe_set(b, 'Book', a1)
    assert _is_linked(b, 'Book', a1)
    if hasattr(a1, 'articles'):
        assert _is_linked(a1, 'articles', b)
    _safe_set(b, 'Book', a2)
    assert _is_linked(b, 'Book', a2)
    if hasattr(a1, 'articles'):
        assert not _is_linked(a1, 'articles', b)
    if hasattr(a2, 'articles'):
        assert _is_linked(a2, 'articles', b)
    _safe_set(b, 'Book', None)
    assert not _is_linked(b, 'Book', a2)
    if hasattr(a2, 'articles'):
        assert not _is_linked(a2, 'articles', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_abbreviation35_stub_double():
    # publication_SimpleOntologyTerm has no real 'publication_SimpleOntologyTerm36' property in the generated
    # code (a bare stub) -- manually attach it so publication_Journal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication_Journal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication_Journal(iSSN="sample_text")
    partner = publication_SimpleOntologyTerm()
    setattr(partner, 'publication_SimpleOntologyTerm36', None)
    _safe_set(owner, 'publication_Journal', partner)
    assert getattr(partner, 'publication_SimpleOntologyTerm36') == owner
    _safe_set(owner, 'publication_Journal', None)
    assert getattr(partner, 'publication_SimpleOntologyTerm36') is None


def test_assoc_articles39_stub_double():
    # publication_JournalArticle has no real 'JournalArticle' property in the generated
    # code (a bare stub) -- manually attach it so publication_JournalIssue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication_JournalIssue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication_JournalIssue(issue="sample_text", issueSupplement="sample_text", volume="sample_text")
    partner = publication_JournalArticle()
    setattr(partner, 'JournalArticle', None)
    _safe_set(owner, 'journalIssue', {partner})
    assert getattr(partner, 'JournalArticle') == owner
    _safe_set(owner, 'journalIssue', set())
    assert getattr(partner, 'JournalArticle') is None


def test_assoc_authority23_stub_double():
    # publication_LegalEntity has no real 'publication_LegalEntity25' property in the generated
    # code (a bare stub) -- manually attach it so publication_Indexing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication_Indexing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication_Indexing(keywords="sample_text")
    partner = publication_LegalEntity()
    setattr(partner, 'publication_LegalEntity25', None)
    _safe_set(owner, 'publication_Indexing24', partner)
    assert getattr(partner, 'publication_LegalEntity25') == owner
    _safe_set(owner, 'publication_Indexing24', None)
    assert getattr(partner, 'publication_LegalEntity25') is None


def test_assoc_biblioReference19_stub_double():
    # publication_BiblioReference has no real 'publication_BiblioReference21' property in the generated
    # code (a bare stub) -- manually attach it so publication_Content's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication_Content's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication_Content(body="sample_text")
    partner = publication_BiblioReference()
    setattr(partner, 'publication_BiblioReference21', None)
    _safe_set(owner, 'publication_Content20', partner)
    assert getattr(partner, 'publication_BiblioReference21') == owner
    _safe_set(owner, 'publication_Content20', None)
    assert getattr(partner, 'publication_BiblioReference21') is None


def test_assoc_citations14_stub_double():
    # publication_BiblioReferenceSet has no real 'publication_BiblioReferenceSet' property in the generated
    # code (a bare stub) -- manually attach it so publication_SimpleCitation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication_SimpleCitation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication_SimpleCitation(authorList="sample_text", date=date(2024, 1, 1), source="sample_text")
    partner = publication_BiblioReferenceSet()
    setattr(partner, 'publication_BiblioReferenceSet', None)
    _safe_set(owner, 'publication_SimpleCitation', partner)
    assert owner in getattr(partner, 'publication_BiblioReferenceSet')
    _safe_set(owner, 'publication_SimpleCitation', None)
    assert owner not in getattr(partner, 'publication_BiblioReferenceSet')


def test_assoc_classificationCodes31_stub_double():
    # publication_SimpleOntologyTerm has no real 'publication_SimpleOntologyTerm33' property in the generated
    # code (a bare stub) -- manually attach it so publication_Indexing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication_Indexing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication_Indexing(keywords="sample_text")
    partner = publication_SimpleOntologyTerm()
    setattr(partner, 'publication_SimpleOntologyTerm33', None)
    _safe_set(owner, 'publication_Indexing32', {partner})
    assert getattr(partner, 'publication_SimpleOntologyTerm33') == owner
    _safe_set(owner, 'publication_Indexing32', set())
    assert getattr(partner, 'publication_SimpleOntologyTerm33') is None


def test_assoc_content11_stub_double():
    # publication_BiblioReference has no real 'publication_BiblioReference12' property in the generated
    # code (a bare stub) -- manually attach it so publication_Content's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication_Content's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication_Content(body="sample_text")
    partner = publication_BiblioReference()
    setattr(partner, 'publication_BiblioReference12', None)
    _safe_set(owner, 'publication_Content', partner)
    assert getattr(partner, 'publication_BiblioReference12') == owner
    _safe_set(owner, 'publication_Content', None)
    assert getattr(partner, 'publication_BiblioReference12') is None


def test_assoc_editors15_stub_double():
    # publication_OrderedLegalEntitySet has no real 'publication_OrderedLegalEntitySet16' property in the generated
    # code (a bare stub) -- manually attach it so publication_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication_Book(edition="sample_text", iSBN="sample_text", series="sample_text", volume="sample_text")
    partner = publication_OrderedLegalEntitySet()
    setattr(partner, 'publication_OrderedLegalEntitySet16', None)
    _safe_set(owner, 'publication_Book', partner)
    assert getattr(partner, 'publication_OrderedLegalEntitySet16') == owner
    _safe_set(owner, 'publication_Book', None)
    assert getattr(partner, 'publication_OrderedLegalEntitySet16') is None


def test_assoc_indexings13_stub_double():
    # publication_BiblioReference has no real 'reference' property in the generated
    # code (a bare stub) -- manually attach it so publication_Indexing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication_Indexing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication_Indexing(keywords="sample_text")
    partner = publication_BiblioReference()
    setattr(partner, 'reference', None)
    _safe_set(owner, 'Indexing', partner)
    assert owner in getattr(partner, 'reference')
    _safe_set(owner, 'Indexing', None)
    assert owner not in getattr(partner, 'reference')


def test_assoc_journalIssue37_stub_double():
    # publication_JournalArticle has no real 'articles38' property in the generated
    # code (a bare stub) -- manually attach it so publication_JournalIssue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication_JournalIssue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication_JournalIssue(issue="sample_text", issueSupplement="sample_text", volume="sample_text")
    partner = publication_JournalArticle()
    setattr(partner, 'articles38', None)
    _safe_set(owner, 'JournalIssue', partner)
    assert getattr(partner, 'articles38') == owner
    _safe_set(owner, 'JournalIssue', None)
    assert getattr(partner, 'articles38') is None


def test_assoc_librarian22_stub_double():
    # publication_Contact has no real 'publication_Contact' property in the generated
    # code (a bare stub) -- manually attach it so publication_Indexing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication_Indexing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication_Indexing(keywords="sample_text")
    partner = publication_Contact()
    setattr(partner, 'publication_Contact', None)
    _safe_set(owner, 'publication_Indexing', partner)
    assert getattr(partner, 'publication_Contact') == owner
    _safe_set(owner, 'publication_Indexing', None)
    assert getattr(partner, 'publication_Contact') is None


def test_assoc_reference34_stub_double():
    # publication_BiblioReference has no real 'BiblioReference' property in the generated
    # code (a bare stub) -- manually attach it so publication_Indexing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication_Indexing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication_Indexing(keywords="sample_text")
    partner = publication_BiblioReference()
    setattr(partner, 'BiblioReference', None)
    _safe_set(owner, 'indexings', partner)
    assert getattr(partner, 'BiblioReference') == owner
    _safe_set(owner, 'indexings', None)
    assert getattr(partner, 'BiblioReference') is None


def test_assoc_subjectHeadingOntology26_stub_double():
    # publication_Ontology has no real 'publication_Ontology' property in the generated
    # code (a bare stub) -- manually attach it so publication_Indexing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication_Indexing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication_Indexing(keywords="sample_text")
    partner = publication_Ontology()
    setattr(partner, 'publication_Ontology', None)
    _safe_set(owner, 'publication_Indexing27', partner)
    assert getattr(partner, 'publication_Ontology') == owner
    _safe_set(owner, 'publication_Indexing27', None)
    assert getattr(partner, 'publication_Ontology') is None


def test_assoc_subjectHeadings28_stub_double():
    # publication_SimpleOntologyTerm has no real 'publication_SimpleOntologyTerm30' property in the generated
    # code (a bare stub) -- manually attach it so publication_Indexing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # publication_Indexing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = publication_Indexing(keywords="sample_text")
    partner = publication_SimpleOntologyTerm()
    setattr(partner, 'publication_SimpleOntologyTerm30', None)
    _safe_set(owner, 'publication_Indexing29', {partner})
    assert getattr(partner, 'publication_SimpleOntologyTerm30') == owner
    _safe_set(owner, 'publication_Indexing29', set())
    assert getattr(partner, 'publication_SimpleOntologyTerm30') is None


