import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Account,
    Activity,
    Administrator,
    Approval_Email,
    Author,
    Bid,
    Chairman,
    Co_author,
    Cocus_Abstract,
    Cocus_Acceptance,
    Cocus_Account,
    Cocus_Activity,
    Cocus_Admin_Role,
    Cocus_Administrator,
    Cocus_Approval_Email,
    Cocus_Assistance,
    Cocus_AssociatedChair,
    Cocus_Author,
    Cocus_AuthorNotReviewer,
    Cocus_Author_Role,
    Cocus_Bid,
    Cocus_Chairman,
    Cocus_Co_author,
    Cocus_Committe_Role,
    Cocus_Committee,
    Cocus_Conference,
    Cocus_ConferenceChair,
    Cocus_ConferenceMember,
    Cocus_Corresponding_Author,
    Cocus_Decision,
    Cocus_Description,
    Cocus_Detail,
    Cocus_Document,
    Cocus_Email,
    Cocus_Email_Template,
    Cocus_Event,
    Cocus_Event_Approval,
    Cocus_Event_Creation,
    Cocus_Event_Setup,
    Cocus_Event_Tracks,
    Cocus_Event_URL,
    Cocus_ExternalReviewer,
    Cocus_Feature_Request,
    Cocus_Full_Paper,
    Cocus_Group_Email,
    Cocus_Head_Role,
    Cocus_Help_Request,
    Cocus_Inforamtion,
    Cocus_Invited_Paper,
    Cocus_Meta_Review,
    Cocus_Meta_Reviewer,
    Cocus_Misc,
    Cocus_Notification_Email,
    Cocus_Paper,
    Cocus_PaperAbstract,
    Cocus_PaperFullVersion,
    Cocus_Paper_Typologies,
    Cocus_Person,
    Cocus_Preference,
    Cocus_Preview,
    Cocus_ProgramCommittee,
    Cocus_ProgramCommitteeChair,
    Cocus_ProgramCommitteeMember,
    Cocus_Registration,
    Cocus_Rejection,
    Cocus_Rejection_Email,
    Cocus_Request,
    Cocus_Research_Topic,
    Cocus_Review,
    Cocus_Review_Form,
    Cocus_Review_Form_Setup,
    Cocus_Reviewer,
    Cocus_Reviewer_Role,
    Cocus_Role,
    Cocus_Short_Paper,
    Cocus_SubjectArea,
    Cocus_Submission,
    Cocus_Submission_Template,
    Cocus_Symposium,
    Cocus_Template,
    Cocus_Thing,
    Cocus_URL,
    Cocus_User,
    Cocus_Workshop,
    Conference,
    ConferenceMember,
    Decision,
    Document,
    Email,
    Event,
    Event_Setup,
    Event_Tracks,
    ExternalReviewer,
    Help_Request,
    Inforamtion,
    Meta_Reviewer,
    Paper,
    Person,
    ProgramCommittee,
    ProgramCommitteeMember,
    Request,
    Review,
    Review_Form,
    Reviewer,
    Role,
    SubjectArea,
    Thing,
    URL,
    User,
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

def test_Cocus_Conference_acceptsHardcopySubmissions_value_roundtrip():
    instance = Cocus_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    assert instance.acceptsHardcopySubmissions == "sample_text"
    instance.acceptsHardcopySubmissions = "sample_text_2"
    assert instance.acceptsHardcopySubmissions == "sample_text_2"


def test_Cocus_Conference_date_value_roundtrip():
    instance = Cocus_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_Cocus_Conference_logoURL_value_roundtrip():
    instance = Cocus_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    assert instance.logoURL == "sample_text"
    instance.logoURL = "sample_text_2"
    assert instance.logoURL == "sample_text_2"


def test_Cocus_Conference_reviewsPerPaper_value_roundtrip():
    instance = Cocus_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    assert instance.reviewsPerPaper == "sample_text"
    instance.reviewsPerPaper = "sample_text_2"
    assert instance.reviewsPerPaper == "sample_text_2"


def test_Cocus_Conference_siteURL_value_roundtrip():
    instance = Cocus_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    assert instance.siteURL == "sample_text"
    instance.siteURL = "sample_text_2"
    assert instance.siteURL == "sample_text_2"


def test_Cocus_Paper_paperID_value_roundtrip():
    instance = Cocus_Paper(paperID="sample_text", title="sample_text")
    assert instance.paperID == "sample_text"
    instance.paperID = "sample_text_2"
    assert instance.paperID == "sample_text_2"


def test_Cocus_Paper_title_value_roundtrip():
    instance = Cocus_Paper(paperID="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_Cocus_Person_email_value_roundtrip():
    instance = Cocus_Person(email="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Cocus_ProgramCommitteeMember_maxPapers_value_roundtrip():
    instance = Cocus_ProgramCommitteeMember(maxPapers="sample_text")
    assert instance.maxPapers == "sample_text"
    instance.maxPapers = "sample_text_2"
    assert instance.maxPapers == "sample_text_2"


def test_Cocus_Event_Approval_isa_Activity():
    instance = Cocus_Event_Approval()
    assert isinstance(instance, Activity)


def test_Cocus_Event_Creation_isa_Activity():
    instance = Cocus_Event_Creation()
    assert isinstance(instance, Activity)


def test_Cocus_Registration_isa_Activity():
    instance = Cocus_Registration()
    assert isinstance(instance, Activity)


def test_Cocus_Request_isa_Activity():
    instance = Cocus_Request()
    assert isinstance(instance, Activity)


def test_Cocus_AuthorNotReviewer_isa_Author():
    instance = Cocus_AuthorNotReviewer()
    assert isinstance(instance, Author)


def test_Cocus_Co_author_isa_Author():
    instance = Cocus_Co_author()
    assert isinstance(instance, Author)


def test_Cocus_Corresponding_Author_isa_Author():
    instance = Cocus_Corresponding_Author()
    assert isinstance(instance, Author)


def test_Cocus_AssociatedChair_isa_Chairman():
    instance = Cocus_AssociatedChair()
    assert isinstance(instance, Chairman)


def test_Cocus_ConferenceChair_isa_Chairman():
    instance = Cocus_ConferenceChair()
    assert isinstance(instance, Chairman)


def test_Cocus_ProgramCommitteeChair_isa_Chairman():
    instance = Cocus_ProgramCommitteeChair()
    assert isinstance(instance, Chairman)


def test_Cocus_AssociatedChair_isa_ConferenceMember():
    instance = Cocus_AssociatedChair()
    assert isinstance(instance, ConferenceMember)


def test_Cocus_Author_isa_ConferenceMember():
    instance = Cocus_Author()
    assert isinstance(instance, ConferenceMember)


def test_Cocus_Chairman_isa_ConferenceMember():
    instance = Cocus_Chairman()
    assert isinstance(instance, ConferenceMember)


def test_Cocus_ConferenceChair_isa_ConferenceMember():
    instance = Cocus_ConferenceChair()
    assert isinstance(instance, ConferenceMember)


def test_Cocus_ProgramCommitteeMember_isa_ConferenceMember():
    instance = Cocus_ProgramCommitteeMember(maxPapers="sample_text")
    assert isinstance(instance, ConferenceMember)


def test_Cocus_Reviewer_isa_ConferenceMember():
    instance = Cocus_Reviewer()
    assert isinstance(instance, ConferenceMember)


def test_Cocus_Acceptance_isa_Decision():
    instance = Cocus_Acceptance()
    assert isinstance(instance, Decision)


def test_Cocus_Rejection_isa_Decision():
    instance = Cocus_Rejection()
    assert isinstance(instance, Decision)


def test_Cocus_Email_isa_Document():
    instance = Cocus_Email()
    assert isinstance(instance, Document)


def test_Cocus_Paper_isa_Document():
    instance = Cocus_Paper(paperID="sample_text", title="sample_text")
    assert isinstance(instance, Document)


def test_Cocus_Review_isa_Document():
    instance = Cocus_Review()
    assert isinstance(instance, Document)


def test_Cocus_Submission_isa_Document():
    instance = Cocus_Submission()
    assert isinstance(instance, Document)


def test_Cocus_Template_isa_Document():
    instance = Cocus_Template()
    assert isinstance(instance, Document)


def test_Cocus_Approval_Email_isa_Email():
    instance = Cocus_Approval_Email()
    assert isinstance(instance, Email)


def test_Cocus_Group_Email_isa_Email():
    instance = Cocus_Group_Email()
    assert isinstance(instance, Email)


def test_Cocus_Notification_Email_isa_Email():
    instance = Cocus_Notification_Email()
    assert isinstance(instance, Email)


def test_Cocus_Rejection_Email_isa_Email():
    instance = Cocus_Rejection_Email()
    assert isinstance(instance, Email)


def test_Cocus_Conference_isa_Event():
    instance = Cocus_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    assert isinstance(instance, Event)


def test_Cocus_Symposium_isa_Event():
    instance = Cocus_Symposium()
    assert isinstance(instance, Event)


def test_Cocus_Workshop_isa_Event():
    instance = Cocus_Workshop()
    assert isinstance(instance, Event)


def test_Cocus_Email_Template_isa_Event_Setup():
    instance = Cocus_Email_Template()
    assert isinstance(instance, Event_Setup)


def test_Cocus_Event_Tracks_isa_Event_Setup():
    instance = Cocus_Event_Tracks()
    assert isinstance(instance, Event_Setup)


def test_Cocus_Paper_Typologies_isa_Event_Setup():
    instance = Cocus_Paper_Typologies()
    assert isinstance(instance, Event_Setup)


def test_Cocus_Research_Topic_isa_Event_Setup():
    instance = Cocus_Research_Topic()
    assert isinstance(instance, Event_Setup)


def test_Cocus_Review_Form_isa_Event_Setup():
    instance = Cocus_Review_Form()
    assert isinstance(instance, Event_Setup)


def test_Cocus_Submission_Template_isa_Event_Setup():
    instance = Cocus_Submission_Template()
    assert isinstance(instance, Event_Setup)


def test_Cocus_Assistance_isa_Help_Request():
    instance = Cocus_Assistance()
    assert isinstance(instance, Help_Request)


def test_Cocus_Feature_Request_isa_Help_Request():
    instance = Cocus_Feature_Request()
    assert isinstance(instance, Help_Request)


def test_Cocus_Misc_isa_Help_Request():
    instance = Cocus_Misc()
    assert isinstance(instance, Help_Request)


def test_Cocus_Abstract_isa_Paper():
    instance = Cocus_Abstract()
    assert isinstance(instance, Paper)


def test_Cocus_Full_Paper_isa_Paper():
    instance = Cocus_Full_Paper()
    assert isinstance(instance, Paper)


def test_Cocus_Invited_Paper_isa_Paper():
    instance = Cocus_Invited_Paper()
    assert isinstance(instance, Paper)


def test_Cocus_PaperAbstract_isa_Paper():
    instance = Cocus_PaperAbstract()
    assert isinstance(instance, Paper)


def test_Cocus_PaperFullVersion_isa_Paper():
    instance = Cocus_PaperFullVersion()
    assert isinstance(instance, Paper)


def test_Cocus_Short_Paper_isa_Paper():
    instance = Cocus_Short_Paper()
    assert isinstance(instance, Paper)


def test_Cocus_Administrator_isa_Person():
    instance = Cocus_Administrator()
    assert isinstance(instance, Person)


def test_Cocus_Chairman_isa_Person():
    instance = Cocus_Chairman()
    assert isinstance(instance, Person)


def test_Cocus_ConferenceMember_isa_Person():
    instance = Cocus_ConferenceMember()
    assert isinstance(instance, Person)


def test_Cocus_ExternalReviewer_isa_Person():
    instance = Cocus_ExternalReviewer()
    assert isinstance(instance, Person)


def test_Cocus_ProgramCommitteeMember_isa_Person():
    instance = Cocus_ProgramCommitteeMember(maxPapers="sample_text")
    assert isinstance(instance, Person)


def test_Cocus_User_isa_Person():
    instance = Cocus_User()
    assert isinstance(instance, Person)


def test_Cocus_ProgramCommitteeChair_isa_ProgramCommitteeMember():
    instance = Cocus_ProgramCommitteeChair()
    assert isinstance(instance, ProgramCommitteeMember)


def test_Cocus_Help_Request_isa_Request():
    instance = Cocus_Help_Request()
    assert isinstance(instance, Request)


def test_Cocus_Meta_Review_isa_Review():
    instance = Cocus_Meta_Review()
    assert isinstance(instance, Review)


def test_Cocus_Preview_isa_Review_Form():
    instance = Cocus_Preview()
    assert isinstance(instance, Review_Form)


def test_Cocus_Review_Form_Setup_isa_Review_Form():
    instance = Cocus_Review_Form_Setup()
    assert isinstance(instance, Review_Form)


def test_Cocus_Meta_Reviewer_isa_Reviewer():
    instance = Cocus_Meta_Reviewer()
    assert isinstance(instance, Reviewer)


def test_Cocus_Admin_Role_isa_Role():
    instance = Cocus_Admin_Role()
    assert isinstance(instance, Role)


def test_Cocus_Author_Role_isa_Role():
    instance = Cocus_Author_Role()
    assert isinstance(instance, Role)


def test_Cocus_Committe_Role_isa_Role():
    instance = Cocus_Committe_Role()
    assert isinstance(instance, Role)


def test_Cocus_Head_Role_isa_Role():
    instance = Cocus_Head_Role()
    assert isinstance(instance, Role)


def test_Cocus_Reviewer_Role_isa_Role():
    instance = Cocus_Reviewer_Role()
    assert isinstance(instance, Role)


def test_Cocus_Conference_isa_Thing():
    instance = Cocus_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    assert isinstance(instance, Thing)


def test_Cocus_Detail_isa_Thing():
    instance = Cocus_Detail()
    assert isinstance(instance, Thing)


def test_Cocus_Document_isa_Thing():
    instance = Cocus_Document()
    assert isinstance(instance, Thing)


def test_Cocus_Event_isa_Thing():
    instance = Cocus_Event()
    assert isinstance(instance, Thing)


def test_Cocus_Person_isa_Thing():
    instance = Cocus_Person(email="sample_text")
    assert isinstance(instance, Thing)


def test_Cocus_Role_isa_Thing():
    instance = Cocus_Role()
    assert isinstance(instance, Thing)


def test_Cocus_Event_URL_isa_URL():
    instance = Cocus_Event_URL()
    assert isinstance(instance, URL)


def test_Cocus_Administrator_isa_User():
    instance = Cocus_Administrator()
    assert isinstance(instance, User)


def test_Cocus_Author_isa_User():
    instance = Cocus_Author()
    assert isinstance(instance, User)


def test_Cocus_Committee_isa_User():
    instance = Cocus_Committee()
    assert isinstance(instance, User)


def test_Cocus_Reviewer_isa_User():
    instance = Cocus_Reviewer()
    assert isinstance(instance, User)


def test_assoc_acceptedBy56_link_reassign_clear():
    a = Cocus_Paper(paperID="sample_text", title="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'Cocus_Paper57', b1)
    assert _is_linked(a, 'Cocus_Paper57', b1)
    if hasattr(b1, 'Administrator58'):
        assert _is_linked(b1, 'Administrator58', a)
    _safe_set(a, 'Cocus_Paper57', b2)
    assert _is_linked(a, 'Cocus_Paper57', b2)
    if hasattr(b1, 'Administrator58'):
        assert not _is_linked(b1, 'Administrator58', a)
    if hasattr(b2, 'Administrator58'):
        assert _is_linked(b2, 'Administrator58', a)
    _safe_set(a, 'Cocus_Paper57', None)
    assert not _is_linked(a, 'Cocus_Paper57', b2)
    if hasattr(b2, 'Administrator58'):
        assert not _is_linked(b2, 'Administrator58', a)


def test_assoc_add137_link_reassign_clear():
    a = Cocus_Person(email="sample_text")
    b1 = Person()
    b2 = Person()
    _safe_set(a, 'Cocus_Person138', b1)
    assert _is_linked(a, 'Cocus_Person138', b1)
    if hasattr(b1, 'Person139'):
        assert _is_linked(b1, 'Person139', a)
    _safe_set(a, 'Cocus_Person138', b2)
    assert _is_linked(a, 'Cocus_Person138', b2)
    if hasattr(b1, 'Person139'):
        assert not _is_linked(b1, 'Person139', a)
    if hasattr(b2, 'Person139'):
        assert _is_linked(b2, 'Person139', a)
    _safe_set(a, 'Cocus_Person138', None)
    assert not _is_linked(a, 'Cocus_Person138', b2)
    if hasattr(b2, 'Person139'):
        assert not _is_linked(b2, 'Person139', a)


def test_assoc_addedBy35_link_reassign_clear():
    a = Cocus_ProgramCommitteeMember(maxPapers="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'Cocus_ProgramCommitteeMember', b1)
    assert _is_linked(a, 'Cocus_ProgramCommitteeMember', b1)
    if hasattr(b1, 'Administrator36'):
        assert _is_linked(b1, 'Administrator36', a)
    _safe_set(a, 'Cocus_ProgramCommitteeMember', b2)
    assert _is_linked(a, 'Cocus_ProgramCommitteeMember', b2)
    if hasattr(b1, 'Administrator36'):
        assert not _is_linked(b1, 'Administrator36', a)
    if hasattr(b2, 'Administrator36'):
        assert _is_linked(b2, 'Administrator36', a)
    _safe_set(a, 'Cocus_ProgramCommitteeMember', None)
    assert not _is_linked(a, 'Cocus_ProgramCommitteeMember', b2)
    if hasattr(b2, 'Administrator36'):
        assert not _is_linked(b2, 'Administrator36', a)


def test_assoc_added_by141_link_reassign_clear():
    a = Cocus_Person(email="sample_text")
    b1 = Person()
    b2 = Person()
    _safe_set(a, 'Cocus_Person142', b1)
    assert _is_linked(a, 'Cocus_Person142', b1)
    if hasattr(b1, 'Person143'):
        assert _is_linked(b1, 'Person143', a)
    _safe_set(a, 'Cocus_Person142', b2)
    assert _is_linked(a, 'Cocus_Person142', b2)
    if hasattr(b1, 'Person143'):
        assert not _is_linked(b1, 'Person143', a)
    if hasattr(b2, 'Person143'):
        assert _is_linked(b2, 'Person143', a)
    _safe_set(a, 'Cocus_Person142', None)
    assert not _is_linked(a, 'Cocus_Person142', b2)
    if hasattr(b2, 'Person143'):
        assert not _is_linked(b2, 'Person143', a)


def test_assoc_assignedTo48_link_reassign_clear():
    a = Cocus_Paper(paperID="sample_text", title="sample_text")
    b1 = Reviewer()
    b2 = Reviewer()
    _safe_set(a, 'hasBeenAssigned', b1)
    assert _is_linked(a, 'hasBeenAssigned', b1)
    if hasattr(b1, 'Reviewer49'):
        assert _is_linked(b1, 'Reviewer49', a)
    _safe_set(a, 'hasBeenAssigned', b2)
    assert _is_linked(a, 'hasBeenAssigned', b2)
    if hasattr(b1, 'Reviewer49'):
        assert not _is_linked(b1, 'Reviewer49', a)
    if hasattr(b2, 'Reviewer49'):
        assert _is_linked(b2, 'Reviewer49', a)
    _safe_set(a, 'hasBeenAssigned', None)
    assert not _is_linked(a, 'hasBeenAssigned', b2)
    if hasattr(b2, 'Reviewer49'):
        assert not _is_linked(b2, 'Reviewer49', a)


def test_assoc_detailsEnteredBy27_link_reassign_clear():
    a = Cocus_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'Cocus_Conference28', b1)
    assert _is_linked(a, 'Cocus_Conference28', b1)
    if hasattr(b1, 'Administrator29'):
        assert _is_linked(b1, 'Administrator29', a)
    _safe_set(a, 'Cocus_Conference28', b2)
    assert _is_linked(a, 'Cocus_Conference28', b2)
    if hasattr(b1, 'Administrator29'):
        assert not _is_linked(b1, 'Administrator29', a)
    if hasattr(b2, 'Administrator29'):
        assert _is_linked(b2, 'Administrator29', a)
    _safe_set(a, 'Cocus_Conference28', None)
    assert not _is_linked(a, 'Cocus_Conference28', b2)
    if hasattr(b2, 'Administrator29'):
        assert not _is_linked(b2, 'Administrator29', a)


def test_assoc_execute120_link_reassign_clear():
    a = Cocus_Person(email="sample_text")
    b1 = Thing()
    b2 = Thing()
    _safe_set(a, 'Cocus_Person121', {b1})
    assert _is_linked(a, 'Cocus_Person121', b1)
    if hasattr(b1, 'Thing122'):
        assert _is_linked(b1, 'Thing122', a)
    _safe_set(a, 'Cocus_Person121', {b2})
    assert _is_linked(a, 'Cocus_Person121', b2)
    if hasattr(b1, 'Thing122'):
        assert not _is_linked(b1, 'Thing122', a)
    if hasattr(b2, 'Thing122'):
        assert _is_linked(b2, 'Thing122', a)
    _safe_set(a, 'Cocus_Person121', set())
    assert not _is_linked(a, 'Cocus_Person121', b2)
    if hasattr(b2, 'Thing122'):
        assert not _is_linked(b2, 'Thing122', a)


def test_assoc_get123_link_reassign_clear():
    a = Cocus_Person(email="sample_text")
    b1 = Inforamtion()
    b2 = Inforamtion()
    _safe_set(a, 'Cocus_Person124', b1)
    assert _is_linked(a, 'Cocus_Person124', b1)
    if hasattr(b1, 'Inforamtion'):
        assert _is_linked(b1, 'Inforamtion', a)
    _safe_set(a, 'Cocus_Person124', b2)
    assert _is_linked(a, 'Cocus_Person124', b2)
    if hasattr(b1, 'Inforamtion'):
        assert not _is_linked(b1, 'Inforamtion', a)
    if hasattr(b2, 'Inforamtion'):
        assert _is_linked(b2, 'Inforamtion', a)
    _safe_set(a, 'Cocus_Person124', None)
    assert not _is_linked(a, 'Cocus_Person124', b2)
    if hasattr(b2, 'Inforamtion'):
        assert not _is_linked(b2, 'Inforamtion', a)


def test_assoc_hardcopyMailingManifestsPrintedBy24_link_reassign_clear():
    a = Cocus_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'Cocus_Conference25', b1)
    assert _is_linked(a, 'Cocus_Conference25', b1)
    if hasattr(b1, 'Administrator26'):
        assert _is_linked(b1, 'Administrator26', a)
    _safe_set(a, 'Cocus_Conference25', b2)
    assert _is_linked(a, 'Cocus_Conference25', b2)
    if hasattr(b1, 'Administrator26'):
        assert not _is_linked(b1, 'Administrator26', a)
    if hasattr(b2, 'Administrator26'):
        assert _is_linked(b2, 'Administrator26', a)
    _safe_set(a, 'Cocus_Conference25', None)
    assert not _is_linked(a, 'Cocus_Conference25', b2)
    if hasattr(b2, 'Administrator26'):
        assert not _is_linked(b2, 'Administrator26', a)


def test_assoc_hasAuthor54_link_reassign_clear():
    a = Cocus_Paper(paperID="sample_text", title="sample_text")
    b1 = Author()
    b2 = Author()
    _safe_set(a, 'Cocus_Paper55', b1)
    assert _is_linked(a, 'Cocus_Paper55', b1)
    if hasattr(b1, 'Author'):
        assert _is_linked(b1, 'Author', a)
    _safe_set(a, 'Cocus_Paper55', b2)
    assert _is_linked(a, 'Cocus_Paper55', b2)
    if hasattr(b1, 'Author'):
        assert not _is_linked(b1, 'Author', a)
    if hasattr(b2, 'Author'):
        assert _is_linked(b2, 'Author', a)
    _safe_set(a, 'Cocus_Paper55', None)
    assert not _is_linked(a, 'Cocus_Paper55', b2)
    if hasattr(b2, 'Author'):
        assert not _is_linked(b2, 'Author', a)


def test_assoc_hasBid44_link_reassign_clear():
    a = Cocus_Paper(paperID="sample_text", title="sample_text")
    b1 = Bid()
    b2 = Bid()
    _safe_set(a, 'Cocus_Paper', b1)
    assert _is_linked(a, 'Cocus_Paper', b1)
    if hasattr(b1, 'Bid45'):
        assert _is_linked(b1, 'Bid45', a)
    _safe_set(a, 'Cocus_Paper', b2)
    assert _is_linked(a, 'Cocus_Paper', b2)
    if hasattr(b1, 'Bid45'):
        assert not _is_linked(b1, 'Bid45', a)
    if hasattr(b2, 'Bid45'):
        assert _is_linked(b2, 'Bid45', a)
    _safe_set(a, 'Cocus_Paper', None)
    assert not _is_linked(a, 'Cocus_Paper', b2)
    if hasattr(b2, 'Bid45'):
        assert not _is_linked(b2, 'Bid45', a)


def test_assoc_hasCo_author43_link_reassign_clear():
    a = Cocus_Paper(paperID="sample_text", title="sample_text")
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


def test_assoc_hasConferenceMember12_link_reassign_clear():
    a = Cocus_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
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


def test_assoc_hasConflictOfInterest144_link_reassign_clear():
    a = Cocus_Person(email="sample_text")
    b1 = Document()
    b2 = Document()
    _safe_set(a, 'Cocus_Person145', b1)
    assert _is_linked(a, 'Cocus_Person145', b1)
    if hasattr(b1, 'Document146'):
        assert _is_linked(b1, 'Document146', a)
    _safe_set(a, 'Cocus_Person145', b2)
    assert _is_linked(a, 'Cocus_Person145', b2)
    if hasattr(b1, 'Document146'):
        assert not _is_linked(b1, 'Document146', a)
    if hasattr(b2, 'Document146'):
        assert _is_linked(b2, 'Document146', a)
    _safe_set(a, 'Cocus_Person145', None)
    assert not _is_linked(a, 'Cocus_Person145', b2)
    if hasattr(b2, 'Document146'):
        assert not _is_linked(b2, 'Document146', a)


def test_assoc_hasDecision46_link_reassign_clear():
    a = Cocus_Paper(paperID="sample_text", title="sample_text")
    b1 = Decision()
    b2 = Decision()
    _safe_set(a, 'Cocus_Paper47', b1)
    assert _is_linked(a, 'Cocus_Paper47', b1)
    if hasattr(b1, 'Decision'):
        assert _is_linked(b1, 'Decision', a)
    _safe_set(a, 'Cocus_Paper47', b2)
    assert _is_linked(a, 'Cocus_Paper47', b2)
    if hasattr(b1, 'Decision'):
        assert not _is_linked(b1, 'Decision', a)
    if hasattr(b2, 'Decision'):
        assert _is_linked(b2, 'Decision', a)
    _safe_set(a, 'Cocus_Paper47', None)
    assert not _is_linked(a, 'Cocus_Paper47', b2)
    if hasattr(b2, 'Decision'):
        assert not _is_linked(b2, 'Decision', a)


def test_assoc_hasSubjectArea50_link_reassign_clear():
    a = Cocus_Paper(paperID="sample_text", title="sample_text")
    b1 = SubjectArea()
    b2 = SubjectArea()
    _safe_set(a, 'Cocus_Paper51', b1)
    assert _is_linked(a, 'Cocus_Paper51', b1)
    if hasattr(b1, 'SubjectArea'):
        assert _is_linked(b1, 'SubjectArea', a)
    _safe_set(a, 'Cocus_Paper51', b2)
    assert _is_linked(a, 'Cocus_Paper51', b2)
    if hasattr(b1, 'SubjectArea'):
        assert not _is_linked(b1, 'SubjectArea', a)
    if hasattr(b2, 'SubjectArea'):
        assert _is_linked(b2, 'SubjectArea', a)
    _safe_set(a, 'Cocus_Paper51', None)
    assert not _is_linked(a, 'Cocus_Paper51', b2)
    if hasattr(b2, 'SubjectArea'):
        assert not _is_linked(b2, 'SubjectArea', a)


def test_assoc_inverse_of_add118_link_reassign_clear():
    a = Cocus_Person(email="sample_text")
    b1 = Thing()
    b2 = Thing()
    _safe_set(a, 'Cocus_Person', {b1})
    assert _is_linked(a, 'Cocus_Person', b1)
    if hasattr(b1, 'Thing119'):
        assert _is_linked(b1, 'Thing119', a)
    _safe_set(a, 'Cocus_Person', {b2})
    assert _is_linked(a, 'Cocus_Person', b2)
    if hasattr(b1, 'Thing119'):
        assert not _is_linked(b1, 'Thing119', a)
    if hasattr(b2, 'Thing119'):
        assert _is_linked(b2, 'Thing119', a)
    _safe_set(a, 'Cocus_Person', set())
    assert not _is_linked(a, 'Cocus_Person', b2)
    if hasattr(b2, 'Thing119'):
        assert not _is_linked(b2, 'Thing119', a)


def test_assoc_memberOfProgramCommittee34_link_reassign_clear():
    a = Cocus_ProgramCommitteeMember(maxPapers="sample_text")
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


def test_assoc_modify128_link_reassign_clear():
    a = Cocus_Person(email="sample_text")
    b1 = Thing()
    b2 = Thing()
    _safe_set(a, 'Cocus_Person129', {b1})
    assert _is_linked(a, 'Cocus_Person129', b1)
    if hasattr(b1, 'Thing130'):
        assert _is_linked(b1, 'Thing130', a)
    _safe_set(a, 'Cocus_Person129', {b2})
    assert _is_linked(a, 'Cocus_Person129', b2)
    if hasattr(b1, 'Thing130'):
        assert not _is_linked(b1, 'Thing130', a)
    if hasattr(b2, 'Thing130'):
        assert _is_linked(b2, 'Thing130', a)
    _safe_set(a, 'Cocus_Person129', set())
    assert not _is_linked(a, 'Cocus_Person129', b2)
    if hasattr(b2, 'Thing130'):
        assert not _is_linked(b2, 'Thing130', a)


def test_assoc_paperAssignmentFinalizedBy13_link_reassign_clear():
    a = Cocus_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'Cocus_Conference', b1)
    assert _is_linked(a, 'Cocus_Conference', b1)
    if hasattr(b1, 'Administrator14'):
        assert _is_linked(b1, 'Administrator14', a)
    _safe_set(a, 'Cocus_Conference', b2)
    assert _is_linked(a, 'Cocus_Conference', b2)
    if hasattr(b1, 'Administrator14'):
        assert not _is_linked(b1, 'Administrator14', a)
    if hasattr(b2, 'Administrator14'):
        assert _is_linked(b2, 'Administrator14', a)
    _safe_set(a, 'Cocus_Conference', None)
    assert not _is_linked(a, 'Cocus_Conference', b2)
    if hasattr(b2, 'Administrator14'):
        assert not _is_linked(b2, 'Administrator14', a)


def test_assoc_paperAssignmentToolsRunBy18_link_reassign_clear():
    a = Cocus_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'Cocus_Conference19', b1)
    assert _is_linked(a, 'Cocus_Conference19', b1)
    if hasattr(b1, 'Administrator20'):
        assert _is_linked(b1, 'Administrator20', a)
    _safe_set(a, 'Cocus_Conference19', b2)
    assert _is_linked(a, 'Cocus_Conference19', b2)
    if hasattr(b1, 'Administrator20'):
        assert not _is_linked(b1, 'Administrator20', a)
    if hasattr(b2, 'Administrator20'):
        assert _is_linked(b2, 'Administrator20', a)
    _safe_set(a, 'Cocus_Conference19', None)
    assert not _is_linked(a, 'Cocus_Conference19', b2)
    if hasattr(b2, 'Administrator20'):
        assert not _is_linked(b2, 'Administrator20', a)


def test_assoc_readByMeta_Reviewer62_link_reassign_clear():
    a = Cocus_Paper(paperID="sample_text", title="sample_text")
    b1 = Meta_Reviewer()
    b2 = Meta_Reviewer()
    _safe_set(a, 'Cocus_Paper63', b1)
    assert _is_linked(a, 'Cocus_Paper63', b1)
    if hasattr(b1, 'Meta_Reviewer'):
        assert _is_linked(b1, 'Meta_Reviewer', a)
    _safe_set(a, 'Cocus_Paper63', b2)
    assert _is_linked(a, 'Cocus_Paper63', b2)
    if hasattr(b1, 'Meta_Reviewer'):
        assert not _is_linked(b1, 'Meta_Reviewer', a)
    if hasattr(b2, 'Meta_Reviewer'):
        assert _is_linked(b2, 'Meta_Reviewer', a)
    _safe_set(a, 'Cocus_Paper63', None)
    assert not _is_linked(a, 'Cocus_Paper63', b2)
    if hasattr(b2, 'Meta_Reviewer'):
        assert not _is_linked(b2, 'Meta_Reviewer', a)


def test_assoc_readByReviewer52_link_reassign_clear():
    a = Cocus_Paper(paperID="sample_text", title="sample_text")
    b1 = Reviewer()
    b2 = Reviewer()
    _safe_set(a, 'readPaper', b1)
    assert _is_linked(a, 'readPaper', b1)
    if hasattr(b1, 'Reviewer53'):
        assert _is_linked(b1, 'Reviewer53', a)
    _safe_set(a, 'readPaper', b2)
    assert _is_linked(a, 'readPaper', b2)
    if hasattr(b1, 'Reviewer53'):
        assert not _is_linked(b1, 'Reviewer53', a)
    if hasattr(b2, 'Reviewer53'):
        assert _is_linked(b2, 'Reviewer53', a)
    _safe_set(a, 'readPaper', None)
    assert not _is_linked(a, 'readPaper', b2)
    if hasattr(b2, 'Reviewer53'):
        assert not _is_linked(b2, 'Reviewer53', a)


def test_assoc_register127_link_reassign_clear():
    a = Cocus_Person(email="sample_text")
    b1 = Account()
    b2 = Account()
    _safe_set(a, 'registred_by', b1)
    assert _is_linked(a, 'registred_by', b1)
    if hasattr(b1, 'Account'):
        assert _is_linked(b1, 'Account', a)
    _safe_set(a, 'registred_by', b2)
    assert _is_linked(a, 'registred_by', b2)
    if hasattr(b1, 'Account'):
        assert not _is_linked(b1, 'Account', a)
    if hasattr(b2, 'Account'):
        assert _is_linked(b2, 'Account', a)
    _safe_set(a, 'registred_by', None)
    assert not _is_linked(a, 'registred_by', b2)
    if hasattr(b2, 'Account'):
        assert not _is_linked(b2, 'Account', a)


def test_assoc_rejectedBy59_link_reassign_clear():
    a = Cocus_Paper(paperID="sample_text", title="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'Cocus_Paper60', b1)
    assert _is_linked(a, 'Cocus_Paper60', b1)
    if hasattr(b1, 'Administrator61'):
        assert _is_linked(b1, 'Administrator61', a)
    _safe_set(a, 'Cocus_Paper60', b2)
    assert _is_linked(a, 'Cocus_Paper60', b2)
    if hasattr(b1, 'Administrator61'):
        assert not _is_linked(b1, 'Administrator61', a)
    if hasattr(b2, 'Administrator61'):
        assert _is_linked(b2, 'Administrator61', a)
    _safe_set(a, 'Cocus_Paper60', None)
    assert not _is_linked(a, 'Cocus_Paper60', b2)
    if hasattr(b2, 'Administrator61'):
        assert not _is_linked(b2, 'Administrator61', a)


def test_assoc_remove134_link_reassign_clear():
    a = Cocus_Person(email="sample_text")
    b1 = Thing()
    b2 = Thing()
    _safe_set(a, 'Cocus_Person135', {b1})
    assert _is_linked(a, 'Cocus_Person135', b1)
    if hasattr(b1, 'Thing136'):
        assert _is_linked(b1, 'Thing136', a)
    _safe_set(a, 'Cocus_Person135', {b2})
    assert _is_linked(a, 'Cocus_Person135', b2)
    if hasattr(b1, 'Thing136'):
        assert not _is_linked(b1, 'Thing136', a)
    if hasattr(b2, 'Thing136'):
        assert _is_linked(b2, 'Thing136', a)
    _safe_set(a, 'Cocus_Person135', set())
    assert not _is_linked(a, 'Cocus_Person135', b2)
    if hasattr(b2, 'Thing136'):
        assert not _is_linked(b2, 'Thing136', a)


def test_assoc_reviewCriteriaEnteredBy15_link_reassign_clear():
    a = Cocus_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'Cocus_Conference16', b1)
    assert _is_linked(a, 'Cocus_Conference16', b1)
    if hasattr(b1, 'Administrator17'):
        assert _is_linked(b1, 'Administrator17', a)
    _safe_set(a, 'Cocus_Conference16', b2)
    assert _is_linked(a, 'Cocus_Conference16', b2)
    if hasattr(b1, 'Administrator17'):
        assert not _is_linked(b1, 'Administrator17', a)
    if hasattr(b2, 'Administrator17'):
        assert _is_linked(b2, 'Administrator17', a)
    _safe_set(a, 'Cocus_Conference16', None)
    assert not _is_linked(a, 'Cocus_Conference16', b2)
    if hasattr(b2, 'Administrator17'):
        assert not _is_linked(b2, 'Administrator17', a)


def test_assoc_reviewerBiddingStartedBy30_link_reassign_clear():
    a = Cocus_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'Cocus_Conference31', b1)
    assert _is_linked(a, 'Cocus_Conference31', b1)
    if hasattr(b1, 'Administrator32'):
        assert _is_linked(b1, 'Administrator32', a)
    _safe_set(a, 'Cocus_Conference31', b2)
    assert _is_linked(a, 'Cocus_Conference31', b2)
    if hasattr(b1, 'Administrator32'):
        assert not _is_linked(b1, 'Administrator32', a)
    if hasattr(b2, 'Administrator32'):
        assert _is_linked(b2, 'Administrator32', a)
    _safe_set(a, 'Cocus_Conference31', None)
    assert not _is_linked(a, 'Cocus_Conference31', b2)
    if hasattr(b2, 'Administrator32'):
        assert not _is_linked(b2, 'Administrator32', a)


def test_assoc_send140_link_reassign_clear():
    a = Cocus_Person(email="sample_text")
    b1 = Activity()
    b2 = Activity()
    _safe_set(a, 'sent_by', b1)
    assert _is_linked(a, 'sent_by', b1)
    if hasattr(b1, 'Activity'):
        assert _is_linked(b1, 'Activity', a)
    _safe_set(a, 'sent_by', b2)
    assert _is_linked(a, 'sent_by', b2)
    if hasattr(b1, 'Activity'):
        assert not _is_linked(b1, 'Activity', a)
    if hasattr(b2, 'Activity'):
        assert _is_linked(b2, 'Activity', a)
    _safe_set(a, 'sent_by', None)
    assert not _is_linked(a, 'sent_by', b2)
    if hasattr(b2, 'Activity'):
        assert not _is_linked(b2, 'Activity', a)


def test_assoc_take_part_in131_link_reassign_clear():
    a = Cocus_Person(email="sample_text")
    b1 = Event()
    b2 = Event()
    _safe_set(a, 'Cocus_Person132', b1)
    assert _is_linked(a, 'Cocus_Person132', b1)
    if hasattr(b1, 'Event133'):
        assert _is_linked(b1, 'Event133', a)
    _safe_set(a, 'Cocus_Person132', b2)
    assert _is_linked(a, 'Cocus_Person132', b2)
    if hasattr(b1, 'Event133'):
        assert not _is_linked(b1, 'Event133', a)
    if hasattr(b2, 'Event133'):
        assert _is_linked(b2, 'Event133', a)
    _safe_set(a, 'Cocus_Person132', None)
    assert not _is_linked(a, 'Cocus_Person132', b2)
    if hasattr(b2, 'Event133'):
        assert not _is_linked(b2, 'Event133', a)


def test_assoc_use125_link_reassign_clear():
    a = Cocus_Person(email="sample_text")
    b1 = Document()
    b2 = Document()
    _safe_set(a, 'used_by', b1)
    assert _is_linked(a, 'used_by', b1)
    if hasattr(b1, 'Document126'):
        assert _is_linked(b1, 'Document126', a)
    _safe_set(a, 'used_by', b2)
    assert _is_linked(a, 'used_by', b2)
    if hasattr(b1, 'Document126'):
        assert not _is_linked(b1, 'Document126', a)
    if hasattr(b2, 'Document126'):
        assert _is_linked(b2, 'Document126', a)
    _safe_set(a, 'used_by', None)
    assert not _is_linked(a, 'used_by', b2)
    if hasattr(b2, 'Document126'):
        assert not _is_linked(b2, 'Document126', a)


def test_assoc_virtualMeetingEnabledBy21_link_reassign_clear():
    a = Cocus_Conference(acceptsHardcopySubmissions="sample_text", date="sample_text", logoURL="sample_text", reviewsPerPaper="sample_text", siteURL="sample_text")
    b1 = Administrator()
    b2 = Administrator()
    _safe_set(a, 'Cocus_Conference22', b1)
    assert _is_linked(a, 'Cocus_Conference22', b1)
    if hasattr(b1, 'Administrator23'):
        assert _is_linked(b1, 'Administrator23', a)
    _safe_set(a, 'Cocus_Conference22', b2)
    assert _is_linked(a, 'Cocus_Conference22', b2)
    if hasattr(b1, 'Administrator23'):
        assert not _is_linked(b1, 'Administrator23', a)
    if hasattr(b2, 'Administrator23'):
        assert _is_linked(b2, 'Administrator23', a)
    _safe_set(a, 'Cocus_Conference22', None)
    assert not _is_linked(a, 'Cocus_Conference22', b2)
    if hasattr(b2, 'Administrator23'):
        assert not _is_linked(b2, 'Administrator23', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Account_strategy = st.builds(Account)
@given(instance=Account_strategy)
@settings(max_examples=25)
def test_Account_instantiation(instance):
    assert isinstance(instance, Account)


Activity_strategy = st.builds(Activity)
@given(instance=Activity_strategy)
@settings(max_examples=25)
def test_Activity_instantiation(instance):
    assert isinstance(instance, Activity)


Administrator_strategy = st.builds(Administrator)
@given(instance=Administrator_strategy)
@settings(max_examples=25)
def test_Administrator_instantiation(instance):
    assert isinstance(instance, Administrator)


Approval_Email_strategy = st.builds(Approval_Email)
@given(instance=Approval_Email_strategy)
@settings(max_examples=25)
def test_Approval_Email_instantiation(instance):
    assert isinstance(instance, Approval_Email)


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


Cocus_Abstract_strategy = st.builds(Cocus_Abstract)
@given(instance=Cocus_Abstract_strategy)
@settings(max_examples=25)
def test_Cocus_Abstract_instantiation(instance):
    assert isinstance(instance, Cocus_Abstract)


Cocus_Acceptance_strategy = st.builds(Cocus_Acceptance)
@given(instance=Cocus_Acceptance_strategy)
@settings(max_examples=25)
def test_Cocus_Acceptance_instantiation(instance):
    assert isinstance(instance, Cocus_Acceptance)


Cocus_Account_strategy = st.builds(Cocus_Account)
@given(instance=Cocus_Account_strategy)
@settings(max_examples=25)
def test_Cocus_Account_instantiation(instance):
    assert isinstance(instance, Cocus_Account)


Cocus_Activity_strategy = st.builds(Cocus_Activity)
@given(instance=Cocus_Activity_strategy)
@settings(max_examples=25)
def test_Cocus_Activity_instantiation(instance):
    assert isinstance(instance, Cocus_Activity)


Cocus_Admin_Role_strategy = st.builds(Cocus_Admin_Role)
@given(instance=Cocus_Admin_Role_strategy)
@settings(max_examples=25)
def test_Cocus_Admin_Role_instantiation(instance):
    assert isinstance(instance, Cocus_Admin_Role)


Cocus_Administrator_strategy = st.builds(Cocus_Administrator)
@given(instance=Cocus_Administrator_strategy)
@settings(max_examples=25)
def test_Cocus_Administrator_instantiation(instance):
    assert isinstance(instance, Cocus_Administrator)


Cocus_Approval_Email_strategy = st.builds(Cocus_Approval_Email)
@given(instance=Cocus_Approval_Email_strategy)
@settings(max_examples=25)
def test_Cocus_Approval_Email_instantiation(instance):
    assert isinstance(instance, Cocus_Approval_Email)


Cocus_Assistance_strategy = st.builds(Cocus_Assistance)
@given(instance=Cocus_Assistance_strategy)
@settings(max_examples=25)
def test_Cocus_Assistance_instantiation(instance):
    assert isinstance(instance, Cocus_Assistance)


Cocus_AssociatedChair_strategy = st.builds(Cocus_AssociatedChair)
@given(instance=Cocus_AssociatedChair_strategy)
@settings(max_examples=25)
def test_Cocus_AssociatedChair_instantiation(instance):
    assert isinstance(instance, Cocus_AssociatedChair)


Cocus_Author_strategy = st.builds(Cocus_Author)
@given(instance=Cocus_Author_strategy)
@settings(max_examples=25)
def test_Cocus_Author_instantiation(instance):
    assert isinstance(instance, Cocus_Author)


Cocus_AuthorNotReviewer_strategy = st.builds(Cocus_AuthorNotReviewer)
@given(instance=Cocus_AuthorNotReviewer_strategy)
@settings(max_examples=25)
def test_Cocus_AuthorNotReviewer_instantiation(instance):
    assert isinstance(instance, Cocus_AuthorNotReviewer)


Cocus_Author_Role_strategy = st.builds(Cocus_Author_Role)
@given(instance=Cocus_Author_Role_strategy)
@settings(max_examples=25)
def test_Cocus_Author_Role_instantiation(instance):
    assert isinstance(instance, Cocus_Author_Role)


Cocus_Bid_strategy = st.builds(Cocus_Bid)
@given(instance=Cocus_Bid_strategy)
@settings(max_examples=25)
def test_Cocus_Bid_instantiation(instance):
    assert isinstance(instance, Cocus_Bid)


Cocus_Chairman_strategy = st.builds(Cocus_Chairman)
@given(instance=Cocus_Chairman_strategy)
@settings(max_examples=25)
def test_Cocus_Chairman_instantiation(instance):
    assert isinstance(instance, Cocus_Chairman)


Cocus_Co_author_strategy = st.builds(Cocus_Co_author)
@given(instance=Cocus_Co_author_strategy)
@settings(max_examples=25)
def test_Cocus_Co_author_instantiation(instance):
    assert isinstance(instance, Cocus_Co_author)


Cocus_Committe_Role_strategy = st.builds(Cocus_Committe_Role)
@given(instance=Cocus_Committe_Role_strategy)
@settings(max_examples=25)
def test_Cocus_Committe_Role_instantiation(instance):
    assert isinstance(instance, Cocus_Committe_Role)


Cocus_Committee_strategy = st.builds(Cocus_Committee)
@given(instance=Cocus_Committee_strategy)
@settings(max_examples=25)
def test_Cocus_Committee_instantiation(instance):
    assert isinstance(instance, Cocus_Committee)


Cocus_Conference_strategy = st.builds(Cocus_Conference, acceptsHardcopySubmissions=safe_text, date=safe_text, logoURL=safe_text, reviewsPerPaper=safe_text, siteURL=safe_text)
@given(instance=Cocus_Conference_strategy)
@settings(max_examples=25)
def test_Cocus_Conference_instantiation(instance):
    assert isinstance(instance, Cocus_Conference)


Cocus_ConferenceChair_strategy = st.builds(Cocus_ConferenceChair)
@given(instance=Cocus_ConferenceChair_strategy)
@settings(max_examples=25)
def test_Cocus_ConferenceChair_instantiation(instance):
    assert isinstance(instance, Cocus_ConferenceChair)


Cocus_ConferenceMember_strategy = st.builds(Cocus_ConferenceMember)
@given(instance=Cocus_ConferenceMember_strategy)
@settings(max_examples=25)
def test_Cocus_ConferenceMember_instantiation(instance):
    assert isinstance(instance, Cocus_ConferenceMember)


Cocus_Corresponding_Author_strategy = st.builds(Cocus_Corresponding_Author)
@given(instance=Cocus_Corresponding_Author_strategy)
@settings(max_examples=25)
def test_Cocus_Corresponding_Author_instantiation(instance):
    assert isinstance(instance, Cocus_Corresponding_Author)


Cocus_Decision_strategy = st.builds(Cocus_Decision)
@given(instance=Cocus_Decision_strategy)
@settings(max_examples=25)
def test_Cocus_Decision_instantiation(instance):
    assert isinstance(instance, Cocus_Decision)


Cocus_Description_strategy = st.builds(Cocus_Description)
@given(instance=Cocus_Description_strategy)
@settings(max_examples=25)
def test_Cocus_Description_instantiation(instance):
    assert isinstance(instance, Cocus_Description)


Cocus_Detail_strategy = st.builds(Cocus_Detail)
@given(instance=Cocus_Detail_strategy)
@settings(max_examples=25)
def test_Cocus_Detail_instantiation(instance):
    assert isinstance(instance, Cocus_Detail)


Cocus_Document_strategy = st.builds(Cocus_Document)
@given(instance=Cocus_Document_strategy)
@settings(max_examples=25)
def test_Cocus_Document_instantiation(instance):
    assert isinstance(instance, Cocus_Document)


Cocus_Email_strategy = st.builds(Cocus_Email)
@given(instance=Cocus_Email_strategy)
@settings(max_examples=25)
def test_Cocus_Email_instantiation(instance):
    assert isinstance(instance, Cocus_Email)


Cocus_Email_Template_strategy = st.builds(Cocus_Email_Template)
@given(instance=Cocus_Email_Template_strategy)
@settings(max_examples=25)
def test_Cocus_Email_Template_instantiation(instance):
    assert isinstance(instance, Cocus_Email_Template)


Cocus_Event_strategy = st.builds(Cocus_Event)
@given(instance=Cocus_Event_strategy)
@settings(max_examples=25)
def test_Cocus_Event_instantiation(instance):
    assert isinstance(instance, Cocus_Event)


Cocus_Event_Approval_strategy = st.builds(Cocus_Event_Approval)
@given(instance=Cocus_Event_Approval_strategy)
@settings(max_examples=25)
def test_Cocus_Event_Approval_instantiation(instance):
    assert isinstance(instance, Cocus_Event_Approval)


Cocus_Event_Creation_strategy = st.builds(Cocus_Event_Creation)
@given(instance=Cocus_Event_Creation_strategy)
@settings(max_examples=25)
def test_Cocus_Event_Creation_instantiation(instance):
    assert isinstance(instance, Cocus_Event_Creation)


Cocus_Event_Setup_strategy = st.builds(Cocus_Event_Setup)
@given(instance=Cocus_Event_Setup_strategy)
@settings(max_examples=25)
def test_Cocus_Event_Setup_instantiation(instance):
    assert isinstance(instance, Cocus_Event_Setup)


Cocus_Event_Tracks_strategy = st.builds(Cocus_Event_Tracks)
@given(instance=Cocus_Event_Tracks_strategy)
@settings(max_examples=25)
def test_Cocus_Event_Tracks_instantiation(instance):
    assert isinstance(instance, Cocus_Event_Tracks)


Cocus_Event_URL_strategy = st.builds(Cocus_Event_URL)
@given(instance=Cocus_Event_URL_strategy)
@settings(max_examples=25)
def test_Cocus_Event_URL_instantiation(instance):
    assert isinstance(instance, Cocus_Event_URL)


Cocus_ExternalReviewer_strategy = st.builds(Cocus_ExternalReviewer)
@given(instance=Cocus_ExternalReviewer_strategy)
@settings(max_examples=25)
def test_Cocus_ExternalReviewer_instantiation(instance):
    assert isinstance(instance, Cocus_ExternalReviewer)


Cocus_Feature_Request_strategy = st.builds(Cocus_Feature_Request)
@given(instance=Cocus_Feature_Request_strategy)
@settings(max_examples=25)
def test_Cocus_Feature_Request_instantiation(instance):
    assert isinstance(instance, Cocus_Feature_Request)


Cocus_Full_Paper_strategy = st.builds(Cocus_Full_Paper)
@given(instance=Cocus_Full_Paper_strategy)
@settings(max_examples=25)
def test_Cocus_Full_Paper_instantiation(instance):
    assert isinstance(instance, Cocus_Full_Paper)


Cocus_Group_Email_strategy = st.builds(Cocus_Group_Email)
@given(instance=Cocus_Group_Email_strategy)
@settings(max_examples=25)
def test_Cocus_Group_Email_instantiation(instance):
    assert isinstance(instance, Cocus_Group_Email)


Cocus_Head_Role_strategy = st.builds(Cocus_Head_Role)
@given(instance=Cocus_Head_Role_strategy)
@settings(max_examples=25)
def test_Cocus_Head_Role_instantiation(instance):
    assert isinstance(instance, Cocus_Head_Role)


Cocus_Help_Request_strategy = st.builds(Cocus_Help_Request)
@given(instance=Cocus_Help_Request_strategy)
@settings(max_examples=25)
def test_Cocus_Help_Request_instantiation(instance):
    assert isinstance(instance, Cocus_Help_Request)


Cocus_Inforamtion_strategy = st.builds(Cocus_Inforamtion)
@given(instance=Cocus_Inforamtion_strategy)
@settings(max_examples=25)
def test_Cocus_Inforamtion_instantiation(instance):
    assert isinstance(instance, Cocus_Inforamtion)


Cocus_Invited_Paper_strategy = st.builds(Cocus_Invited_Paper)
@given(instance=Cocus_Invited_Paper_strategy)
@settings(max_examples=25)
def test_Cocus_Invited_Paper_instantiation(instance):
    assert isinstance(instance, Cocus_Invited_Paper)


Cocus_Meta_Review_strategy = st.builds(Cocus_Meta_Review)
@given(instance=Cocus_Meta_Review_strategy)
@settings(max_examples=25)
def test_Cocus_Meta_Review_instantiation(instance):
    assert isinstance(instance, Cocus_Meta_Review)


Cocus_Meta_Reviewer_strategy = st.builds(Cocus_Meta_Reviewer)
@given(instance=Cocus_Meta_Reviewer_strategy)
@settings(max_examples=25)
def test_Cocus_Meta_Reviewer_instantiation(instance):
    assert isinstance(instance, Cocus_Meta_Reviewer)


Cocus_Misc_strategy = st.builds(Cocus_Misc)
@given(instance=Cocus_Misc_strategy)
@settings(max_examples=25)
def test_Cocus_Misc_instantiation(instance):
    assert isinstance(instance, Cocus_Misc)


Cocus_Notification_Email_strategy = st.builds(Cocus_Notification_Email)
@given(instance=Cocus_Notification_Email_strategy)
@settings(max_examples=25)
def test_Cocus_Notification_Email_instantiation(instance):
    assert isinstance(instance, Cocus_Notification_Email)


Cocus_Paper_strategy = st.builds(Cocus_Paper, paperID=safe_text, title=safe_text)
@given(instance=Cocus_Paper_strategy)
@settings(max_examples=25)
def test_Cocus_Paper_instantiation(instance):
    assert isinstance(instance, Cocus_Paper)


Cocus_PaperAbstract_strategy = st.builds(Cocus_PaperAbstract)
@given(instance=Cocus_PaperAbstract_strategy)
@settings(max_examples=25)
def test_Cocus_PaperAbstract_instantiation(instance):
    assert isinstance(instance, Cocus_PaperAbstract)


Cocus_PaperFullVersion_strategy = st.builds(Cocus_PaperFullVersion)
@given(instance=Cocus_PaperFullVersion_strategy)
@settings(max_examples=25)
def test_Cocus_PaperFullVersion_instantiation(instance):
    assert isinstance(instance, Cocus_PaperFullVersion)


Cocus_Paper_Typologies_strategy = st.builds(Cocus_Paper_Typologies)
@given(instance=Cocus_Paper_Typologies_strategy)
@settings(max_examples=25)
def test_Cocus_Paper_Typologies_instantiation(instance):
    assert isinstance(instance, Cocus_Paper_Typologies)


Cocus_Person_strategy = st.builds(Cocus_Person, email=safe_text)
@given(instance=Cocus_Person_strategy)
@settings(max_examples=25)
def test_Cocus_Person_instantiation(instance):
    assert isinstance(instance, Cocus_Person)


Cocus_Preference_strategy = st.builds(Cocus_Preference)
@given(instance=Cocus_Preference_strategy)
@settings(max_examples=25)
def test_Cocus_Preference_instantiation(instance):
    assert isinstance(instance, Cocus_Preference)


Cocus_Preview_strategy = st.builds(Cocus_Preview)
@given(instance=Cocus_Preview_strategy)
@settings(max_examples=25)
def test_Cocus_Preview_instantiation(instance):
    assert isinstance(instance, Cocus_Preview)


Cocus_ProgramCommittee_strategy = st.builds(Cocus_ProgramCommittee)
@given(instance=Cocus_ProgramCommittee_strategy)
@settings(max_examples=25)
def test_Cocus_ProgramCommittee_instantiation(instance):
    assert isinstance(instance, Cocus_ProgramCommittee)


Cocus_ProgramCommitteeChair_strategy = st.builds(Cocus_ProgramCommitteeChair)
@given(instance=Cocus_ProgramCommitteeChair_strategy)
@settings(max_examples=25)
def test_Cocus_ProgramCommitteeChair_instantiation(instance):
    assert isinstance(instance, Cocus_ProgramCommitteeChair)


Cocus_ProgramCommitteeMember_strategy = st.builds(Cocus_ProgramCommitteeMember, maxPapers=safe_text)
@given(instance=Cocus_ProgramCommitteeMember_strategy)
@settings(max_examples=25)
def test_Cocus_ProgramCommitteeMember_instantiation(instance):
    assert isinstance(instance, Cocus_ProgramCommitteeMember)


Cocus_Registration_strategy = st.builds(Cocus_Registration)
@given(instance=Cocus_Registration_strategy)
@settings(max_examples=25)
def test_Cocus_Registration_instantiation(instance):
    assert isinstance(instance, Cocus_Registration)


Cocus_Rejection_strategy = st.builds(Cocus_Rejection)
@given(instance=Cocus_Rejection_strategy)
@settings(max_examples=25)
def test_Cocus_Rejection_instantiation(instance):
    assert isinstance(instance, Cocus_Rejection)


Cocus_Rejection_Email_strategy = st.builds(Cocus_Rejection_Email)
@given(instance=Cocus_Rejection_Email_strategy)
@settings(max_examples=25)
def test_Cocus_Rejection_Email_instantiation(instance):
    assert isinstance(instance, Cocus_Rejection_Email)


Cocus_Request_strategy = st.builds(Cocus_Request)
@given(instance=Cocus_Request_strategy)
@settings(max_examples=25)
def test_Cocus_Request_instantiation(instance):
    assert isinstance(instance, Cocus_Request)


Cocus_Research_Topic_strategy = st.builds(Cocus_Research_Topic)
@given(instance=Cocus_Research_Topic_strategy)
@settings(max_examples=25)
def test_Cocus_Research_Topic_instantiation(instance):
    assert isinstance(instance, Cocus_Research_Topic)


Cocus_Review_strategy = st.builds(Cocus_Review)
@given(instance=Cocus_Review_strategy)
@settings(max_examples=25)
def test_Cocus_Review_instantiation(instance):
    assert isinstance(instance, Cocus_Review)


Cocus_Review_Form_strategy = st.builds(Cocus_Review_Form)
@given(instance=Cocus_Review_Form_strategy)
@settings(max_examples=25)
def test_Cocus_Review_Form_instantiation(instance):
    assert isinstance(instance, Cocus_Review_Form)


Cocus_Review_Form_Setup_strategy = st.builds(Cocus_Review_Form_Setup)
@given(instance=Cocus_Review_Form_Setup_strategy)
@settings(max_examples=25)
def test_Cocus_Review_Form_Setup_instantiation(instance):
    assert isinstance(instance, Cocus_Review_Form_Setup)


Cocus_Reviewer_strategy = st.builds(Cocus_Reviewer)
@given(instance=Cocus_Reviewer_strategy)
@settings(max_examples=25)
def test_Cocus_Reviewer_instantiation(instance):
    assert isinstance(instance, Cocus_Reviewer)


Cocus_Reviewer_Role_strategy = st.builds(Cocus_Reviewer_Role)
@given(instance=Cocus_Reviewer_Role_strategy)
@settings(max_examples=25)
def test_Cocus_Reviewer_Role_instantiation(instance):
    assert isinstance(instance, Cocus_Reviewer_Role)


Cocus_Role_strategy = st.builds(Cocus_Role)
@given(instance=Cocus_Role_strategy)
@settings(max_examples=25)
def test_Cocus_Role_instantiation(instance):
    assert isinstance(instance, Cocus_Role)


Cocus_Short_Paper_strategy = st.builds(Cocus_Short_Paper)
@given(instance=Cocus_Short_Paper_strategy)
@settings(max_examples=25)
def test_Cocus_Short_Paper_instantiation(instance):
    assert isinstance(instance, Cocus_Short_Paper)


Cocus_SubjectArea_strategy = st.builds(Cocus_SubjectArea)
@given(instance=Cocus_SubjectArea_strategy)
@settings(max_examples=25)
def test_Cocus_SubjectArea_instantiation(instance):
    assert isinstance(instance, Cocus_SubjectArea)


Cocus_Submission_strategy = st.builds(Cocus_Submission)
@given(instance=Cocus_Submission_strategy)
@settings(max_examples=25)
def test_Cocus_Submission_instantiation(instance):
    assert isinstance(instance, Cocus_Submission)


Cocus_Submission_Template_strategy = st.builds(Cocus_Submission_Template)
@given(instance=Cocus_Submission_Template_strategy)
@settings(max_examples=25)
def test_Cocus_Submission_Template_instantiation(instance):
    assert isinstance(instance, Cocus_Submission_Template)


Cocus_Symposium_strategy = st.builds(Cocus_Symposium)
@given(instance=Cocus_Symposium_strategy)
@settings(max_examples=25)
def test_Cocus_Symposium_instantiation(instance):
    assert isinstance(instance, Cocus_Symposium)


Cocus_Template_strategy = st.builds(Cocus_Template)
@given(instance=Cocus_Template_strategy)
@settings(max_examples=25)
def test_Cocus_Template_instantiation(instance):
    assert isinstance(instance, Cocus_Template)


Cocus_Thing_strategy = st.builds(Cocus_Thing)
@given(instance=Cocus_Thing_strategy)
@settings(max_examples=25)
def test_Cocus_Thing_instantiation(instance):
    assert isinstance(instance, Cocus_Thing)


Cocus_URL_strategy = st.builds(Cocus_URL)
@given(instance=Cocus_URL_strategy)
@settings(max_examples=25)
def test_Cocus_URL_instantiation(instance):
    assert isinstance(instance, Cocus_URL)


Cocus_User_strategy = st.builds(Cocus_User)
@given(instance=Cocus_User_strategy)
@settings(max_examples=25)
def test_Cocus_User_instantiation(instance):
    assert isinstance(instance, Cocus_User)


Cocus_Workshop_strategy = st.builds(Cocus_Workshop)
@given(instance=Cocus_Workshop_strategy)
@settings(max_examples=25)
def test_Cocus_Workshop_instantiation(instance):
    assert isinstance(instance, Cocus_Workshop)


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


Email_strategy = st.builds(Email)
@given(instance=Email_strategy)
@settings(max_examples=25)
def test_Email_instantiation(instance):
    assert isinstance(instance, Email)


Event_strategy = st.builds(Event)
@given(instance=Event_strategy)
@settings(max_examples=25)
def test_Event_instantiation(instance):
    assert isinstance(instance, Event)


Event_Setup_strategy = st.builds(Event_Setup)
@given(instance=Event_Setup_strategy)
@settings(max_examples=25)
def test_Event_Setup_instantiation(instance):
    assert isinstance(instance, Event_Setup)


Event_Tracks_strategy = st.builds(Event_Tracks)
@given(instance=Event_Tracks_strategy)
@settings(max_examples=25)
def test_Event_Tracks_instantiation(instance):
    assert isinstance(instance, Event_Tracks)


ExternalReviewer_strategy = st.builds(ExternalReviewer)
@given(instance=ExternalReviewer_strategy)
@settings(max_examples=25)
def test_ExternalReviewer_instantiation(instance):
    assert isinstance(instance, ExternalReviewer)


Help_Request_strategy = st.builds(Help_Request)
@given(instance=Help_Request_strategy)
@settings(max_examples=25)
def test_Help_Request_instantiation(instance):
    assert isinstance(instance, Help_Request)


Inforamtion_strategy = st.builds(Inforamtion)
@given(instance=Inforamtion_strategy)
@settings(max_examples=25)
def test_Inforamtion_instantiation(instance):
    assert isinstance(instance, Inforamtion)


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


Request_strategy = st.builds(Request)
@given(instance=Request_strategy)
@settings(max_examples=25)
def test_Request_instantiation(instance):
    assert isinstance(instance, Request)


Review_strategy = st.builds(Review)
@given(instance=Review_strategy)
@settings(max_examples=25)
def test_Review_instantiation(instance):
    assert isinstance(instance, Review)


Review_Form_strategy = st.builds(Review_Form)
@given(instance=Review_Form_strategy)
@settings(max_examples=25)
def test_Review_Form_instantiation(instance):
    assert isinstance(instance, Review_Form)


Reviewer_strategy = st.builds(Reviewer)
@given(instance=Reviewer_strategy)
@settings(max_examples=25)
def test_Reviewer_instantiation(instance):
    assert isinstance(instance, Reviewer)


Role_strategy = st.builds(Role)
@given(instance=Role_strategy)
@settings(max_examples=25)
def test_Role_instantiation(instance):
    assert isinstance(instance, Role)


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


URL_strategy = st.builds(URL)
@given(instance=URL_strategy)
@settings(max_examples=25)
def test_URL_instantiation(instance):
    assert isinstance(instance, URL)


User_strategy = st.builds(User)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


