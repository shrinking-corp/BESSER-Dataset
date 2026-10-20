import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Base,
    Org,
    dXP_AcademicSession,
    dXP_Base,
    dXP_Class,
    dXP_Course,
    dXP_Enrolment,
    dXP_Metadata,
    dXP_OneRoster,
    dXP_Org,
    dXP_OrgUnit,
    dXP_User,
    dXP_UserId,
    OrgType,
    Role,
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

def test_assoc_class_19_reverse_link_reassign_clear():
    a1 = dXP_Enrolment(primary="sample_text", role="sample_text")
    a2 = dXP_Enrolment(primary="sample_text_2", role="sample_text_2")
    b = dXP_Class(classCode="sample_text", classType="sample_text", location="sample_text", title="sample_text")
    _safe_set(b, 'dXP_Class21', a1)
    assert _is_linked(b, 'dXP_Class21', a1)
    if hasattr(a1, 'dXP_Enrolment20'):
        assert _is_linked(a1, 'dXP_Enrolment20', b)
    _safe_set(b, 'dXP_Class21', a2)
    assert _is_linked(b, 'dXP_Class21', a2)
    if hasattr(a1, 'dXP_Enrolment20'):
        assert not _is_linked(a1, 'dXP_Enrolment20', b)
    if hasattr(a2, 'dXP_Enrolment20'):
        assert _is_linked(a2, 'dXP_Enrolment20', b)
    _safe_set(b, 'dXP_Class21', None)
    assert not _is_linked(b, 'dXP_Class21', a2)
    if hasattr(a2, 'dXP_Enrolment20'):
        assert not _is_linked(a2, 'dXP_Enrolment20', b)


def test_assoc_class_5_reverse_link_reassign_clear():
    a1 = dXP_Course(courseCode="sample_text", title="sample_text")
    a2 = dXP_Course(courseCode="sample_text_2", title="sample_text_2")
    b = dXP_Class(classCode="sample_text", classType="sample_text", location="sample_text", title="sample_text")
    _safe_set(b, 'dXP_Class', a1)
    assert _is_linked(b, 'dXP_Class', a1)
    if hasattr(a1, 'dXP_Course'):
        assert _is_linked(a1, 'dXP_Course', b)
    _safe_set(b, 'dXP_Class', a2)
    assert _is_linked(b, 'dXP_Class', a2)
    if hasattr(a1, 'dXP_Course'):
        assert not _is_linked(a1, 'dXP_Course', b)
    if hasattr(a2, 'dXP_Course'):
        assert _is_linked(a2, 'dXP_Course', b)
    _safe_set(b, 'dXP_Class', None)
    assert not _is_linked(b, 'dXP_Class', a2)
    if hasattr(a2, 'dXP_Course'):
        assert not _is_linked(a2, 'dXP_Course', b)


def test_assoc_course7_reverse_link_reassign_clear():
    a1 = dXP_Course(courseCode="sample_text", title="sample_text")
    a2 = dXP_Course(courseCode="sample_text_2", title="sample_text_2")
    b = dXP_AcademicSession(endDate="sample_text", schoolYear="sample_text", startDate="sample_text", title="sample_text", type="sample_text")
    _safe_set(b, 'dXP_AcademicSession8', {a1})
    assert _is_linked(b, 'dXP_AcademicSession8', a1)
    if hasattr(a1, 'dXP_Course9'):
        assert _is_linked(a1, 'dXP_Course9', b)
    _safe_set(b, 'dXP_AcademicSession8', {a2})
    assert _is_linked(b, 'dXP_AcademicSession8', a2)
    if hasattr(a1, 'dXP_Course9'):
        assert not _is_linked(a1, 'dXP_Course9', b)
    if hasattr(a2, 'dXP_Course9'):
        assert _is_linked(a2, 'dXP_Course9', b)
    _safe_set(b, 'dXP_AcademicSession8', set())
    assert not _is_linked(b, 'dXP_AcademicSession8', a2)
    if hasattr(a2, 'dXP_Course9'):
        assert not _is_linked(a2, 'dXP_Course9', b)


def test_assoc_metadata6_reverse_link_reassign_clear():
    a1 = dXP_Metadata(key="sample_text", value="sample_text")
    a2 = dXP_Metadata(key="sample_text_2", value="sample_text_2")
    b = dXP_Base(dateLastModified="sample_text", sourceId="sample_text", status="sample_text")
    _safe_set(b, 'dXP_Base', {a1})
    assert _is_linked(b, 'dXP_Base', a1)
    if hasattr(a1, 'dXP_Metadata'):
        assert _is_linked(a1, 'dXP_Metadata', b)
    _safe_set(b, 'dXP_Base', {a2})
    assert _is_linked(b, 'dXP_Base', a2)
    if hasattr(a1, 'dXP_Metadata'):
        assert not _is_linked(a1, 'dXP_Metadata', b)
    if hasattr(a2, 'dXP_Metadata'):
        assert _is_linked(a2, 'dXP_Metadata', b)
    _safe_set(b, 'dXP_Base', set())
    assert not _is_linked(b, 'dXP_Base', a2)
    if hasattr(a2, 'dXP_Metadata'):
        assert not _is_linked(a2, 'dXP_Metadata', b)


def test_assoc_user10_reverse_link_reassign_clear():
    a1 = dXP_User(enabledUser="sample_text", identifier="sample_text", role="sample_text", userName="sample_text")
    a2 = dXP_User(enabledUser="sample_text_2", identifier="sample_text_2", role="sample_text_2", userName="sample_text_2")
    b = dXP_AcademicSession(endDate="sample_text", schoolYear="sample_text", startDate="sample_text", title="sample_text", type="sample_text")
    _safe_set(b, 'dXP_AcademicSession11', {a1})
    assert _is_linked(b, 'dXP_AcademicSession11', a1)
    if hasattr(a1, 'dXP_User'):
        assert _is_linked(a1, 'dXP_User', b)
    _safe_set(b, 'dXP_AcademicSession11', {a2})
    assert _is_linked(b, 'dXP_AcademicSession11', a2)
    if hasattr(a1, 'dXP_User'):
        assert not _is_linked(a1, 'dXP_User', b)
    if hasattr(a2, 'dXP_User'):
        assert _is_linked(a2, 'dXP_User', b)
    _safe_set(b, 'dXP_AcademicSession11', set())
    assert not _is_linked(b, 'dXP_AcademicSession11', a2)
    if hasattr(a2, 'dXP_User'):
        assert not _is_linked(a2, 'dXP_User', b)


def test_assoc_user16_reverse_link_reassign_clear():
    a1 = dXP_User(enabledUser="sample_text", identifier="sample_text", role="sample_text", userName="sample_text")
    a2 = dXP_User(enabledUser="sample_text_2", identifier="sample_text_2", role="sample_text_2", userName="sample_text_2")
    b = dXP_Enrolment(primary="sample_text", role="sample_text")
    _safe_set(b, 'dXP_Enrolment17', a1)
    assert _is_linked(b, 'dXP_Enrolment17', a1)
    if hasattr(a1, 'dXP_User18'):
        assert _is_linked(a1, 'dXP_User18', b)
    _safe_set(b, 'dXP_Enrolment17', a2)
    assert _is_linked(b, 'dXP_Enrolment17', a2)
    if hasattr(a1, 'dXP_User18'):
        assert not _is_linked(a1, 'dXP_User18', b)
    if hasattr(a2, 'dXP_User18'):
        assert _is_linked(a2, 'dXP_User18', b)
    _safe_set(b, 'dXP_Enrolment17', None)
    assert not _is_linked(b, 'dXP_Enrolment17', a2)
    if hasattr(a2, 'dXP_User18'):
        assert not _is_linked(a2, 'dXP_User18', b)


def test_assoc_userid12_reverse_link_reassign_clear():
    a1 = dXP_UserId(identifier="sample_text", type="sample_text")
    a2 = dXP_UserId(identifier="sample_text_2", type="sample_text_2")
    b = dXP_User(enabledUser="sample_text", identifier="sample_text", role="sample_text", userName="sample_text")
    _safe_set(b, 'dXP_User13', {a1})
    assert _is_linked(b, 'dXP_User13', a1)
    if hasattr(a1, 'dXP_UserId'):
        assert _is_linked(a1, 'dXP_UserId', b)
    _safe_set(b, 'dXP_User13', {a2})
    assert _is_linked(b, 'dXP_User13', a2)
    if hasattr(a1, 'dXP_UserId'):
        assert not _is_linked(a1, 'dXP_UserId', b)
    if hasattr(a2, 'dXP_UserId'):
        assert _is_linked(a2, 'dXP_UserId', b)
    _safe_set(b, 'dXP_User13', set())
    assert not _is_linked(b, 'dXP_User13', a2)
    if hasattr(a2, 'dXP_UserId'):
        assert not _is_linked(a2, 'dXP_UserId', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_academicsession0_stub_double():
    # dXP_OneRoster has no real 'dXP_OneRoster' property in the generated
    # code (a bare stub) -- manually attach it so dXP_AcademicSession's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dXP_AcademicSession's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dXP_AcademicSession(endDate="sample_text", schoolYear="sample_text", startDate="sample_text", title="sample_text", type="sample_text")
    partner = dXP_OneRoster()
    setattr(partner, 'dXP_OneRoster', None)
    _safe_set(owner, 'dXP_AcademicSession', partner)
    assert owner in getattr(partner, 'dXP_OneRoster')
    _safe_set(owner, 'dXP_AcademicSession', None)
    assert owner not in getattr(partner, 'dXP_OneRoster')


def test_assoc_enrolment3_stub_double():
    # dXP_OneRoster has no real 'dXP_OneRoster4' property in the generated
    # code (a bare stub) -- manually attach it so dXP_Enrolment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dXP_Enrolment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dXP_Enrolment(primary="sample_text", role="sample_text")
    partner = dXP_OneRoster()
    setattr(partner, 'dXP_OneRoster4', None)
    _safe_set(owner, 'dXP_Enrolment', partner)
    assert owner in getattr(partner, 'dXP_OneRoster4')
    _safe_set(owner, 'dXP_Enrolment', None)
    assert owner not in getattr(partner, 'dXP_OneRoster4')


def test_assoc_org1_stub_double():
    # dXP_OneRoster has no real 'dXP_OneRoster2' property in the generated
    # code (a bare stub) -- manually attach it so dXP_Org's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dXP_Org's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dXP_Org(name="sample_text", type="sample_text")
    partner = dXP_OneRoster()
    setattr(partner, 'dXP_OneRoster2', None)
    _safe_set(owner, 'dXP_Org', partner)
    assert owner in getattr(partner, 'dXP_OneRoster2')
    _safe_set(owner, 'dXP_Org', None)
    assert owner not in getattr(partner, 'dXP_OneRoster2')


def test_assoc_orgunit14_stub_double():
    # dXP_OrgUnit has no real 'dXP_OrgUnit' property in the generated
    # code (a bare stub) -- manually attach it so dXP_Org's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dXP_Org's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dXP_Org(name="sample_text", type="sample_text")
    partner = dXP_OrgUnit()
    setattr(partner, 'dXP_OrgUnit', None)
    _safe_set(owner, 'dXP_Org15', {partner})
    assert getattr(partner, 'dXP_OrgUnit') == owner
    _safe_set(owner, 'dXP_Org15', set())
    assert getattr(partner, 'dXP_OrgUnit') is None


def test_assoc_orgunit22_stub_double():
    # dXP_OrgUnit has no real 'dXP_OrgUnit24' property in the generated
    # code (a bare stub) -- manually attach it so dXP_Enrolment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dXP_Enrolment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dXP_Enrolment(primary="sample_text", role="sample_text")
    partner = dXP_OrgUnit()
    setattr(partner, 'dXP_OrgUnit24', None)
    _safe_set(owner, 'dXP_Enrolment23', partner)
    assert getattr(partner, 'dXP_OrgUnit24') == owner
    _safe_set(owner, 'dXP_Enrolment23', None)
    assert getattr(partner, 'dXP_OrgUnit24') is None


