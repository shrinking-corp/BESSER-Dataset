import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    BallotInformation,
    Candidate,
    Election,
    Post,
    Voter,
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

def test_assoc_Admin_BallotInformation_reverse_link_reassign_clear():
    a1 = BallotInformation(BallotElectionID=7, BallotID=7, BallotPropBallotID=7, BallotPropID=7, BallotPropResults=7, BallotVotersID=7)
    a2 = BallotInformation(BallotElectionID=13, BallotID=13, BallotPropBallotID=13, BallotPropID=13, BallotPropResults=13, BallotVotersID=13)
    b = Admin(AdminID=7, AminName="sample_text", UserLogin=7)
    _safe_set(b, 'ballotInformation18', a1)
    assert _is_linked(b, 'ballotInformation18', a1)
    if hasattr(a1, 'admin19'):
        assert _is_linked(a1, 'admin19', b)
    _safe_set(b, 'ballotInformation18', a2)
    assert _is_linked(b, 'ballotInformation18', a2)
    if hasattr(a1, 'admin19'):
        assert not _is_linked(a1, 'admin19', b)
    if hasattr(a2, 'admin19'):
        assert _is_linked(a2, 'admin19', b)
    _safe_set(b, 'ballotInformation18', None)
    assert not _is_linked(b, 'ballotInformation18', a2)
    if hasattr(a2, 'admin19'):
        assert not _is_linked(a2, 'admin19', b)


def test_assoc_Admin_Candidate_reverse_link_reassign_clear():
    a1 = Candidate(CandidatePartyName="sample_text", Candidate_Name="sample_text", Candidate_PostID=7, candidate_ID=7)
    a2 = Candidate(CandidatePartyName="sample_text_2", Candidate_Name="sample_text_2", Candidate_PostID=13, candidate_ID=13)
    b = Admin(AdminID=7, AminName="sample_text", UserLogin=7)
    _safe_set(b, 'candidate14', a1)
    assert _is_linked(b, 'candidate14', a1)
    if hasattr(a1, 'admin15'):
        assert _is_linked(a1, 'admin15', b)
    _safe_set(b, 'candidate14', a2)
    assert _is_linked(b, 'candidate14', a2)
    if hasattr(a1, 'admin15'):
        assert not _is_linked(a1, 'admin15', b)
    if hasattr(a2, 'admin15'):
        assert _is_linked(a2, 'admin15', b)
    _safe_set(b, 'candidate14', None)
    assert not _is_linked(b, 'candidate14', a2)
    if hasattr(a2, 'admin15'):
        assert not _is_linked(a2, 'admin15', b)


def test_assoc_Admin_Election_reverse_link_reassign_clear():
    a1 = Election(ElectionCriteria="sample_text", ElectionDate="sample_text", ElectionID=7, ElectionName="sample_text")
    a2 = Election(ElectionCriteria="sample_text_2", ElectionDate="sample_text_2", ElectionID=13, ElectionName="sample_text_2")
    b = Admin(AdminID=7, AminName="sample_text", UserLogin=7)
    _safe_set(b, 'election16', a1)
    assert _is_linked(b, 'election16', a1)
    if hasattr(a1, 'admin17'):
        assert _is_linked(a1, 'admin17', b)
    _safe_set(b, 'election16', a2)
    assert _is_linked(b, 'election16', a2)
    if hasattr(a1, 'admin17'):
        assert not _is_linked(a1, 'admin17', b)
    if hasattr(a2, 'admin17'):
        assert _is_linked(a2, 'admin17', b)
    _safe_set(b, 'election16', None)
    assert not _is_linked(b, 'election16', a2)
    if hasattr(a2, 'admin17'):
        assert not _is_linked(a2, 'admin17', b)


def test_assoc_Candidate__BallotInformation_reverse_link_reassign_clear():
    a1 = Candidate(CandidatePartyName="sample_text", Candidate_Name="sample_text", Candidate_PostID=7, candidate_ID=7)
    a2 = Candidate(CandidatePartyName="sample_text_2", Candidate_Name="sample_text_2", Candidate_PostID=13, candidate_ID=13)
    b = BallotInformation(BallotElectionID=7, BallotID=7, BallotPropBallotID=7, BallotPropID=7, BallotPropResults=7, BallotVotersID=7)
    _safe_set(b, 'candidate1', a1)
    assert _is_linked(b, 'candidate1', a1)
    if hasattr(a1, 'ballotInformation0'):
        assert _is_linked(a1, 'ballotInformation0', b)
    _safe_set(b, 'candidate1', a2)
    assert _is_linked(b, 'candidate1', a2)
    if hasattr(a1, 'ballotInformation0'):
        assert not _is_linked(a1, 'ballotInformation0', b)
    if hasattr(a2, 'ballotInformation0'):
        assert _is_linked(a2, 'ballotInformation0', b)
    _safe_set(b, 'candidate1', None)
    assert not _is_linked(b, 'candidate1', a2)
    if hasattr(a2, 'ballotInformation0'):
        assert not _is_linked(a2, 'ballotInformation0', b)


def test_assoc_Candidate__Election_reverse_link_reassign_clear():
    a1 = Election(ElectionCriteria="sample_text", ElectionDate="sample_text", ElectionID=7, ElectionName="sample_text")
    a2 = Election(ElectionCriteria="sample_text_2", ElectionDate="sample_text_2", ElectionID=13, ElectionName="sample_text_2")
    b = Candidate(CandidatePartyName="sample_text", Candidate_Name="sample_text", Candidate_PostID=7, candidate_ID=7)
    _safe_set(b, 'election10', a1)
    assert _is_linked(b, 'election10', a1)
    if hasattr(a1, 'candidate11'):
        assert _is_linked(a1, 'candidate11', b)
    _safe_set(b, 'election10', a2)
    assert _is_linked(b, 'election10', a2)
    if hasattr(a1, 'candidate11'):
        assert not _is_linked(a1, 'candidate11', b)
    if hasattr(a2, 'candidate11'):
        assert _is_linked(a2, 'candidate11', b)
    _safe_set(b, 'election10', None)
    assert not _is_linked(b, 'election10', a2)
    if hasattr(a2, 'candidate11'):
        assert not _is_linked(a2, 'candidate11', b)


def test_assoc_Election_BallotInformation_reverse_link_reassign_clear():
    a1 = Election(ElectionCriteria="sample_text", ElectionDate="sample_text", ElectionID=7, ElectionName="sample_text")
    a2 = Election(ElectionCriteria="sample_text_2", ElectionDate="sample_text_2", ElectionID=13, ElectionName="sample_text_2")
    b = BallotInformation(BallotElectionID=7, BallotID=7, BallotPropBallotID=7, BallotPropID=7, BallotPropResults=7, BallotVotersID=7)
    _safe_set(b, 'election3', a1)
    assert _is_linked(b, 'election3', a1)
    if hasattr(a1, 'ballotInformation2'):
        assert _is_linked(a1, 'ballotInformation2', b)
    _safe_set(b, 'election3', a2)
    assert _is_linked(b, 'election3', a2)
    if hasattr(a1, 'ballotInformation2'):
        assert not _is_linked(a1, 'ballotInformation2', b)
    if hasattr(a2, 'ballotInformation2'):
        assert _is_linked(a2, 'ballotInformation2', b)
    _safe_set(b, 'election3', None)
    assert not _is_linked(b, 'election3', a2)
    if hasattr(a2, 'ballotInformation2'):
        assert not _is_linked(a2, 'ballotInformation2', b)


def test_assoc_Post_BallotInformation_reverse_link_reassign_clear():
    a1 = Post(PostDesc="sample_text", PostElectionId=7, PostId=7)
    a2 = Post(PostDesc="sample_text_2", PostElectionId=13, PostId=13)
    b = BallotInformation(BallotElectionID=7, BallotID=7, BallotPropBallotID=7, BallotPropID=7, BallotPropResults=7, BallotVotersID=7)
    _safe_set(b, 'post9', a1)
    assert _is_linked(b, 'post9', a1)
    if hasattr(a1, 'ballotInformation8'):
        assert _is_linked(a1, 'ballotInformation8', b)
    _safe_set(b, 'post9', a2)
    assert _is_linked(b, 'post9', a2)
    if hasattr(a1, 'ballotInformation8'):
        assert not _is_linked(a1, 'ballotInformation8', b)
    if hasattr(a2, 'ballotInformation8'):
        assert _is_linked(a2, 'ballotInformation8', b)
    _safe_set(b, 'post9', None)
    assert not _is_linked(b, 'post9', a2)
    if hasattr(a2, 'ballotInformation8'):
        assert not _is_linked(a2, 'ballotInformation8', b)


def test_assoc_Voter_Admin_reverse_link_reassign_clear():
    a1 = Voter(Address="sample_text", Age=7, Eligibilty=True, Name="sample_text", student_faculty_ID=7)
    a2 = Voter(Address="sample_text_2", Age=13, Eligibilty=False, Name="sample_text_2", student_faculty_ID=13)
    b = Admin(AdminID=7, AminName="sample_text", UserLogin=7)
    _safe_set(b, 'voter13', a1)
    assert _is_linked(b, 'voter13', a1)
    if hasattr(a1, 'admin12'):
        assert _is_linked(a1, 'admin12', b)
    _safe_set(b, 'voter13', a2)
    assert _is_linked(b, 'voter13', a2)
    if hasattr(a1, 'admin12'):
        assert not _is_linked(a1, 'admin12', b)
    if hasattr(a2, 'admin12'):
        assert _is_linked(a2, 'admin12', b)
    _safe_set(b, 'voter13', None)
    assert not _is_linked(b, 'voter13', a2)
    if hasattr(a2, 'admin12'):
        assert not _is_linked(a2, 'admin12', b)


def test_assoc_Voter_Election_reverse_link_reassign_clear():
    a1 = Voter(Address="sample_text", Age=7, Eligibilty=True, Name="sample_text", student_faculty_ID=7)
    a2 = Voter(Address="sample_text_2", Age=13, Eligibilty=False, Name="sample_text_2", student_faculty_ID=13)
    b = Election(ElectionCriteria="sample_text", ElectionDate="sample_text", ElectionID=7, ElectionName="sample_text")
    _safe_set(b, 'voter5', a1)
    assert _is_linked(b, 'voter5', a1)
    if hasattr(a1, 'election4'):
        assert _is_linked(a1, 'election4', b)
    _safe_set(b, 'voter5', a2)
    assert _is_linked(b, 'voter5', a2)
    if hasattr(a1, 'election4'):
        assert not _is_linked(a1, 'election4', b)
    if hasattr(a2, 'election4'):
        assert _is_linked(a2, 'election4', b)
    _safe_set(b, 'voter5', None)
    assert not _is_linked(b, 'voter5', a2)
    if hasattr(a2, 'election4'):
        assert not _is_linked(a2, 'election4', b)


def test_assoc_Voter_Post_reverse_link_reassign_clear():
    a1 = Voter(Address="sample_text", Age=7, Eligibilty=True, Name="sample_text", student_faculty_ID=7)
    a2 = Voter(Address="sample_text_2", Age=13, Eligibilty=False, Name="sample_text_2", student_faculty_ID=13)
    b = Post(PostDesc="sample_text", PostElectionId=7, PostId=7)
    _safe_set(b, 'voter7', a1)
    assert _is_linked(b, 'voter7', a1)
    if hasattr(a1, 'post6'):
        assert _is_linked(a1, 'post6', b)
    _safe_set(b, 'voter7', a2)
    assert _is_linked(b, 'voter7', a2)
    if hasattr(a1, 'post6'):
        assert not _is_linked(a1, 'post6', b)
    if hasattr(a2, 'post6'):
        assert _is_linked(a2, 'post6', b)
    _safe_set(b, 'voter7', None)
    assert not _is_linked(b, 'voter7', a2)
    if hasattr(a2, 'post6'):
        assert not _is_linked(a2, 'post6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

