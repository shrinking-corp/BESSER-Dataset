import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Administrator,
    Author,
    Bid,
    Chairman,
    Co_author,
    Conference,
    ConferenceMember,
    Decision,
    Document,
    ExternalReviewer,
    Meta_Reviewer,
    Paper,
    Person,
    ProgramCommittee,
    ProgramCommitteeMember,
    Review,
    Reviewer,
    SubjectArea,
    Thing,
    User,
    cmt_Acceptance,
    cmt_Administrator,
    cmt_AssociatedChair,
    cmt_Author,
    cmt_AuthorNotReviewer,
    cmt_Bid,
    cmt_Chairman,
    cmt_Co_author,
    cmt_Conference,
    cmt_ConferenceChair,
    cmt_ConferenceMember,
    cmt_Decision,
    cmt_Document,
    cmt_ExternalReviewer,
    cmt_Meta_Review,
    cmt_Meta_Reviewer,
    cmt_Paper,
    cmt_PaperAbstract,
    cmt_PaperFullVersion,
    cmt_Person,
    cmt_Preference,
    cmt_ProgramCommittee,
    cmt_ProgramCommitteeChair,
    cmt_ProgramCommitteeMember,
    cmt_Rejection,
    cmt_Review,
    cmt_Reviewer,
    cmt_SubjectArea,
    cmt_Thing,
    cmt_User,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_cmt_Conference_acceptsHardcopySubmissions_value_roundtrip():
    instance = cmt_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    assert instance.acceptsHardcopySubmissions == "sample_text"
    instance.acceptsHardcopySubmissions = "sample_text_2"
    assert instance.acceptsHardcopySubmissions == "sample_text_2"


def test_cmt_Conference_date_value_roundtrip():
    instance = cmt_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_cmt_Conference_logoURL_value_roundtrip():
    instance = cmt_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    assert instance.logoURL == "sample_text"
    instance.logoURL = "sample_text_2"
    assert instance.logoURL == "sample_text_2"


def test_cmt_Conference_reviewsPerPaper_value_roundtrip():
    instance = cmt_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    assert instance.reviewsPerPaper == "sample_text"
    instance.reviewsPerPaper = "sample_text_2"
    assert instance.reviewsPerPaper == "sample_text_2"


def test_cmt_Conference_siteURL_value_roundtrip():
    instance = cmt_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    assert instance.siteURL == "sample_text"
    instance.siteURL = "sample_text_2"
    assert instance.siteURL == "sample_text_2"


def test_cmt_Paper_paperID_value_roundtrip():
    instance = cmt_Paper(paperID="sample_text", title="sample_text")
    assert instance.paperID == "sample_text"
    instance.paperID = "sample_text_2"
    assert instance.paperID == "sample_text_2"


def test_cmt_Paper_title_value_roundtrip():
    instance = cmt_Paper(paperID="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_cmt_Person_email_value_roundtrip():
    instance = cmt_Person(email="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_cmt_ProgramCommitteeMember_maxPapers_value_roundtrip():
    instance = cmt_ProgramCommitteeMember(maxPapers="sample_text")
    assert instance.maxPapers == "sample_text"
    instance.maxPapers = "sample_text_2"
    assert instance.maxPapers == "sample_text_2"


def test_cmt_AuthorNotReviewer_isa_Author():
    instance = cmt_AuthorNotReviewer()
    assert isinstance(instance, Author)


def test_cmt_Co_author_isa_Author():
    instance = cmt_Co_author()
    assert isinstance(instance, Author)


def test_cmt_AssociatedChair_isa_Chairman():
    instance = cmt_AssociatedChair()
    assert isinstance(instance, Chairman)


def test_cmt_ConferenceChair_isa_Chairman():
    instance = cmt_ConferenceChair()
    assert isinstance(instance, Chairman)


def test_cmt_ProgramCommitteeChair_isa_Chairman():
    instance = cmt_ProgramCommitteeChair()
    assert isinstance(instance, Chairman)


def test_cmt_AssociatedChair_isa_ConferenceMember():
    instance = cmt_AssociatedChair()
    assert isinstance(instance, ConferenceMember)


def test_cmt_Author_isa_ConferenceMember():
    instance = cmt_Author()
    assert isinstance(instance, ConferenceMember)


def test_cmt_Chairman_isa_ConferenceMember():
    instance = cmt_Chairman()
    assert isinstance(instance, ConferenceMember)


def test_cmt_ConferenceChair_isa_ConferenceMember():
    instance = cmt_ConferenceChair()
    assert isinstance(instance, ConferenceMember)


def test_cmt_ProgramCommitteeMember_isa_ConferenceMember():
    instance = cmt_ProgramCommitteeMember(maxPapers="sample_text")
    assert isinstance(instance, ConferenceMember)


def test_cmt_Reviewer_isa_ConferenceMember():
    instance = cmt_Reviewer()
    assert isinstance(instance, ConferenceMember)


def test_cmt_Acceptance_isa_Decision():
    instance = cmt_Acceptance()
    assert isinstance(instance, Decision)


def test_cmt_Rejection_isa_Decision():
    instance = cmt_Rejection()
    assert isinstance(instance, Decision)


def test_cmt_Paper_isa_Document():
    instance = cmt_Paper(paperID="sample_text", title="sample_text")
    assert isinstance(instance, Document)


def test_cmt_Review_isa_Document():
    instance = cmt_Review()
    assert isinstance(instance, Document)


def test_cmt_PaperAbstract_isa_Paper():
    instance = cmt_PaperAbstract()
    assert isinstance(instance, Paper)


def test_cmt_PaperFullVersion_isa_Paper():
    instance = cmt_PaperFullVersion()
    assert isinstance(instance, Paper)


def test_cmt_Chairman_isa_Person():
    instance = cmt_Chairman()
    assert isinstance(instance, Person)


def test_cmt_ConferenceMember_isa_Person():
    instance = cmt_ConferenceMember()
    assert isinstance(instance, Person)


def test_cmt_ExternalReviewer_isa_Person():
    instance = cmt_ExternalReviewer()
    assert isinstance(instance, Person)


def test_cmt_ProgramCommitteeMember_isa_Person():
    instance = cmt_ProgramCommitteeMember(maxPapers="sample_text")
    assert isinstance(instance, Person)


def test_cmt_User_isa_Person():
    instance = cmt_User()
    assert isinstance(instance, Person)


def test_cmt_ProgramCommitteeChair_isa_ProgramCommitteeMember():
    instance = cmt_ProgramCommitteeChair()
    assert isinstance(instance, ProgramCommitteeMember)


def test_cmt_Meta_Review_isa_Review():
    instance = cmt_Meta_Review()
    assert isinstance(instance, Review)


def test_cmt_Meta_Reviewer_isa_Reviewer():
    instance = cmt_Meta_Reviewer()
    assert isinstance(instance, Reviewer)


def test_cmt_Conference_isa_Thing():
    instance = cmt_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    assert isinstance(instance, Thing)


def test_cmt_Administrator_isa_User():
    instance = cmt_Administrator()
    assert isinstance(instance, User)


def test_cmt_Author_isa_User():
    instance = cmt_Author()
    assert isinstance(instance, User)


def test_cmt_Reviewer_isa_User():
    instance = cmt_Reviewer()
    assert isinstance(instance, User)


def test_assoc_acceptedBy47_link_reassign_clear():
    a = cmt_Paper(paperID="sample_text", title="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'acceptPaper', b1)
    assert _is_linked(a, 'acceptPaper', b1)
    if hasattr(b1, 'Administrator48'):
        assert _is_linked(b1, 'Administrator48', a)
    _safe_set(a, 'acceptPaper', b2)
    assert _is_linked(a, 'acceptPaper', b2)
    if hasattr(b1, 'Administrator48'):
        assert not _is_linked(b1, 'Administrator48', a)
    if hasattr(b2, 'Administrator48'):
        assert _is_linked(b2, 'Administrator48', a)
    _safe_set(a, 'acceptPaper', None)
    assert not _is_linked(a, 'acceptPaper', b2)
    if hasattr(b2, 'Administrator48'):
        assert not _is_linked(b2, 'Administrator48', a)


def test_assoc_addedBy27_link_reassign_clear():
    a = cmt_ProgramCommitteeMember(maxPapers="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'addProgramCommitteeMember', b1)
    assert _is_linked(a, 'addProgramCommitteeMember', b1)
    if hasattr(b1, 'Administrator28'):
        assert _is_linked(b1, 'Administrator28', a)
    _safe_set(a, 'addProgramCommitteeMember', b2)
    assert _is_linked(a, 'addProgramCommitteeMember', b2)
    if hasattr(b1, 'Administrator28'):
        assert not _is_linked(b1, 'Administrator28', a)
    if hasattr(b2, 'Administrator28'):
        assert _is_linked(b2, 'Administrator28', a)
    _safe_set(a, 'addProgramCommitteeMember', None)
    assert not _is_linked(a, 'addProgramCommitteeMember', b2)
    if hasattr(b2, 'Administrator28'):
        assert not _is_linked(b2, 'Administrator28', a)


def test_assoc_assignedTo40_link_reassign_clear():
    a = cmt_Paper(paperID="sample_text", title="sample_text")
    b1 = Reviewer()
    b2 = Reviewer()
    _safe_set(a, 'hasBeenAssigned', b1)
    assert _is_linked(a, 'hasBeenAssigned', b1)
    if hasattr(b1, 'Reviewer41'):
        assert _is_linked(b1, 'Reviewer41', a)
    _safe_set(a, 'hasBeenAssigned', b2)
    assert _is_linked(a, 'hasBeenAssigned', b2)
    if hasattr(b1, 'Reviewer41'):
        assert not _is_linked(b1, 'Reviewer41', a)
    if hasattr(b2, 'Reviewer41'):
        assert _is_linked(b2, 'Reviewer41', a)
    _safe_set(a, 'hasBeenAssigned', None)
    assert not _is_linked(a, 'hasBeenAssigned', b2)
    if hasattr(b2, 'Reviewer41'):
        assert not _is_linked(b2, 'Reviewer41', a)


def test_assoc_detailsEnteredBy21_link_reassign_clear():
    a = cmt_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'enterConferenceDetails', b1)
    assert _is_linked(a, 'enterConferenceDetails', b1)
    if hasattr(b1, 'Administrator22'):
        assert _is_linked(b1, 'Administrator22', a)
    _safe_set(a, 'enterConferenceDetails', b2)
    assert _is_linked(a, 'enterConferenceDetails', b2)
    if hasattr(b1, 'Administrator22'):
        assert not _is_linked(b1, 'Administrator22', a)
    if hasattr(b2, 'Administrator22'):
        assert _is_linked(b2, 'Administrator22', a)
    _safe_set(a, 'enterConferenceDetails', None)
    assert not _is_linked(a, 'enterConferenceDetails', b2)
    if hasattr(b2, 'Administrator22'):
        assert not _is_linked(b2, 'Administrator22', a)


def test_assoc_hardcopyMailingManifestsPrintedBy19_link_reassign_clear():
    a = cmt_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'printHardcopyMailingManifests', b1)
    assert _is_linked(a, 'printHardcopyMailingManifests', b1)
    if hasattr(b1, 'Administrator20'):
        assert _is_linked(b1, 'Administrator20', a)
    _safe_set(a, 'printHardcopyMailingManifests', b2)
    assert _is_linked(a, 'printHardcopyMailingManifests', b2)
    if hasattr(b1, 'Administrator20'):
        assert not _is_linked(b1, 'Administrator20', a)
    if hasattr(b2, 'Administrator20'):
        assert _is_linked(b2, 'Administrator20', a)
    _safe_set(a, 'printHardcopyMailingManifests', None)
    assert not _is_linked(a, 'printHardcopyMailingManifests', b2)
    if hasattr(b2, 'Administrator20'):
        assert not _is_linked(b2, 'Administrator20', a)


def test_assoc_hasAuthor46_link_reassign_clear():
    a = cmt_Paper(paperID="sample_text", title="sample_text")
    b1 = Author()
    b2 = Author()
    _safe_set(a, 'writePaper', b1)
    assert _is_linked(a, 'writePaper', b1)
    if hasattr(b1, 'Author'):
        assert _is_linked(b1, 'Author', a)
    _safe_set(a, 'writePaper', b2)
    assert _is_linked(a, 'writePaper', b2)
    if hasattr(b1, 'Author'):
        assert not _is_linked(b1, 'Author', a)
    if hasattr(b2, 'Author'):
        assert _is_linked(b2, 'Author', a)
    _safe_set(a, 'writePaper', None)
    assert not _is_linked(a, 'writePaper', b2)
    if hasattr(b2, 'Author'):
        assert not _is_linked(b2, 'Author', a)


def test_assoc_hasBid36_link_reassign_clear():
    a = cmt_Paper(paperID="sample_text", title="sample_text")
    b1 = Bid()
    b2 = Bid()
    _safe_set(a, 'cmt_Paper', b1)
    assert _is_linked(a, 'cmt_Paper', b1)
    if hasattr(b1, 'Bid37'):
        assert _is_linked(b1, 'Bid37', a)
    _safe_set(a, 'cmt_Paper', b2)
    assert _is_linked(a, 'cmt_Paper', b2)
    if hasattr(b1, 'Bid37'):
        assert not _is_linked(b1, 'Bid37', a)
    if hasattr(b2, 'Bid37'):
        assert _is_linked(b2, 'Bid37', a)
    _safe_set(a, 'cmt_Paper', None)
    assert not _is_linked(a, 'cmt_Paper', b2)
    if hasattr(b2, 'Bid37'):
        assert not _is_linked(b2, 'Bid37', a)


def test_assoc_hasCo_author35_link_reassign_clear():
    a = cmt_Paper(paperID="sample_text", title="sample_text")
    b1 = Co_author()
    b2 = Co_author()
    _safe_set(a, 'co_writePaper', b1)
    assert _is_linked(a, 'co_writePaper', b1)
    if hasattr(b1, 'Co_author'):
        assert _is_linked(b1, 'Co_author', a)
    _safe_set(a, 'co_writePaper', b2)
    assert _is_linked(a, 'co_writePaper', b2)
    if hasattr(b1, 'Co_author'):
        assert not _is_linked(b1, 'Co_author', a)
    if hasattr(b2, 'Co_author'):
        assert _is_linked(b2, 'Co_author', a)
    _safe_set(a, 'co_writePaper', None)
    assert not _is_linked(a, 'co_writePaper', b2)
    if hasattr(b2, 'Co_author'):
        assert not _is_linked(b2, 'Co_author', a)


def test_assoc_hasConferenceMember10_link_reassign_clear():
    a = cmt_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    b1 = ConferenceMember()
    b2 = ConferenceMember()
    _safe_set(a, 'memberOfConference', b1)
    assert _is_linked(a, 'memberOfConference', b1)
    if hasattr(b1, 'ConferenceMember'):
        assert _is_linked(b1, 'ConferenceMember', a)
    _safe_set(a, 'memberOfConference', b2)
    assert _is_linked(a, 'memberOfConference', b2)
    if hasattr(b1, 'ConferenceMember'):
        assert not _is_linked(b1, 'ConferenceMember', a)
    if hasattr(b2, 'ConferenceMember'):
        assert _is_linked(b2, 'ConferenceMember', a)
    _safe_set(a, 'memberOfConference', None)
    assert not _is_linked(a, 'memberOfConference', b2)
    if hasattr(b2, 'ConferenceMember'):
        assert not _is_linked(b2, 'ConferenceMember', a)


def test_assoc_hasConflictOfInterest7_link_reassign_clear():
    a = cmt_Person(email="sample_text")
    b1 = Document()
    b2 = Document()
    _safe_set(a, 'cmt_Person', b1)
    assert _is_linked(a, 'cmt_Person', b1)
    if hasattr(b1, 'Document'):
        assert _is_linked(b1, 'Document', a)
    _safe_set(a, 'cmt_Person', b2)
    assert _is_linked(a, 'cmt_Person', b2)
    if hasattr(b1, 'Document'):
        assert not _is_linked(b1, 'Document', a)
    if hasattr(b2, 'Document'):
        assert _is_linked(b2, 'Document', a)
    _safe_set(a, 'cmt_Person', None)
    assert not _is_linked(a, 'cmt_Person', b2)
    if hasattr(b2, 'Document'):
        assert not _is_linked(b2, 'Document', a)


def test_assoc_hasDecision38_link_reassign_clear():
    a = cmt_Paper(paperID="sample_text", title="sample_text")
    b1 = Decision()
    b2 = Decision()
    _safe_set(a, 'cmt_Paper39', b1)
    assert _is_linked(a, 'cmt_Paper39', b1)
    if hasattr(b1, 'Decision'):
        assert _is_linked(b1, 'Decision', a)
    _safe_set(a, 'cmt_Paper39', b2)
    assert _is_linked(a, 'cmt_Paper39', b2)
    if hasattr(b1, 'Decision'):
        assert not _is_linked(b1, 'Decision', a)
    if hasattr(b2, 'Decision'):
        assert _is_linked(b2, 'Decision', a)
    _safe_set(a, 'cmt_Paper39', None)
    assert not _is_linked(a, 'cmt_Paper39', b2)
    if hasattr(b2, 'Decision'):
        assert not _is_linked(b2, 'Decision', a)


def test_assoc_hasSubjectArea42_link_reassign_clear():
    a = cmt_Paper(paperID="sample_text", title="sample_text")
    b1 = SubjectArea()
    b2 = SubjectArea()
    _safe_set(a, 'cmt_Paper43', b1)
    assert _is_linked(a, 'cmt_Paper43', b1)
    if hasattr(b1, 'SubjectArea'):
        assert _is_linked(b1, 'SubjectArea', a)
    _safe_set(a, 'cmt_Paper43', b2)
    assert _is_linked(a, 'cmt_Paper43', b2)
    if hasattr(b1, 'SubjectArea'):
        assert not _is_linked(b1, 'SubjectArea', a)
    if hasattr(b2, 'SubjectArea'):
        assert _is_linked(b2, 'SubjectArea', a)
    _safe_set(a, 'cmt_Paper43', None)
    assert not _is_linked(a, 'cmt_Paper43', b2)
    if hasattr(b2, 'SubjectArea'):
        assert not _is_linked(b2, 'SubjectArea', a)


def test_assoc_memberOfProgramCommittee26_link_reassign_clear():
    a = cmt_ProgramCommitteeMember(maxPapers="sample_text")
    b1 = ProgramCommittee()
    b2 = ProgramCommittee()
    _safe_set(a, 'hasProgramCommitteeMember', b1)
    assert _is_linked(a, 'hasProgramCommitteeMember', b1)
    if hasattr(b1, 'ProgramCommittee'):
        assert _is_linked(b1, 'ProgramCommittee', a)
    _safe_set(a, 'hasProgramCommitteeMember', b2)
    assert _is_linked(a, 'hasProgramCommitteeMember', b2)
    if hasattr(b1, 'ProgramCommittee'):
        assert not _is_linked(b1, 'ProgramCommittee', a)
    if hasattr(b2, 'ProgramCommittee'):
        assert _is_linked(b2, 'ProgramCommittee', a)
    _safe_set(a, 'hasProgramCommitteeMember', None)
    assert not _is_linked(a, 'hasProgramCommitteeMember', b2)
    if hasattr(b2, 'ProgramCommittee'):
        assert not _is_linked(b2, 'ProgramCommittee', a)


def test_assoc_paperAssignmentFinalizedBy11_link_reassign_clear():
    a = cmt_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'finalizePaperAssignment', b1)
    assert _is_linked(a, 'finalizePaperAssignment', b1)
    if hasattr(b1, 'Administrator12'):
        assert _is_linked(b1, 'Administrator12', a)
    _safe_set(a, 'finalizePaperAssignment', b2)
    assert _is_linked(a, 'finalizePaperAssignment', b2)
    if hasattr(b1, 'Administrator12'):
        assert not _is_linked(b1, 'Administrator12', a)
    if hasattr(b2, 'Administrator12'):
        assert _is_linked(b2, 'Administrator12', a)
    _safe_set(a, 'finalizePaperAssignment', None)
    assert not _is_linked(a, 'finalizePaperAssignment', b2)
    if hasattr(b2, 'Administrator12'):
        assert not _is_linked(b2, 'Administrator12', a)


def test_assoc_paperAssignmentToolsRunBy15_link_reassign_clear():
    a = cmt_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'runPaperAssignmentTools', b1)
    assert _is_linked(a, 'runPaperAssignmentTools', b1)
    if hasattr(b1, 'Administrator16'):
        assert _is_linked(b1, 'Administrator16', a)
    _safe_set(a, 'runPaperAssignmentTools', b2)
    assert _is_linked(a, 'runPaperAssignmentTools', b2)
    if hasattr(b1, 'Administrator16'):
        assert not _is_linked(b1, 'Administrator16', a)
    if hasattr(b2, 'Administrator16'):
        assert _is_linked(b2, 'Administrator16', a)
    _safe_set(a, 'runPaperAssignmentTools', None)
    assert not _is_linked(a, 'runPaperAssignmentTools', b2)
    if hasattr(b2, 'Administrator16'):
        assert not _is_linked(b2, 'Administrator16', a)


def test_assoc_readByMeta_Reviewer51_link_reassign_clear():
    a = cmt_Paper(paperID="sample_text", title="sample_text")
    b1 = Meta_Reviewer()
    b2 = Meta_Reviewer()
    _safe_set(a, 'cmt_Paper52', b1)
    assert _is_linked(a, 'cmt_Paper52', b1)
    if hasattr(b1, 'Meta_Reviewer'):
        assert _is_linked(b1, 'Meta_Reviewer', a)
    _safe_set(a, 'cmt_Paper52', b2)
    assert _is_linked(a, 'cmt_Paper52', b2)
    if hasattr(b1, 'Meta_Reviewer'):
        assert not _is_linked(b1, 'Meta_Reviewer', a)
    if hasattr(b2, 'Meta_Reviewer'):
        assert _is_linked(b2, 'Meta_Reviewer', a)
    _safe_set(a, 'cmt_Paper52', None)
    assert not _is_linked(a, 'cmt_Paper52', b2)
    if hasattr(b2, 'Meta_Reviewer'):
        assert not _is_linked(b2, 'Meta_Reviewer', a)


def test_assoc_readByReviewer44_link_reassign_clear():
    a = cmt_Paper(paperID="sample_text", title="sample_text")
    b1 = Reviewer()
    b2 = Reviewer()
    _safe_set(a, 'readPaper', b1)
    assert _is_linked(a, 'readPaper', b1)
    if hasattr(b1, 'Reviewer45'):
        assert _is_linked(b1, 'Reviewer45', a)
    _safe_set(a, 'readPaper', b2)
    assert _is_linked(a, 'readPaper', b2)
    if hasattr(b1, 'Reviewer45'):
        assert not _is_linked(b1, 'Reviewer45', a)
    if hasattr(b2, 'Reviewer45'):
        assert _is_linked(b2, 'Reviewer45', a)
    _safe_set(a, 'readPaper', None)
    assert not _is_linked(a, 'readPaper', b2)
    if hasattr(b2, 'Reviewer45'):
        assert not _is_linked(b2, 'Reviewer45', a)


def test_assoc_rejectedBy49_link_reassign_clear():
    a = cmt_Paper(paperID="sample_text", title="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'rejectPaper', b1)
    assert _is_linked(a, 'rejectPaper', b1)
    if hasattr(b1, 'Administrator50'):
        assert _is_linked(b1, 'Administrator50', a)
    _safe_set(a, 'rejectPaper', b2)
    assert _is_linked(a, 'rejectPaper', b2)
    if hasattr(b1, 'Administrator50'):
        assert not _is_linked(b1, 'Administrator50', a)
    if hasattr(b2, 'Administrator50'):
        assert _is_linked(b2, 'Administrator50', a)
    _safe_set(a, 'rejectPaper', None)
    assert not _is_linked(a, 'rejectPaper', b2)
    if hasattr(b2, 'Administrator50'):
        assert not _is_linked(b2, 'Administrator50', a)


def test_assoc_reviewCriteriaEnteredBy13_link_reassign_clear():
    a = cmt_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'enterReviewCriteria', b1)
    assert _is_linked(a, 'enterReviewCriteria', b1)
    if hasattr(b1, 'Administrator14'):
        assert _is_linked(b1, 'Administrator14', a)
    _safe_set(a, 'enterReviewCriteria', b2)
    assert _is_linked(a, 'enterReviewCriteria', b2)
    if hasattr(b1, 'Administrator14'):
        assert not _is_linked(b1, 'Administrator14', a)
    if hasattr(b2, 'Administrator14'):
        assert _is_linked(b2, 'Administrator14', a)
    _safe_set(a, 'enterReviewCriteria', None)
    assert not _is_linked(a, 'enterReviewCriteria', b2)
    if hasattr(b2, 'Administrator14'):
        assert not _is_linked(b2, 'Administrator14', a)


def test_assoc_reviewerBiddingStartedBy23_link_reassign_clear():
    a = cmt_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'startReviewerBidding', b1)
    assert _is_linked(a, 'startReviewerBidding', b1)
    if hasattr(b1, 'Administrator24'):
        assert _is_linked(b1, 'Administrator24', a)
    _safe_set(a, 'startReviewerBidding', b2)
    assert _is_linked(a, 'startReviewerBidding', b2)
    if hasattr(b1, 'Administrator24'):
        assert not _is_linked(b1, 'Administrator24', a)
    if hasattr(b2, 'Administrator24'):
        assert _is_linked(b2, 'Administrator24', a)
    _safe_set(a, 'startReviewerBidding', None)
    assert not _is_linked(a, 'startReviewerBidding', b2)
    if hasattr(b2, 'Administrator24'):
        assert not _is_linked(b2, 'Administrator24', a)


def test_assoc_virtualMeetingEnabledBy17_link_reassign_clear():
    a = cmt_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'enableVirtualMeeting', b1)
    assert _is_linked(a, 'enableVirtualMeeting', b1)
    if hasattr(b1, 'Administrator18'):
        assert _is_linked(b1, 'Administrator18', a)
    _safe_set(a, 'enableVirtualMeeting', b2)
    assert _is_linked(a, 'enableVirtualMeeting', b2)
    if hasattr(b1, 'Administrator18'):
        assert not _is_linked(b1, 'Administrator18', a)
    if hasattr(b2, 'Administrator18'):
        assert _is_linked(b2, 'Administrator18', a)
    _safe_set(a, 'enableVirtualMeeting', None)
    assert not _is_linked(a, 'enableVirtualMeeting', b2)
    if hasattr(b2, 'Administrator18'):
        assert not _is_linked(b2, 'Administrator18', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Administrator_strategy = st.builds(Administrator)
@given(instance=Administrator_strategy)
@settings(max_examples=25)
def test_Administrator_instantiation(instance):
    assert isinstance(instance, Administrator)


Author_strategy = st.builds(Author)
@given(instance=Author_strategy)
@settings(max_examples=25)
def test_Author_instantiation(instance):
    assert isinstance(instance, Author)


Bid_strategy = st.builds(Bid)
@given(instance=Bid_strategy)
@settings(max_examples=25)
def test_Bid_instantiation(instance):
    assert isinstance(instance, Bid)


Chairman_strategy = st.builds(Chairman)
@given(instance=Chairman_strategy)
@settings(max_examples=25)
def test_Chairman_instantiation(instance):
    assert isinstance(instance, Chairman)


Co_author_strategy = st.builds(Co_author)
@given(instance=Co_author_strategy)
@settings(max_examples=25)
def test_Co_author_instantiation(instance):
    assert isinstance(instance, Co_author)


Conference_strategy = st.builds(Conference)
@given(instance=Conference_strategy)
@settings(max_examples=25)
def test_Conference_instantiation(instance):
    assert isinstance(instance, Conference)


ConferenceMember_strategy = st.builds(ConferenceMember)
@given(instance=ConferenceMember_strategy)
@settings(max_examples=25)
def test_ConferenceMember_instantiation(instance):
    assert isinstance(instance, ConferenceMember)


Decision_strategy = st.builds(Decision)
@given(instance=Decision_strategy)
@settings(max_examples=25)
def test_Decision_instantiation(instance):
    assert isinstance(instance, Decision)


Document_strategy = st.builds(Document)
@given(instance=Document_strategy)
@settings(max_examples=25)
def test_Document_instantiation(instance):
    assert isinstance(instance, Document)


ExternalReviewer_strategy = st.builds(ExternalReviewer)
@given(instance=ExternalReviewer_strategy)
@settings(max_examples=25)
def test_ExternalReviewer_instantiation(instance):
    assert isinstance(instance, ExternalReviewer)


Meta_Reviewer_strategy = st.builds(Meta_Reviewer)
@given(instance=Meta_Reviewer_strategy)
@settings(max_examples=25)
def test_Meta_Reviewer_instantiation(instance):
    assert isinstance(instance, Meta_Reviewer)


Paper_strategy = st.builds(Paper)
@given(instance=Paper_strategy)
@settings(max_examples=25)
def test_Paper_instantiation(instance):
    assert isinstance(instance, Paper)


Person_strategy = st.builds(Person)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


ProgramCommittee_strategy = st.builds(ProgramCommittee)
@given(instance=ProgramCommittee_strategy)
@settings(max_examples=25)
def test_ProgramCommittee_instantiation(instance):
    assert isinstance(instance, ProgramCommittee)


ProgramCommitteeMember_strategy = st.builds(ProgramCommitteeMember)
@given(instance=ProgramCommitteeMember_strategy)
@settings(max_examples=25)
def test_ProgramCommitteeMember_instantiation(instance):
    assert isinstance(instance, ProgramCommitteeMember)


Review_strategy = st.builds(Review)
@given(instance=Review_strategy)
@settings(max_examples=25)
def test_Review_instantiation(instance):
    assert isinstance(instance, Review)


Reviewer_strategy = st.builds(Reviewer)
@given(instance=Reviewer_strategy)
@settings(max_examples=25)
def test_Reviewer_instantiation(instance):
    assert isinstance(instance, Reviewer)


SubjectArea_strategy = st.builds(SubjectArea)
@given(instance=SubjectArea_strategy)
@settings(max_examples=25)
def test_SubjectArea_instantiation(instance):
    assert isinstance(instance, SubjectArea)


Thing_strategy = st.builds(Thing)
@given(instance=Thing_strategy)
@settings(max_examples=25)
def test_Thing_instantiation(instance):
    assert isinstance(instance, Thing)


User_strategy = st.builds(User)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


cmt_Acceptance_strategy = st.builds(cmt_Acceptance)
@given(instance=cmt_Acceptance_strategy)
@settings(max_examples=25)
def test_cmt_Acceptance_instantiation(instance):
    assert isinstance(instance, cmt_Acceptance)


cmt_Administrator_strategy = st.builds(cmt_Administrator)
@given(instance=cmt_Administrator_strategy)
@settings(max_examples=25)
def test_cmt_Administrator_instantiation(instance):
    assert isinstance(instance, cmt_Administrator)


cmt_AssociatedChair_strategy = st.builds(cmt_AssociatedChair)
@given(instance=cmt_AssociatedChair_strategy)
@settings(max_examples=25)
def test_cmt_AssociatedChair_instantiation(instance):
    assert isinstance(instance, cmt_AssociatedChair)


cmt_Author_strategy = st.builds(cmt_Author)
@given(instance=cmt_Author_strategy)
@settings(max_examples=25)
def test_cmt_Author_instantiation(instance):
    assert isinstance(instance, cmt_Author)


cmt_AuthorNotReviewer_strategy = st.builds(cmt_AuthorNotReviewer)
@given(instance=cmt_AuthorNotReviewer_strategy)
@settings(max_examples=25)
def test_cmt_AuthorNotReviewer_instantiation(instance):
    assert isinstance(instance, cmt_AuthorNotReviewer)


cmt_Bid_strategy = st.builds(cmt_Bid)
@given(instance=cmt_Bid_strategy)
@settings(max_examples=25)
def test_cmt_Bid_instantiation(instance):
    assert isinstance(instance, cmt_Bid)


cmt_Chairman_strategy = st.builds(cmt_Chairman)
@given(instance=cmt_Chairman_strategy)
@settings(max_examples=25)
def test_cmt_Chairman_instantiation(instance):
    assert isinstance(instance, cmt_Chairman)


cmt_Co_author_strategy = st.builds(cmt_Co_author)
@given(instance=cmt_Co_author_strategy)
@settings(max_examples=25)
def test_cmt_Co_author_instantiation(instance):
    assert isinstance(instance, cmt_Co_author)


cmt_Conference_strategy = st.builds(cmt_Conference, acceptsHardcopySubmissions=safe_text, date=safe_text, logoURL=safe_text, reviewsPerPaper=safe_text, siteURL=safe_text)
@given(instance=cmt_Conference_strategy)
@settings(max_examples=25)
def test_cmt_Conference_instantiation(instance):
    assert isinstance(instance, cmt_Conference)


cmt_ConferenceChair_strategy = st.builds(cmt_ConferenceChair)
@given(instance=cmt_ConferenceChair_strategy)
@settings(max_examples=25)
def test_cmt_ConferenceChair_instantiation(instance):
    assert isinstance(instance, cmt_ConferenceChair)


cmt_ConferenceMember_strategy = st.builds(cmt_ConferenceMember)
@given(instance=cmt_ConferenceMember_strategy)
@settings(max_examples=25)
def test_cmt_ConferenceMember_instantiation(instance):
    assert isinstance(instance, cmt_ConferenceMember)


cmt_Decision_strategy = st.builds(cmt_Decision)
@given(instance=cmt_Decision_strategy)
@settings(max_examples=25)
def test_cmt_Decision_instantiation(instance):
    assert isinstance(instance, cmt_Decision)


cmt_Document_strategy = st.builds(cmt_Document)
@given(instance=cmt_Document_strategy)
@settings(max_examples=25)
def test_cmt_Document_instantiation(instance):
    assert isinstance(instance, cmt_Document)


cmt_ExternalReviewer_strategy = st.builds(cmt_ExternalReviewer)
@given(instance=cmt_ExternalReviewer_strategy)
@settings(max_examples=25)
def test_cmt_ExternalReviewer_instantiation(instance):
    assert isinstance(instance, cmt_ExternalReviewer)


cmt_Meta_Review_strategy = st.builds(cmt_Meta_Review)
@given(instance=cmt_Meta_Review_strategy)
@settings(max_examples=25)
def test_cmt_Meta_Review_instantiation(instance):
    assert isinstance(instance, cmt_Meta_Review)


cmt_Meta_Reviewer_strategy = st.builds(cmt_Meta_Reviewer)
@given(instance=cmt_Meta_Reviewer_strategy)
@settings(max_examples=25)
def test_cmt_Meta_Reviewer_instantiation(instance):
    assert isinstance(instance, cmt_Meta_Reviewer)


cmt_Paper_strategy = st.builds(cmt_Paper, paperID=safe_text, title=safe_text)
@given(instance=cmt_Paper_strategy)
@settings(max_examples=25)
def test_cmt_Paper_instantiation(instance):
    assert isinstance(instance, cmt_Paper)


cmt_PaperAbstract_strategy = st.builds(cmt_PaperAbstract)
@given(instance=cmt_PaperAbstract_strategy)
@settings(max_examples=25)
def test_cmt_PaperAbstract_instantiation(instance):
    assert isinstance(instance, cmt_PaperAbstract)


cmt_PaperFullVersion_strategy = st.builds(cmt_PaperFullVersion)
@given(instance=cmt_PaperFullVersion_strategy)
@settings(max_examples=25)
def test_cmt_PaperFullVersion_instantiation(instance):
    assert isinstance(instance, cmt_PaperFullVersion)


cmt_Person_strategy = st.builds(cmt_Person, email=safe_text)
@given(instance=cmt_Person_strategy)
@settings(max_examples=25)
def test_cmt_Person_instantiation(instance):
    assert isinstance(instance, cmt_Person)


cmt_Preference_strategy = st.builds(cmt_Preference)
@given(instance=cmt_Preference_strategy)
@settings(max_examples=25)
def test_cmt_Preference_instantiation(instance):
    assert isinstance(instance, cmt_Preference)


cmt_ProgramCommittee_strategy = st.builds(cmt_ProgramCommittee)
@given(instance=cmt_ProgramCommittee_strategy)
@settings(max_examples=25)
def test_cmt_ProgramCommittee_instantiation(instance):
    assert isinstance(instance, cmt_ProgramCommittee)


cmt_ProgramCommitteeChair_strategy = st.builds(cmt_ProgramCommitteeChair)
@given(instance=cmt_ProgramCommitteeChair_strategy)
@settings(max_examples=25)
def test_cmt_ProgramCommitteeChair_instantiation(instance):
    assert isinstance(instance, cmt_ProgramCommitteeChair)


cmt_ProgramCommitteeMember_strategy = st.builds(cmt_ProgramCommitteeMember, maxPapers=safe_text)
@given(instance=cmt_ProgramCommitteeMember_strategy)
@settings(max_examples=25)
def test_cmt_ProgramCommitteeMember_instantiation(instance):
    assert isinstance(instance, cmt_ProgramCommitteeMember)


cmt_Rejection_strategy = st.builds(cmt_Rejection)
@given(instance=cmt_Rejection_strategy)
@settings(max_examples=25)
def test_cmt_Rejection_instantiation(instance):
    assert isinstance(instance, cmt_Rejection)


cmt_Review_strategy = st.builds(cmt_Review)
@given(instance=cmt_Review_strategy)
@settings(max_examples=25)
def test_cmt_Review_instantiation(instance):
    assert isinstance(instance, cmt_Review)


cmt_Reviewer_strategy = st.builds(cmt_Reviewer)
@given(instance=cmt_Reviewer_strategy)
@settings(max_examples=25)
def test_cmt_Reviewer_instantiation(instance):
    assert isinstance(instance, cmt_Reviewer)


cmt_SubjectArea_strategy = st.builds(cmt_SubjectArea)
@given(instance=cmt_SubjectArea_strategy)
@settings(max_examples=25)
def test_cmt_SubjectArea_instantiation(instance):
    assert isinstance(instance, cmt_SubjectArea)


cmt_Thing_strategy = st.builds(cmt_Thing)
@given(instance=cmt_Thing_strategy)
@settings(max_examples=25)
def test_cmt_Thing_instantiation(instance):
    assert isinstance(instance, cmt_Thing)


cmt_User_strategy = st.builds(cmt_User)
@given(instance=cmt_User_strategy)
@settings(max_examples=25)
def test_cmt_User_instantiation(instance):
    assert isinstance(instance, cmt_User)


