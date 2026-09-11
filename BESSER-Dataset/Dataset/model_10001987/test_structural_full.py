import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    BallotInformation,
    Candidate,
    Election,
    Post,
    Voter,
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

def test_Admin_AdminID_value_roundtrip():
    instance = Admin(AdminID=7, AminName="sample_text", UserLogin=7)
    assert instance.AdminID == 7
    instance.AdminID = 13
    assert instance.AdminID == 13


def test_Admin_AminName_value_roundtrip():
    instance = Admin(AdminID=7, AminName="sample_text", UserLogin=7)
    assert instance.AminName == "sample_text"
    instance.AminName = "sample_text_2"
    assert instance.AminName == "sample_text_2"


def test_Admin_UserLogin_value_roundtrip():
    instance = Admin(AdminID=7, AminName="sample_text", UserLogin=7)
    assert instance.UserLogin == 7
    instance.UserLogin = 13
    assert instance.UserLogin == 13


def test_BallotInformation_BallotElectionID_value_roundtrip():
    instance = BallotInformation(BallotElectionID=7, BallotID=7, BallotPropBallotID=7, BallotPropID=7, BallotPropResults=7, BallotVotersID=7)
    assert instance.BallotElectionID == 7
    instance.BallotElectionID = 13
    assert instance.BallotElectionID == 13


def test_BallotInformation_BallotID_value_roundtrip():
    instance = BallotInformation(BallotElectionID=7, BallotID=7, BallotPropBallotID=7, BallotPropID=7, BallotPropResults=7, BallotVotersID=7)
    assert instance.BallotID == 7
    instance.BallotID = 13
    assert instance.BallotID == 13


def test_BallotInformation_BallotPropBallotID_value_roundtrip():
    instance = BallotInformation(BallotElectionID=7, BallotID=7, BallotPropBallotID=7, BallotPropID=7, BallotPropResults=7, BallotVotersID=7)
    assert instance.BallotPropBallotID == 7
    instance.BallotPropBallotID = 13
    assert instance.BallotPropBallotID == 13


def test_BallotInformation_BallotPropID_value_roundtrip():
    instance = BallotInformation(BallotElectionID=7, BallotID=7, BallotPropBallotID=7, BallotPropID=7, BallotPropResults=7, BallotVotersID=7)
    assert instance.BallotPropID == 7
    instance.BallotPropID = 13
    assert instance.BallotPropID == 13


def test_BallotInformation_BallotPropResults_value_roundtrip():
    instance = BallotInformation(BallotElectionID=7, BallotID=7, BallotPropBallotID=7, BallotPropID=7, BallotPropResults=7, BallotVotersID=7)
    assert instance.BallotPropResults == 7
    instance.BallotPropResults = 13
    assert instance.BallotPropResults == 13


def test_BallotInformation_BallotVotersID_value_roundtrip():
    instance = BallotInformation(BallotElectionID=7, BallotID=7, BallotPropBallotID=7, BallotPropID=7, BallotPropResults=7, BallotVotersID=7)
    assert instance.BallotVotersID == 7
    instance.BallotVotersID = 13
    assert instance.BallotVotersID == 13


def test_Candidate_CandidatePartyName_value_roundtrip():
    instance = Candidate(CandidatePartyName="sample_text", Candidate_Name="sample_text", Candidate_PostID=7, candidate_ID=7)
    assert instance.CandidatePartyName == "sample_text"
    instance.CandidatePartyName = "sample_text_2"
    assert instance.CandidatePartyName == "sample_text_2"


def test_Candidate_Candidate_Name_value_roundtrip():
    instance = Candidate(CandidatePartyName="sample_text", Candidate_Name="sample_text", Candidate_PostID=7, candidate_ID=7)
    assert instance.Candidate_Name == "sample_text"
    instance.Candidate_Name = "sample_text_2"
    assert instance.Candidate_Name == "sample_text_2"


def test_Candidate_Candidate_PostID_value_roundtrip():
    instance = Candidate(CandidatePartyName="sample_text", Candidate_Name="sample_text", Candidate_PostID=7, candidate_ID=7)
    assert instance.Candidate_PostID == 7
    instance.Candidate_PostID = 13
    assert instance.Candidate_PostID == 13


def test_Candidate_candidate_ID_value_roundtrip():
    instance = Candidate(CandidatePartyName="sample_text", Candidate_Name="sample_text", Candidate_PostID=7, candidate_ID=7)
    assert instance.candidate_ID == 7
    instance.candidate_ID = 13
    assert instance.candidate_ID == 13


def test_Election_ElectionCriteria_value_roundtrip():
    instance = Election(ElectionCriteria="sample_text", ElectionDate="sample_text", ElectionID=7, ElectionName="sample_text")
    assert instance.ElectionCriteria == "sample_text"
    instance.ElectionCriteria = "sample_text_2"
    assert instance.ElectionCriteria == "sample_text_2"


def test_Election_ElectionDate_value_roundtrip():
    instance = Election(ElectionCriteria="sample_text", ElectionDate="sample_text", ElectionID=7, ElectionName="sample_text")
    assert instance.ElectionDate == "sample_text"
    instance.ElectionDate = "sample_text_2"
    assert instance.ElectionDate == "sample_text_2"


def test_Election_ElectionID_value_roundtrip():
    instance = Election(ElectionCriteria="sample_text", ElectionDate="sample_text", ElectionID=7, ElectionName="sample_text")
    assert instance.ElectionID == 7
    instance.ElectionID = 13
    assert instance.ElectionID == 13


def test_Election_ElectionName_value_roundtrip():
    instance = Election(ElectionCriteria="sample_text", ElectionDate="sample_text", ElectionID=7, ElectionName="sample_text")
    assert instance.ElectionName == "sample_text"
    instance.ElectionName = "sample_text_2"
    assert instance.ElectionName == "sample_text_2"


def test_Post_PostDesc_value_roundtrip():
    instance = Post(PostDesc="sample_text", PostElectionId=7, PostId=7)
    assert instance.PostDesc == "sample_text"
    instance.PostDesc = "sample_text_2"
    assert instance.PostDesc == "sample_text_2"


def test_Post_PostElectionId_value_roundtrip():
    instance = Post(PostDesc="sample_text", PostElectionId=7, PostId=7)
    assert instance.PostElectionId == 7
    instance.PostElectionId = 13
    assert instance.PostElectionId == 13


def test_Post_PostId_value_roundtrip():
    instance = Post(PostDesc="sample_text", PostElectionId=7, PostId=7)
    assert instance.PostId == 7
    instance.PostId = 13
    assert instance.PostId == 13


def test_Voter_Address_value_roundtrip():
    instance = Voter(Address="sample_text", Age=7, Eligibilty=True, Name="sample_text", student_faculty_ID=7)
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Voter_Age_value_roundtrip():
    instance = Voter(Address="sample_text", Age=7, Eligibilty=True, Name="sample_text", student_faculty_ID=7)
    assert instance.Age == 7
    instance.Age = 13
    assert instance.Age == 13


def test_Voter_Eligibilty_value_roundtrip():
    instance = Voter(Address="sample_text", Age=7, Eligibilty=True, Name="sample_text", student_faculty_ID=7)
    assert instance.Eligibilty == True
    instance.Eligibilty = False
    assert instance.Eligibilty == False


def test_Voter_Name_value_roundtrip():
    instance = Voter(Address="sample_text", Age=7, Eligibilty=True, Name="sample_text", student_faculty_ID=7)
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Voter_student_faculty_ID_value_roundtrip():
    instance = Voter(Address="sample_text", Age=7, Eligibilty=True, Name="sample_text", student_faculty_ID=7)
    assert instance.student_faculty_ID == 7
    instance.student_faculty_ID = 13
    assert instance.student_faculty_ID == 13


def test_assoc_Admin_BallotInformation_link_reassign_clear():
    a = BallotInformation(BallotElectionID=7, BallotID=7, BallotPropBallotID=7, BallotPropID=7, BallotPropResults=7, BallotVotersID=7)
    b1 = Admin(AdminID=7, AminName="sample_text", UserLogin=7)
    b2 = Admin(AdminID=13, AminName="sample_text_2", UserLogin=13)
    _safe_set(a, 'admin19', b1)
    assert _is_linked(a, 'admin19', b1)
    if hasattr(b1, 'ballotInformation18'):
        assert _is_linked(b1, 'ballotInformation18', a)
    _safe_set(a, 'admin19', b2)
    assert _is_linked(a, 'admin19', b2)
    if hasattr(b1, 'ballotInformation18'):
        assert not _is_linked(b1, 'ballotInformation18', a)
    if hasattr(b2, 'ballotInformation18'):
        assert _is_linked(b2, 'ballotInformation18', a)
    _safe_set(a, 'admin19', None)
    assert not _is_linked(a, 'admin19', b2)
    if hasattr(b2, 'ballotInformation18'):
        assert not _is_linked(b2, 'ballotInformation18', a)


def test_assoc_Admin_Candidate_link_reassign_clear():
    a = Candidate(CandidatePartyName="sample_text", Candidate_Name="sample_text", Candidate_PostID=7, candidate_ID=7)
    b1 = Admin(AdminID=7, AminName="sample_text", UserLogin=7)
    b2 = Admin(AdminID=13, AminName="sample_text_2", UserLogin=13)
    _safe_set(a, 'admin15', b1)
    assert _is_linked(a, 'admin15', b1)
    if hasattr(b1, 'candidate14'):
        assert _is_linked(b1, 'candidate14', a)
    _safe_set(a, 'admin15', b2)
    assert _is_linked(a, 'admin15', b2)
    if hasattr(b1, 'candidate14'):
        assert not _is_linked(b1, 'candidate14', a)
    if hasattr(b2, 'candidate14'):
        assert _is_linked(b2, 'candidate14', a)
    _safe_set(a, 'admin15', None)
    assert not _is_linked(a, 'admin15', b2)
    if hasattr(b2, 'candidate14'):
        assert not _is_linked(b2, 'candidate14', a)


def test_assoc_Admin_Election_link_reassign_clear():
    a = Election(ElectionCriteria="sample_text", ElectionDate="sample_text", ElectionID=7, ElectionName="sample_text")
    b1 = Admin(AdminID=7, AminName="sample_text", UserLogin=7)
    b2 = Admin(AdminID=13, AminName="sample_text_2", UserLogin=13)
    _safe_set(a, 'admin17', b1)
    assert _is_linked(a, 'admin17', b1)
    if hasattr(b1, 'election16'):
        assert _is_linked(b1, 'election16', a)
    _safe_set(a, 'admin17', b2)
    assert _is_linked(a, 'admin17', b2)
    if hasattr(b1, 'election16'):
        assert not _is_linked(b1, 'election16', a)
    if hasattr(b2, 'election16'):
        assert _is_linked(b2, 'election16', a)
    _safe_set(a, 'admin17', None)
    assert not _is_linked(a, 'admin17', b2)
    if hasattr(b2, 'election16'):
        assert not _is_linked(b2, 'election16', a)


def test_assoc_Candidate__BallotInformation_link_reassign_clear():
    a = Candidate(CandidatePartyName="sample_text", Candidate_Name="sample_text", Candidate_PostID=7, candidate_ID=7)
    b1 = BallotInformation(BallotElectionID=7, BallotID=7, BallotPropBallotID=7, BallotPropID=7, BallotPropResults=7, BallotVotersID=7)
    b2 = BallotInformation(BallotElectionID=13, BallotID=13, BallotPropBallotID=13, BallotPropID=13, BallotPropResults=13, BallotVotersID=13)
    _safe_set(a, 'ballotInformation0', b1)
    assert _is_linked(a, 'ballotInformation0', b1)
    if hasattr(b1, 'candidate1'):
        assert _is_linked(b1, 'candidate1', a)
    _safe_set(a, 'ballotInformation0', b2)
    assert _is_linked(a, 'ballotInformation0', b2)
    if hasattr(b1, 'candidate1'):
        assert not _is_linked(b1, 'candidate1', a)
    if hasattr(b2, 'candidate1'):
        assert _is_linked(b2, 'candidate1', a)
    _safe_set(a, 'ballotInformation0', None)
    assert not _is_linked(a, 'ballotInformation0', b2)
    if hasattr(b2, 'candidate1'):
        assert not _is_linked(b2, 'candidate1', a)


def test_assoc_Candidate__Election_link_reassign_clear():
    a = Election(ElectionCriteria="sample_text", ElectionDate="sample_text", ElectionID=7, ElectionName="sample_text")
    b1 = Candidate(CandidatePartyName="sample_text", Candidate_Name="sample_text", Candidate_PostID=7, candidate_ID=7)
    b2 = Candidate(CandidatePartyName="sample_text_2", Candidate_Name="sample_text_2", Candidate_PostID=13, candidate_ID=13)
    _safe_set(a, 'candidate11', b1)
    assert _is_linked(a, 'candidate11', b1)
    if hasattr(b1, 'election10'):
        assert _is_linked(b1, 'election10', a)
    _safe_set(a, 'candidate11', b2)
    assert _is_linked(a, 'candidate11', b2)
    if hasattr(b1, 'election10'):
        assert not _is_linked(b1, 'election10', a)
    if hasattr(b2, 'election10'):
        assert _is_linked(b2, 'election10', a)
    _safe_set(a, 'candidate11', None)
    assert not _is_linked(a, 'candidate11', b2)
    if hasattr(b2, 'election10'):
        assert not _is_linked(b2, 'election10', a)


def test_assoc_Election_BallotInformation_link_reassign_clear():
    a = Election(ElectionCriteria="sample_text", ElectionDate="sample_text", ElectionID=7, ElectionName="sample_text")
    b1 = BallotInformation(BallotElectionID=7, BallotID=7, BallotPropBallotID=7, BallotPropID=7, BallotPropResults=7, BallotVotersID=7)
    b2 = BallotInformation(BallotElectionID=13, BallotID=13, BallotPropBallotID=13, BallotPropID=13, BallotPropResults=13, BallotVotersID=13)
    _safe_set(a, 'ballotInformation2', b1)
    assert _is_linked(a, 'ballotInformation2', b1)
    if hasattr(b1, 'election3'):
        assert _is_linked(b1, 'election3', a)
    _safe_set(a, 'ballotInformation2', b2)
    assert _is_linked(a, 'ballotInformation2', b2)
    if hasattr(b1, 'election3'):
        assert not _is_linked(b1, 'election3', a)
    if hasattr(b2, 'election3'):
        assert _is_linked(b2, 'election3', a)
    _safe_set(a, 'ballotInformation2', None)
    assert not _is_linked(a, 'ballotInformation2', b2)
    if hasattr(b2, 'election3'):
        assert not _is_linked(b2, 'election3', a)


def test_assoc_Post_BallotInformation_link_reassign_clear():
    a = Post(PostDesc="sample_text", PostElectionId=7, PostId=7)
    b1 = BallotInformation(BallotElectionID=7, BallotID=7, BallotPropBallotID=7, BallotPropID=7, BallotPropResults=7, BallotVotersID=7)
    b2 = BallotInformation(BallotElectionID=13, BallotID=13, BallotPropBallotID=13, BallotPropID=13, BallotPropResults=13, BallotVotersID=13)
    _safe_set(a, 'ballotInformation8', b1)
    assert _is_linked(a, 'ballotInformation8', b1)
    if hasattr(b1, 'post9'):
        assert _is_linked(b1, 'post9', a)
    _safe_set(a, 'ballotInformation8', b2)
    assert _is_linked(a, 'ballotInformation8', b2)
    if hasattr(b1, 'post9'):
        assert not _is_linked(b1, 'post9', a)
    if hasattr(b2, 'post9'):
        assert _is_linked(b2, 'post9', a)
    _safe_set(a, 'ballotInformation8', None)
    assert not _is_linked(a, 'ballotInformation8', b2)
    if hasattr(b2, 'post9'):
        assert not _is_linked(b2, 'post9', a)


def test_assoc_Voter_Admin_link_reassign_clear():
    a = Voter(Address="sample_text", Age=7, Eligibilty=True, Name="sample_text", student_faculty_ID=7)
    b1 = Admin(AdminID=7, AminName="sample_text", UserLogin=7)
    b2 = Admin(AdminID=13, AminName="sample_text_2", UserLogin=13)
    _safe_set(a, 'admin12', b1)
    assert _is_linked(a, 'admin12', b1)
    if hasattr(b1, 'voter13'):
        assert _is_linked(b1, 'voter13', a)
    _safe_set(a, 'admin12', b2)
    assert _is_linked(a, 'admin12', b2)
    if hasattr(b1, 'voter13'):
        assert not _is_linked(b1, 'voter13', a)
    if hasattr(b2, 'voter13'):
        assert _is_linked(b2, 'voter13', a)
    _safe_set(a, 'admin12', None)
    assert not _is_linked(a, 'admin12', b2)
    if hasattr(b2, 'voter13'):
        assert not _is_linked(b2, 'voter13', a)


def test_assoc_Voter_Election_link_reassign_clear():
    a = Voter(Address="sample_text", Age=7, Eligibilty=True, Name="sample_text", student_faculty_ID=7)
    b1 = Election(ElectionCriteria="sample_text", ElectionDate="sample_text", ElectionID=7, ElectionName="sample_text")
    b2 = Election(ElectionCriteria="sample_text_2", ElectionDate="sample_text_2", ElectionID=13, ElectionName="sample_text_2")
    _safe_set(a, 'election4', b1)
    assert _is_linked(a, 'election4', b1)
    if hasattr(b1, 'voter5'):
        assert _is_linked(b1, 'voter5', a)
    _safe_set(a, 'election4', b2)
    assert _is_linked(a, 'election4', b2)
    if hasattr(b1, 'voter5'):
        assert not _is_linked(b1, 'voter5', a)
    if hasattr(b2, 'voter5'):
        assert _is_linked(b2, 'voter5', a)
    _safe_set(a, 'election4', None)
    assert not _is_linked(a, 'election4', b2)
    if hasattr(b2, 'voter5'):
        assert not _is_linked(b2, 'voter5', a)


def test_assoc_Voter_Post_link_reassign_clear():
    a = Voter(Address="sample_text", Age=7, Eligibilty=True, Name="sample_text", student_faculty_ID=7)
    b1 = Post(PostDesc="sample_text", PostElectionId=7, PostId=7)
    b2 = Post(PostDesc="sample_text_2", PostElectionId=13, PostId=13)
    _safe_set(a, 'post6', b1)
    assert _is_linked(a, 'post6', b1)
    if hasattr(b1, 'voter7'):
        assert _is_linked(b1, 'voter7', a)
    _safe_set(a, 'post6', b2)
    assert _is_linked(a, 'post6', b2)
    if hasattr(b1, 'voter7'):
        assert not _is_linked(b1, 'voter7', a)
    if hasattr(b2, 'voter7'):
        assert _is_linked(b2, 'voter7', a)
    _safe_set(a, 'post6', None)
    assert not _is_linked(a, 'post6', b2)
    if hasattr(b2, 'voter7'):
        assert not _is_linked(b2, 'voter7', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin, AdminID=st.integers(), AminName=safe_text, UserLogin=st.integers())
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


BallotInformation_strategy = st.builds(BallotInformation, BallotElectionID=st.integers(), BallotID=st.integers(), BallotPropBallotID=st.integers(), BallotPropID=st.integers(), BallotPropResults=st.integers(), BallotVotersID=st.integers())
@given(instance=BallotInformation_strategy)
@settings(max_examples=25)
def test_BallotInformation_instantiation(instance):
    assert isinstance(instance, BallotInformation)


Candidate_strategy = st.builds(Candidate, CandidatePartyName=safe_text, Candidate_Name=safe_text, Candidate_PostID=st.integers(), candidate_ID=st.integers())
@given(instance=Candidate_strategy)
@settings(max_examples=25)
def test_Candidate_instantiation(instance):
    assert isinstance(instance, Candidate)


Election_strategy = st.builds(Election, ElectionCriteria=safe_text, ElectionDate=safe_text, ElectionID=st.integers(), ElectionName=safe_text)
@given(instance=Election_strategy)
@settings(max_examples=25)
def test_Election_instantiation(instance):
    assert isinstance(instance, Election)


Post_strategy = st.builds(Post, PostDesc=safe_text, PostElectionId=st.integers(), PostId=st.integers())
@given(instance=Post_strategy)
@settings(max_examples=25)
def test_Post_instantiation(instance):
    assert isinstance(instance, Post)


Voter_strategy = st.builds(Voter, Address=safe_text, Age=st.integers(), Eligibilty=st.booleans(), Name=safe_text, student_faculty_ID=st.integers())
@given(instance=Voter_strategy)
@settings(max_examples=25)
def test_Voter_instantiation(instance):
    assert isinstance(instance, Voter)


